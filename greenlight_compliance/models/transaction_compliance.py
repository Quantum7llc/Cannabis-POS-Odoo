from odoo import models


class GreenLightTransactionCompliance(models.Model):
    _inherit = "greenlight.transaction"

    def action_confirm(self):
        """Check purchase limits before confirming, then record the purchase."""
        for rec in self:
            self.env["greenlight.purchase.limit"].check_and_record(rec)
        return super().action_confirm()

    def action_void(self):
        """Mark associated purchase limit records as voided."""
        res = super().action_void()
        for rec in self:
            limits = self.env["greenlight.purchase.limit"].search([
                ("transaction_id", "=", rec.id),
                ("voided", "=", False),
            ])
            limits.write({"voided": True})
        return res
