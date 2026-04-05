from odoo import models, fields


class GreenLightMetrcPackage(models.Model):
    _name = "greenlight.metrc.package"
    _description = "Metrc Package (local cache)"
    _order = "last_synced_at desc"

    metrc_tag = fields.Char("Package Tag", required=True, size=24, index=True)
    product_id = fields.Many2one("greenlight.product")
    item_name = fields.Char()
    category = fields.Char()
    quantity = fields.Float(digits=(10, 3))
    unit_of_measure = fields.Char()
    lab_testing_state = fields.Char()
    thc_pct = fields.Float("THC %", digits=(5, 2))
    cbd_pct = fields.Float("CBD %", digits=(5, 2))
    is_on_hold = fields.Boolean(default=False)
    last_synced_at = fields.Datetime()
    metrc_data = fields.Json("Raw Metrc Response")

    _sql_constraints = [
        ("metrc_tag_uniq", "unique(metrc_tag)", "Metrc package tag must be unique."),
    ]
