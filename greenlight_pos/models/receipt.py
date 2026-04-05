from odoo import models, fields, api
from odoo.exceptions import UserError, AccessError
import logging

_logger = logging.getLogger(__name__)


class GreenLightReceipt(models.Model):
    _name = "greenlight.receipt"
    _description = "POS Receipt"
    _inherit = ["mail.thread"]
    _order = "create_date desc"
    _rec_name = "receipt_number"

    receipt_number = fields.Char("Receipt #", readonly=True, copy=False, index=True)
    transaction_id = fields.Many2one(
        "greenlight.transaction",
        required=True,
        ondelete="restrict",
        tracking=True,
        index=True,
    )

    # Denormalized from transaction for fast search / display
    customer_id = fields.Many2one(
        "greenlight.customer",
        related="transaction_id.customer_id",
        store=True,
        readonly=True,
    )
    employee_id = fields.Many2one(
        "greenlight.employee",
        related="transaction_id.employee_id",
        store=True,
        readonly=True,
    )
    customer_name = fields.Char(
        related="customer_id.full_name",
        store=True,
        readonly=True,
        string="Customer Name",
    )
    customer_email = fields.Char(
        related="customer_id.email",
        readonly=True,
        string="Customer Email",
    )

    # Amounts (denormalized for receipt permanence)
    subtotal = fields.Monetary(currency_field="currency_id", readonly=True)
    tax_amount = fields.Monetary(currency_field="currency_id", readonly=True)
    total = fields.Monetary(currency_field="currency_id", readonly=True)
    currency_id = fields.Many2one(
        "res.currency",
        default=lambda self: self.env.company.currency_id,
    )
    payment_method = fields.Selection(
        related="transaction_id.payment_method",
        store=True,
        readonly=True,
    )

    state = fields.Selection(
        [
            ("active", "Active"),
            ("voided", "Voided"),
        ],
        default="active",
        tracking=True,
        readonly=True,
    )

    void_reason = fields.Text("Void Reason", readonly=True)
    void_date = fields.Datetime("Voided At", readonly=True)
    voided_by_id = fields.Many2one("greenlight.employee", "Voided By", readonly=True)

    refund_ids = fields.One2many("greenlight.refund", "receipt_id")
    refund_count = fields.Integer(compute="_compute_refund_count")
    total_refunded = fields.Monetary(
        currency_field="currency_id",
        compute="_compute_refund_totals",
        store=True,
        string="Total Refunded",
    )

    # Dispensary info snapshot (frozen at time of receipt creation)
    dispensary_name = fields.Char(readonly=True)
    dispensary_license = fields.Char("License #", readonly=True)
    dispensary_address = fields.Char(readonly=True)

    notes = fields.Text()

    @api.depends("refund_ids")
    def _compute_refund_count(self):
        for rec in self:
            rec.refund_count = len(rec.refund_ids)

    @api.depends("refund_ids.state", "refund_ids.refund_total")
    def _compute_refund_totals(self):
        for rec in self:
            processed = rec.refund_ids.filtered(lambda r: r.state == "processed")
            rec.total_refunded = sum(processed.mapped("refund_total"))

    @api.model_create_multi
    def create(self, vals_list):
        settings = self.env["greenlight.settings"].get_active_settings()
        for vals in vals_list:
            if not vals.get("receipt_number"):
                vals["receipt_number"] = (
                    self.env["ir.sequence"].next_by_code("greenlight.receipt") or "RCT-0000"
                )
            # Snapshot transaction amounts
            if vals.get("transaction_id"):
                txn = self.env["greenlight.transaction"].browse(vals["transaction_id"])
                vals.setdefault("subtotal", txn.subtotal)
                vals.setdefault("tax_amount", txn.tax_amount)
                vals.setdefault("total", txn.total)
            # Snapshot dispensary info
            vals.setdefault("dispensary_name", settings.dispensary_name or "")
            vals.setdefault("dispensary_license", settings.dispensary_license or "")
            addr_parts = [
                settings.dispensary_address or "",
                settings.dispensary_city or "",
                settings.dispensary_state or "",
                settings.dispensary_zip or "",
            ]
            vals.setdefault("dispensary_address", ", ".join(p for p in addr_parts if p))
        return super().create(vals_list)

    # -------------------------------------------------------------------------
    # Actions
    # -------------------------------------------------------------------------

    def action_void(self):
        """Void this receipt. Requires manager or admin role on the current employee.

        Reverses inventory for all transaction lines and marks associated
        purchase limit records as voided.
        """
        self.ensure_one()
        if self.state != "active":
            raise UserError("Only active receipts can be voided.")
        if self.transaction_id.state == "voided":
            raise UserError("The underlying transaction is already voided.")

        employee = self._get_authorized_employee(("manager", "admin"))

        # Void the transaction (this reverses inventory via transaction.action_void)
        self.transaction_id.action_void()

        # Mark purchase limit records voided (if compliance module is installed)
        self._void_purchase_limits()

        self.write({
            "state": "voided",
            "void_date": fields.Datetime.now(),
            "voided_by_id": employee.id,
        })
        self.message_post(
            body=f"Receipt voided by {employee.name}.",
            message_type="notification",
        )
        return True

    def action_void_with_reason(self):
        """Open a wizard to capture the void reason before voiding."""
        self.ensure_one()
        if self.state != "active":
            raise UserError("Only active receipts can be voided.")
        return {
            "type": "ir.actions.act_window",
            "name": "Void Receipt",
            "res_model": "greenlight.receipt.void.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {"default_receipt_id": self.id},
        }

    def action_email_receipt(self):
        """Send the receipt to the customer's email address."""
        self.ensure_one()
        if not self.customer_email:
            raise UserError("Customer does not have an email address on file.")
        template = self.env.ref("greenlight_pos.email_template_receipt", raise_if_not_found=False)
        if template:
            template.send_mail(self.id, force_send=True)
            self.message_post(
                body=f"Receipt emailed to {self.customer_email}.",
                message_type="notification",
            )
        else:
            raise UserError(
                "Receipt email template not found. "
                "Please configure the email template (greenlight_pos.email_template_receipt)."
            )
        return True

    def action_view_refunds(self):
        """Open refunds related to this receipt."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Refunds",
            "res_model": "greenlight.refund",
            "view_mode": "list,form",
            "domain": [("receipt_id", "=", self.id)],
            "context": {"default_receipt_id": self.id},
        }

    def action_create_refund(self):
        """Open the refund creation form pre-linked to this receipt."""
        self.ensure_one()
        if self.state != "active":
            raise UserError("Cannot create a refund for a voided receipt.")
        return {
            "type": "ir.actions.act_window",
            "name": "Create Refund",
            "res_model": "greenlight.refund",
            "view_mode": "form",
            "target": "current",
            "context": {
                "default_receipt_id": self.id,
                "default_transaction_id": self.transaction_id.id,
                "default_customer_id": self.customer_id.id,
            },
        }

    # -------------------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------------------

    def _get_authorized_employee(self, allowed_roles):
        """Return the current user's linked employee and verify role.

        The system maps the current Odoo user to a greenlight.employee via the
        security group. For void/refund operations we also check the employee
        record's role field.
        """
        user = self.env.user
        if user.has_group("greenlight_pos.group_manager"):
            # User has at least manager-level access; look up their employee record
            employee = self.env["greenlight.employee"].search(
                [("name", "=", user.name), ("is_active", "=", True)],
                limit=1,
            )
            if not employee:
                # Fallback: any active manager/admin employee (for Odoo admin users)
                employee = self.env["greenlight.employee"].search(
                    [("role", "in", list(allowed_roles)), ("is_active", "=", True)],
                    limit=1,
                )
            if employee and employee.role in allowed_roles:
                return employee
        raise AccessError(
            f"This action requires {' or '.join(allowed_roles)} role. "
            "Your account does not have the required permissions."
        )

    def _void_purchase_limits(self):
        """Mark purchase limit records for this transaction as voided.

        Handles both cases: compliance module installed or not.
        """
        try:
            PurchaseLimit = self.env["greenlight.purchase.limit"].sudo()
            limits = PurchaseLimit.search([
                ("transaction_id", "=", self.transaction_id.id),
                ("voided", "=", False),
            ])
            if limits:
                limits.write({"voided": True})
                _logger.info(
                    "Voided %d purchase limit records for transaction %s",
                    len(limits),
                    self.transaction_id.name,
                )
        except KeyError:
            # greenlight_compliance module not installed
            pass


class GreenLightRefund(models.Model):
    _name = "greenlight.refund"
    _description = "Receipt Refund"
    _inherit = ["mail.thread"]
    _order = "create_date desc"
    _rec_name = "refund_number"

    refund_number = fields.Char("Refund #", readonly=True, copy=False, index=True)
    receipt_id = fields.Many2one(
        "greenlight.receipt",
        required=True,
        ondelete="restrict",
        tracking=True,
        index=True,
    )
    transaction_id = fields.Many2one(
        "greenlight.transaction",
        required=True,
        ondelete="restrict",
        tracking=True,
    )
    customer_id = fields.Many2one(
        "greenlight.customer",
        related="receipt_id.customer_id",
        store=True,
        readonly=True,
    )
    processed_by_id = fields.Many2one("greenlight.employee", "Processed By", readonly=True)

    line_ids = fields.One2many("greenlight.refund.line", "refund_id")

    refund_total = fields.Monetary(
        currency_field="currency_id",
        compute="_compute_refund_total",
        store=True,
    )
    currency_id = fields.Many2one(
        "res.currency",
        default=lambda self: self.env.company.currency_id,
    )

    reason = fields.Text("Refund Reason", required=True)

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("processed", "Processed"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        tracking=True,
    )

    process_date = fields.Datetime("Processed At", readonly=True)

    @api.depends("line_ids.refund_amount")
    def _compute_refund_total(self):
        for rec in self:
            rec.refund_total = sum(rec.line_ids.mapped("refund_amount"))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("refund_number"):
                vals["refund_number"] = (
                    self.env["ir.sequence"].next_by_code("greenlight.refund") or "RFD-0000"
                )
        return super().create(vals_list)

    # -------------------------------------------------------------------------
    # Actions
    # -------------------------------------------------------------------------

    def action_process(self):
        """Process this refund: restore inventory, adjust purchase limits, finalize."""
        self.ensure_one()
        if self.state != "draft":
            raise UserError("Only draft refunds can be processed.")
        if self.receipt_id.state != "active":
            raise UserError("Cannot process a refund for a voided receipt.")
        if not self.line_ids:
            raise UserError("Add at least one refund line item before processing.")

        employee = self.receipt_id._get_authorized_employee(("manager", "admin"))

        self._validate_refund_quantities()
        self._restore_inventory()
        self._adjust_purchase_limits()

        self.write({
            "state": "processed",
            "process_date": fields.Datetime.now(),
            "processed_by_id": employee.id,
        })
        self.message_post(
            body=f"Refund {self.refund_number} processed by {employee.name}. "
                 f"Amount: {self.refund_total:.2f}",
            message_type="notification",
        )
        return True

    def action_cancel(self):
        """Cancel a draft refund."""
        self.ensure_one()
        if self.state != "draft":
            raise UserError("Only draft refunds can be cancelled.")
        self.state = "cancelled"
        return True

    # -------------------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------------------

    def _validate_refund_quantities(self):
        """Ensure refund quantities do not exceed what was originally purchased,
        accounting for previously processed refunds on the same receipt."""
        for line in self.line_ids:
            # Find the original transaction line for this product
            orig_lines = self.transaction_id.line_ids.filtered(
                lambda l: l.product_id.id == line.product_id.id
            )
            if not orig_lines:
                raise UserError(
                    f"Product '{line.product_id.name}' was not in the original transaction."
                )
            original_qty = sum(orig_lines.mapped("quantity"))

            # Sum already-refunded quantity for this product on this receipt
            already_refunded = 0.0
            for prev_refund in self.receipt_id.refund_ids.filtered(
                lambda r: r.state == "processed" and r.id != self.id
            ):
                for prev_line in prev_refund.line_ids.filtered(
                    lambda l: l.product_id.id == line.product_id.id
                ):
                    already_refunded += prev_line.quantity

            available = original_qty - already_refunded
            if line.quantity > available:
                raise UserError(
                    f"Cannot refund {line.quantity} of '{line.product_id.name}'. "
                    f"Original qty: {original_qty}, already refunded: {already_refunded}, "
                    f"available: {available}."
                )

    def _restore_inventory(self):
        """Restore inventory counts for each refunded item using atomic SQL."""
        for line in self.line_ids:
            self.env.cr.execute(
                "UPDATE greenlight_product SET inventory_count = inventory_count + %s "
                "WHERE id = %s",
                (line.quantity, line.product_id.id),
            )
            line.product_id.invalidate_recordset(["inventory_count"])

    def _adjust_purchase_limits(self):
        """Reduce purchase limit weight_grams and mmceu_units for refunded items.

        This makes the refunded weight available again within the 30-day window.
        Handles both cases: compliance module installed or not.
        """
        try:
            PurchaseLimit = self.env["greenlight.purchase.limit"].sudo()
        except KeyError:
            # greenlight_compliance module not installed
            return

        limits = PurchaseLimit.search([
            ("transaction_id", "=", self.transaction_id.id),
            ("voided", "=", False),
        ])
        if not limits:
            return

        # Sum the weight being refunded, by product type
        refund_grams = 0.0
        refund_mmceu = 0.0
        for line in self.line_ids:
            if line.cannabis_type == "accessory":
                continue
            grams = line.weight_grams * line.quantity
            mmceu = PurchaseLimit.calculate_mmceu(
                line.cannabis_type,
                grams,
                line.product_id.thc_percentage,
            )
            refund_grams += grams
            refund_mmceu += mmceu

        if refund_grams <= 0 and refund_mmceu <= 0:
            return

        # Reduce from the first matching purchase limit record
        # (a transaction typically produces one purchase limit record)
        limit_rec = limits[0]
        new_grams = max(0.0, limit_rec.weight_grams - refund_grams)
        new_mmceu = max(0.0, limit_rec.mmceu_units - refund_mmceu)
        limit_rec.write({
            "weight_grams": new_grams,
            "mmceu_units": new_mmceu,
        })
        _logger.info(
            "Adjusted purchase limits for transaction %s: grams %.3f -> %.3f, "
            "mmceu %.3f -> %.3f",
            self.transaction_id.name,
            limit_rec.weight_grams + refund_grams,
            new_grams,
            limit_rec.mmceu_units + refund_mmceu,
            new_mmceu,
        )


class GreenLightRefundLine(models.Model):
    _name = "greenlight.refund.line"
    _description = "Refund Line Item"

    refund_id = fields.Many2one("greenlight.refund", required=True, ondelete="cascade")
    product_id = fields.Many2one("greenlight.product", required=True, string="Product")
    quantity = fields.Integer(required=True, default=1)
    unit_price = fields.Monetary(
        currency_field="currency_id",
        string="Unit Price",
        help="Refund price per unit (defaults to original sale price)",
    )
    refund_amount = fields.Monetary(
        currency_field="currency_id",
        compute="_compute_refund_amount",
        store=True,
    )
    currency_id = fields.Many2one(
        "res.currency",
        default=lambda self: self.env.company.currency_id,
    )

    # Cannabis tracking (for purchase limit adjustment)
    weight_grams = fields.Float(related="product_id.weight_grams", readonly=True)
    cannabis_type = fields.Selection(related="product_id.cannabis_type", readonly=True)

    @api.depends("quantity", "unit_price")
    def _compute_refund_amount(self):
        for rec in self:
            rec.refund_amount = rec.quantity * rec.unit_price
