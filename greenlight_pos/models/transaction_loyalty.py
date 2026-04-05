from odoo import models


class GreenLightTransactionLoyalty(models.Model):
    _inherit = "greenlight.transaction"

    def action_confirm(self):
        """Override to award loyalty points after confirming."""
        res = super().action_confirm()
        loyalty_config = self.env["greenlight.loyalty.config"].get_config()
        for rec in self:
            if rec.customer_id and rec.state == "confirmed":
                loyalty_config.earn_points(rec.customer_id, rec)
        return res
