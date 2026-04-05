from odoo import models, fields


class GenerateDummyRatesWizard(models.TransientModel):
    _name = "greenlight.exchange.generate.dummy.wizard"
    _description = "Generate Dummy Exchange Rates"

    days = fields.Integer("Number of Days", default=90, required=True)

    def action_generate(self):
        """Generate dummy rates and show the result."""
        count = self.env["greenlight.exchange.rate"].generate_dummy_rates(days=self.days)
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": "Dummy Data Generated",
                "message": f"Created {count} exchange rate entries over {self.days} days.",
                "type": "success",
                "sticky": False,
            },
        }
