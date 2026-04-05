import json
import logging
import time

import requests
from odoo import models, fields, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

METRC_SANDBOX_URL = "https://sandbox-api-ms.metrc.com"
METRC_PRODUCTION_URL = "https://api-ms.metrc.com"

# Rate-limit: minimum seconds between Metrc API calls (5 req/sec = 200ms)
_METRC_RATE_LIMIT_SECS = 0.2
# Maximum transactions per POST batch
_METRC_SALES_BATCH_SIZE = 50


class GreenLightMetrcConfig(models.Model):
    _name = "greenlight.metrc.config"
    _description = "Metrc API Configuration"
    _order = "facility_name"

    facility_license = fields.Char("Facility License", required=True)
    facility_name = fields.Char(required=True)
    api_key = fields.Char("Vendor API Key", required=True, groups="greenlight_pos.group_admin")
    user_key = fields.Char("User API Key", required=True, groups="greenlight_pos.group_admin")
    environment = fields.Selection(
        [("sandbox", "Sandbox"), ("production", "Production")],
        default="sandbox",
        required=True,
    )
    base_url = fields.Char(
        compute="_compute_base_url",
        store=True,
    )
    auto_sync = fields.Boolean("Auto-Sync Sales", default=False)
    sync_interval_minutes = fields.Integer(default=15)
    last_sync_at = fields.Datetime(readonly=True)
    is_active = fields.Boolean(default=True)

    sync_log_ids = fields.One2many("greenlight.metrc.sync.log", "config_id")

    @api.depends("environment")
    def _compute_base_url(self):
        for rec in self:
            rec.base_url = METRC_PRODUCTION_URL if rec.environment == "production" else METRC_SANDBOX_URL

    def _get_auth(self):
        """Return HTTP Basic Auth tuple for Metrc API."""
        self.ensure_one()
        return (self.api_key, self.user_key)

    # ------------------------------------------------------------------
    # Shared API helper
    # ------------------------------------------------------------------

    def _metrc_request(self, method, endpoint, data=None):
        """Execute an HTTP request against the Metrc API.

        Handles authentication, rate limiting, sync-log recording, and
        error translation into ``UserError``.

        Args:
            method: HTTP method string ("GET", "POST", "PUT", "DELETE").
            endpoint: API path, e.g. "/packages/v2/active".
            data: Optional dict/list payload (will be JSON-encoded for
                  POST/PUT).

        Returns:
            ``requests.Response`` on success (2xx).

        Raises:
            ``UserError`` on HTTP or network errors.
        """
        self.ensure_one()

        url = f"{self.base_url}{endpoint}"
        if "?" in endpoint:
            url += f"&licenseNumber={self.facility_license}"
        else:
            url += f"?licenseNumber={self.facility_license}"

        headers = {"Content-Type": "application/json"}
        direction = "outbound" if method in ("POST", "PUT", "DELETE") else "inbound"
        request_body_str = json.dumps(data) if data is not None else None

        start = time.time()
        log_vals = {
            "config_id": self.id,
            "direction": direction,
            "endpoint": endpoint,
            "method": method,
            "request_body": request_body_str,
        }

        try:
            resp = requests.request(
                method,
                url,
                auth=self._get_auth(),
                headers=headers,
                json=data if data is not None else None,
                timeout=30,
            )
            elapsed_ms = int((time.time() - start) * 1000)

            # Truncate large response bodies to 64 KB for DB storage
            resp_text = resp.text[:65536] if resp.text else ""

            log_vals.update({
                "response_status": resp.status_code,
                "response_body": resp_text,
                "duration_ms": elapsed_ms,
                "success": 200 <= resp.status_code < 300,
            })

            # Rate-limit sleep AFTER the call so the next request won't
            # fire sooner than the minimum interval.
            time.sleep(_METRC_RATE_LIMIT_SECS)

            if not (200 <= resp.status_code < 300):
                log_vals["error_message"] = f"HTTP {resp.status_code}: {resp_text[:500]}"
                self.env["greenlight.metrc.sync.log"].sudo().create(log_vals)
                raise UserError(
                    f"Metrc API error on {method} {endpoint}: "
                    f"HTTP {resp.status_code}\n{resp_text[:500]}"
                )

            self.env["greenlight.metrc.sync.log"].sudo().create(log_vals)
            return resp

        except requests.RequestException as exc:
            elapsed_ms = int((time.time() - start) * 1000)
            log_vals.update({
                "response_status": 0,
                "duration_ms": elapsed_ms,
                "success": False,
                "error_message": str(exc),
            })
            self.env["greenlight.metrc.sync.log"].sudo().create(log_vals)
            raise UserError(f"Metrc connection failed on {method} {endpoint}: {exc}") from exc

    # ------------------------------------------------------------------
    # Test connection (uses shared helper)
    # ------------------------------------------------------------------

    def action_test_connection(self):
        """Test the Metrc API connection."""
        self.ensure_one()
        resp = self._metrc_request("GET", "/facilities/v2")
        facilities = resp.json()
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "message": (
                    f"Connected to Metrc ({self.environment}). "
                    f"{len(facilities)} facilities found."
                ),
                "type": "success",
            },
        }

    # ------------------------------------------------------------------
    # Package sync (inbound)
    # ------------------------------------------------------------------

    def action_sync_packages(self):
        """Pull active packages from Metrc and upsert into local cache."""
        self.ensure_one()
        resp = self._metrc_request("GET", "/packages/v2/active")
        packages = resp.json()

        MetrcPackage = self.env["greenlight.metrc.package"].sudo()
        now = fields.Datetime.now()
        created = 0
        updated = 0

        for pkg in packages:
            tag = str(pkg.get("Label") or pkg.get("TagId") or "").strip()
            if not tag:
                continue

            vals = {
                "item_name": pkg.get("Item", {}).get("Name") if isinstance(pkg.get("Item"), dict) else pkg.get("ItemName", ""),
                "category": pkg.get("Item", {}).get("ProductCategoryName") if isinstance(pkg.get("Item"), dict) else pkg.get("ProductCategoryName", ""),
                "quantity": pkg.get("Quantity", 0.0),
                "unit_of_measure": pkg.get("UnitOfMeasureName", ""),
                "lab_testing_state": pkg.get("LabTestingState", ""),
                "is_on_hold": bool(pkg.get("IsOnHold", False)),
                "last_synced_at": now,
                "metrc_data": pkg,
            }

            # Extract THC/CBD from lab results if present
            lab_results = pkg.get("LabTestingResults") or []
            for result in (lab_results if isinstance(lab_results, list) else []):
                analyte = (result.get("LabTestResultAnalyteName") or "").lower()
                if "thc" in analyte and "total" in analyte:
                    vals["thc_pct"] = result.get("LabTestResultValue", 0.0)
                elif "cbd" in analyte and "total" in analyte:
                    vals["cbd_pct"] = result.get("LabTestResultValue", 0.0)

            existing = MetrcPackage.search([("metrc_tag", "=", tag)], limit=1)
            if existing:
                existing.write(vals)
                updated += 1
            else:
                vals["metrc_tag"] = tag
                MetrcPackage.create(vals)
                created += 1

        self.last_sync_at = now

        _logger.info(
            "Metrc package sync for %s: %d created, %d updated out of %d",
            self.facility_license, created, updated, len(packages),
        )

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "message": (
                    f"Package sync complete: {created} created, "
                    f"{updated} updated ({len(packages)} from Metrc)."
                ),
                "type": "success",
            },
        }

    # ------------------------------------------------------------------
    # Sales sync (outbound)
    # ------------------------------------------------------------------

    def action_sync_sales(self):
        """Push pending confirmed transactions to Metrc as sales receipts.

        Batches transactions in groups of 50, rate-limited to 5 req/sec.
        Updates each transaction's ``metrc_sync_status`` and
        ``metrc_receipt_id`` on success.
        """
        self.ensure_one()

        Transaction = self.env["greenlight.transaction"].sudo()
        pending_txns = Transaction.search([
            ("state", "=", "confirmed"),
            ("metrc_sync_status", "=", "pending"),
        ], order="create_date asc")

        if not pending_txns:
            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "message": "No pending transactions to sync.",
                    "type": "info",
                },
            }

        total_synced = 0
        total_failed = 0

        # Process in batches of _METRC_SALES_BATCH_SIZE
        for batch_start in range(0, len(pending_txns), _METRC_SALES_BATCH_SIZE):
            batch = pending_txns[batch_start:batch_start + _METRC_SALES_BATCH_SIZE]
            receipts = []

            for txn in batch:
                receipt = self._build_metrc_receipt(txn)
                if receipt:
                    receipts.append(receipt)
                else:
                    # Accessory-only or no cannabis lines — skip
                    txn.metrc_sync_status = "skipped"

            if not receipts:
                continue

            try:
                resp = self._metrc_request("POST", "/sales/v2/receipts", receipts)

                # Metrc typically returns the created receipt IDs in the
                # response or simply returns 200 with an empty body.
                receipt_ids = []
                try:
                    resp_data = resp.json()
                    if isinstance(resp_data, list):
                        receipt_ids = [str(r.get("Id", "")) for r in resp_data]
                except (ValueError, AttributeError):
                    pass

                for idx, txn in enumerate(batch):
                    if txn.metrc_sync_status == "skipped":
                        continue
                    txn.metrc_sync_status = "synced"
                    if idx < len(receipt_ids) and receipt_ids[idx]:
                        txn.metrc_receipt_id = receipt_ids[idx]
                    total_synced += 1

                # Log the transaction IDs in the sync log for auditability
                log_entry = self.env["greenlight.metrc.sync.log"].sudo().search([
                    ("config_id", "=", self.id),
                    ("endpoint", "=", "/sales/v2/receipts"),
                    ("method", "=", "POST"),
                ], limit=1, order="create_date desc")
                if log_entry:
                    txn_names = ", ".join(batch.mapped("name"))
                    log_entry.response_body = (
                        (log_entry.response_body or "") +
                        f"\n[Transactions: {txn_names}]"
                    )

            except UserError as exc:
                _logger.warning(
                    "Metrc sales sync batch failed for %s: %s",
                    self.facility_license, exc,
                )
                for txn in batch:
                    if txn.metrc_sync_status != "skipped":
                        txn.metrc_sync_status = "failed"
                        total_failed += 1

        self.last_sync_at = fields.Datetime.now()

        msg_parts = []
        if total_synced:
            msg_parts.append(f"{total_synced} synced")
        if total_failed:
            msg_parts.append(f"{total_failed} failed")
        skipped = len(pending_txns) - total_synced - total_failed
        if skipped > 0:
            msg_parts.append(f"{skipped} skipped")

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "message": f"Sales sync complete: {', '.join(msg_parts)}.",
                "type": "warning" if total_failed else "success",
            },
        }

    def _build_metrc_receipt(self, transaction):
        """Build a Metrc-compatible sales receipt dict from a transaction.

        Returns ``None`` if the transaction has no cannabis line items
        (accessory-only sale).
        """
        lines = []
        for line in transaction.line_ids:
            product = line.product_id
            # Skip accessories — Metrc only tracks cannabis
            if product.cannabis_type == "accessory":
                continue

            package_tag = product.metrc_tag or ""
            lines.append({
                "PackageLabel": package_tag,
                "Quantity": line.quantity,
                "UnitOfMeasure": "Each",
                "TotalAmount": line.subtotal + line.tax,
            })

        if not lines:
            return None

        customer = transaction.customer_id
        return {
            "SalesDateTime": fields.Datetime.to_string(transaction.create_date).replace(" ", "T"),
            "SalesCustomerType": "Patient" if customer.medical_card_number else "Consumer",
            "PatientLicenseNumber": customer.medical_card_number or "",
            "Transactions": lines,
        }

    # ------------------------------------------------------------------
    # Combined sync
    # ------------------------------------------------------------------

    def action_sync_all(self):
        """Run a full sync: packages (inbound) then sales (outbound)."""
        self.ensure_one()
        self.action_sync_packages()
        self.action_sync_sales()
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "message": "Full Metrc sync completed (packages + sales).",
                "type": "success",
            },
        }

    # ------------------------------------------------------------------
    # Cron entry point
    # ------------------------------------------------------------------

    @api.model
    def cron_sync_all(self):
        """Called by the scheduled action. Syncs all active configs
        that have auto_sync enabled."""
        configs = self.search([
            ("is_active", "=", True),
            ("auto_sync", "=", True),
        ])
        for config in configs:
            try:
                config.action_sync_all()
            except UserError as exc:
                _logger.error(
                    "Metrc cron sync failed for %s (%s): %s",
                    config.facility_name, config.facility_license, exc,
                )
            except Exception:
                _logger.exception(
                    "Unexpected error during Metrc cron sync for %s (%s)",
                    config.facility_name, config.facility_license,
                )
