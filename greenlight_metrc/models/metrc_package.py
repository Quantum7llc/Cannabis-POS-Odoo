import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


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

    def action_link_to_product(self):
        """Attempt to match this Metrc package to a local product.

        Matching strategy (first match wins):
        1. Exact match on ``greenlight.product.metrc_tag``.
        2. Exact match on ``greenlight.product.sku`` vs. package tag.
        3. Case-insensitive substring match on product name vs. Metrc
           ``item_name``.

        If a match is found the package's ``product_id`` is set and the
        product's ``metrc_tag`` is updated.  If no match is found a
        notification is returned so the user can link manually.
        """
        self.ensure_one()

        Product = self.env["greenlight.product"].sudo()

        # Strategy 1: product already carries this tag
        product = Product.search([("metrc_tag", "=", self.metrc_tag)], limit=1)

        # Strategy 2: SKU matches the tag
        if not product:
            product = Product.search([("sku", "=", self.metrc_tag)], limit=1)

        # Strategy 3: name contains the Metrc item_name (case-insensitive)
        if not product and self.item_name:
            product = Product.search([("name", "=ilike", self.item_name)], limit=1)
            if not product:
                # Try partial match
                product = Product.search(
                    [("name", "ilike", self.item_name)], limit=1
                )

        if product:
            self.product_id = product.id
            product.metrc_tag = self.metrc_tag
            _logger.info(
                "Linked Metrc package %s to product %s (id=%s)",
                self.metrc_tag, product.name, product.id,
            )
            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "message": f"Linked to product: {product.name} ({product.sku})",
                    "type": "success",
                },
            }

        # No match — open a form to let the user pick manually
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "message": (
                    f"No matching product found for '{self.item_name}' "
                    f"(tag {self.metrc_tag}). Please set the product manually."
                ),
                "type": "warning",
                "sticky": True,
            },
        }
