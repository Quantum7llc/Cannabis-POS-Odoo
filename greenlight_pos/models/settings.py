from odoo import models, fields, api


class GreenLightSettings(models.Model):
    _name = "greenlight.settings"
    _description = "Dispensary Settings"

    name = fields.Char(required=True, default="Default")
    tax_rate = fields.Float(
        "Sales Tax Rate",
        digits=(5, 4),
        default=0.07,
        help="Mississippi sales tax rate (e.g., 0.07 = 7%). Applied to all transaction line items.",
    )
    dispensary_name = fields.Char("Dispensary Name")
    dispensary_license = fields.Char("State License #")
    dispensary_dea = fields.Char("DEA Number")
    dispensary_phone = fields.Char("Phone")
    dispensary_address = fields.Char("Address")
    dispensary_city = fields.Char("City")
    dispensary_state = fields.Char("State", default="MS", size=2)
    dispensary_zip = fields.Char("ZIP", size=10)

    is_active = fields.Boolean(default=True)

    @api.model
    def get_active_settings(self):
        """Return the active settings record, or create a default one."""
        settings = self.search([("is_active", "=", True)], limit=1)
        if not settings:
            settings = self.create({"name": "Default"})
        return settings

    @api.model
    def get_tax_rate(self):
        """Convenience method to get the current tax rate."""
        return self.get_active_settings().tax_rate
