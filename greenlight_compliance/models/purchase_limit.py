from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta


# Mississippi MMCP limits
MAX_GRAMS = 84.0
MAX_MMCEU = 24.0
ROLLING_DAYS = 30


class GreenLightPurchaseLimit(models.Model):
    _name = "greenlight.purchase.limit"
    _description = "Rolling 30-Day Purchase Limit Tracking"
    _order = "purchase_date desc"

    customer_id = fields.Many2one("greenlight.customer", required=True, index=True)
    transaction_id = fields.Many2one("greenlight.transaction", required=True, index=True)
    purchase_date = fields.Datetime(required=True)
    weight_grams = fields.Float("Flower-Equivalent Grams", digits=(10, 3))
    mmceu_units = fields.Float("MMCEU", digits=(10, 3))
    product_type = fields.Selection(
        [
            ("flower", "Flower"),
            ("concentrate", "Concentrate"),
            ("infused", "Infused"),
            ("accessory", "Accessory"),
        ],
        required=True,
        default="flower",
    )
    reset_at = fields.Datetime("Falls Off At", required=True, help="purchase_date + 30 days")
    voided = fields.Boolean(default=False)

    @api.model
    def calculate_mmceu(self, cannabis_type, weight_grams, thc_pct):
        """Calculate MMCEU for a given product.

        See docs/shared-compliance/mmceu-calculation.md for the canonical rules.
        Both Rust and Odoo implementations MUST produce identical results.
        """
        if cannabis_type == "flower":
            return weight_grams / 3.5
        elif cannabis_type in ("concentrate", "infused"):
            return weight_grams * thc_pct / 100.0
        else:
            return 0.0

    @api.model
    def get_rolling_totals(self, customer_id):
        """Get a customer's current rolling 30-day totals."""
        now = fields.Datetime.now()
        records = self.search([
            ("customer_id", "=", customer_id),
            ("voided", "=", False),
            ("reset_at", ">", now),
        ])
        total_grams = sum(records.mapped("weight_grams"))
        total_mmceu = sum(records.mapped("mmceu_units"))
        return {
            "total_grams": total_grams,
            "total_mmceu": total_mmceu,
            "remaining_grams": MAX_GRAMS - total_grams,
            "remaining_mmceu": MAX_MMCEU - total_mmceu,
            "at_limit": total_grams >= MAX_GRAMS or total_mmceu >= MAX_MMCEU,
        }

    @api.model
    def check_and_record(self, transaction):
        """Check limits before confirming a transaction, then record the purchase.

        Raises UserError if the transaction would exceed limits.
        """
        totals = self.get_rolling_totals(transaction.customer_id.id)

        # Calculate what this transaction would add
        txn_grams = 0.0
        txn_mmceu = 0.0
        for line in transaction.line_ids:
            if line.cannabis_type == "accessory":
                continue
            grams = line.weight_grams * line.quantity
            mmceu = self.calculate_mmceu(line.cannabis_type, grams, line.product_id.thc_percentage)
            txn_grams += grams
            txn_mmceu += mmceu

        if totals["total_grams"] + txn_grams > MAX_GRAMS:
            raise UserError(
                f"Purchase would exceed 30-day limit. "
                f"Current: {totals['total_grams']:.1f}g, "
                f"This order: {txn_grams:.1f}g, "
                f"Limit: {MAX_GRAMS}g"
            )

        if totals["total_mmceu"] + txn_mmceu > MAX_MMCEU:
            raise UserError(
                f"Purchase would exceed 30-day MMCEU limit. "
                f"Current: {totals['total_mmceu']:.2f}, "
                f"This order: {txn_mmceu:.2f}, "
                f"Limit: {MAX_MMCEU}"
            )

        # Record the purchase
        now = fields.Datetime.now()
        self.create({
            "customer_id": transaction.customer_id.id,
            "transaction_id": transaction.id,
            "purchase_date": now,
            "weight_grams": txn_grams,
            "mmceu_units": txn_mmceu,
            "product_type": "flower",  # Simplified; real impl tracks per-line
            "reset_at": now + timedelta(days=ROLLING_DAYS),
        })
