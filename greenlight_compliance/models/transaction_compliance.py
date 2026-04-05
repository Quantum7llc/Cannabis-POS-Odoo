from odoo import models


class GreenLightTransactionCompliance(models.Model):
    _inherit = "greenlight.transaction"

    def action_confirm(self):
        """Check purchase limits before confirming, then record the purchase."""
        PurchaseLimit = self.env["greenlight.purchase.limit"].sudo()
        for rec in self:
            if rec.state != "draft":
                continue
            PurchaseLimit.check_and_record(rec)
        return super().action_confirm()

    def action_void(self):
        """Mark associated purchase limit records as voided."""
        res = super().action_void()
        PurchaseLimit = self.env["greenlight.purchase.limit"].sudo()
        for rec in self:
            limits = PurchaseLimit.search([
                ("transaction_id", "=", rec.id),
                ("voided", "=", False),
            ])
            limits.write({"voided": True})
        return res
