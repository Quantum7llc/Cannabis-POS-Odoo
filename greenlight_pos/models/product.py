from odoo import models, fields, api


PRODUCT_TYPE_KEYWORDS = {
    "flower": ["flower", "bud", "pre-roll", "preroll"],
    "concentrate": ["concentrate", "extract", "wax", "shatter", "rosin"],
    "infused": ["edible", "gummy", "chocolate", "beverage", "tincture", "capsule"],
}


class GreenLightProduct(models.Model):
    _name = "greenlight.product"
    _description = "Cannabis Product"
    _inherit = ["mail.thread"]
    _order = "name"

    name = fields.Char(required=True, tracking=True)
    sku = fields.Char(required=True, index=True)
    category_id = fields.Many2one("greenlight.product.category", required=True)
    cannabis_type = fields.Selection(
        [
            ("flower", "Flower"),
            ("concentrate", "Concentrate"),
            ("infused", "Infused/Edible"),
            ("accessory", "Accessory"),
        ],
        compute="_compute_cannabis_type",
        store=True,
        help="Derived from category for MMCEU calculation.",
    )

    # Cannabinoid content
    thc_percentage = fields.Float("THC %", digits=(5, 2))
    cbd_percentage = fields.Float("CBD %", digits=(5, 2))

    # Weight and pricing
    weight_grams = fields.Float("Weight (g)", digits=(10, 3))
    price = fields.Monetary(currency_field="currency_id")
    cost = fields.Monetary("Cost (COGS)", currency_field="currency_id", help="Wholesale cost for 280E COGS tracking")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)

    # Inventory
    inventory_count = fields.Integer("Stock Qty", default=0)
    metrc_tag = fields.Char("Metrc Package Tag", size=24, index=True)

    # Status
    is_active = fields.Boolean(default=True)

    @api.depends("category_id", "category_id.name")
    def _compute_cannabis_type(self):
        for rec in self:
            cat_name = (rec.category_id.name or "").lower()
            rec.cannabis_type = "accessory"
            for ptype, keywords in PRODUCT_TYPE_KEYWORDS.items():
                if any(kw in cat_name for kw in keywords):
                    rec.cannabis_type = ptype
                    break


class GreenLightProductCategory(models.Model):
    _name = "greenlight.product.category"
    _description = "Cannabis Product Category"
    _order = "name"

    name = fields.Char(required=True)
    parent_id = fields.Many2one("greenlight.product.category", "Parent Category")
    product_ids = fields.One2many("greenlight.product", "category_id")
    product_count = fields.Integer(compute="_compute_product_count")

    @api.depends("product_ids")
    def _compute_product_count(self):
        for rec in self:
            rec.product_count = len(rec.product_ids)
