from odoo import api, models


class InventoryReport(models.AbstractModel):
    """Custom report model for current stock listing.

    Fetches all active products grouped by category, with totals.
    This report is printed from a product record but shows ALL active products.
    """
    _name = "report.greenlight_pos.report_inventory_document"
    _description = "Inventory Stock Report Data"

    @api.model
    def _get_report_values(self, docids, data=None):
        products = self.env["greenlight.product"].search(
            [("is_active", "=", True)],
            order="category_id, name",
        )

        # Group by category
        categories = {}
        total_stock = 0
        total_cost_value = 0.0
        total_retail_value = 0.0
        for product in products:
            cat_name = product.category_id.name or "Uncategorized"
            cat_id = product.category_id.id or 0
            if cat_id not in categories:
                categories[cat_id] = {
                    "name": cat_name,
                    "products": [],
                    "subtotal_qty": 0,
                    "subtotal_cost": 0.0,
                    "subtotal_retail": 0.0,
                }
            cat = categories[cat_id]
            cost_val = (product.cost or 0.0) * product.inventory_count
            retail_val = (product.price or 0.0) * product.inventory_count
            cat["products"].append({
                "product": product,
                "cost_value": cost_val,
                "retail_value": retail_val,
            })
            cat["subtotal_qty"] += product.inventory_count
            cat["subtotal_cost"] += cost_val
            cat["subtotal_retail"] += retail_val
            total_stock += product.inventory_count
            total_cost_value += cost_val
            total_retail_value += retail_val

        # Sort categories by name
        sorted_categories = sorted(categories.values(), key=lambda c: c["name"])

        return {
            "doc_ids": docids,
            "doc_model": "greenlight.product",
            "docs": products,
            "categories": sorted_categories,
            "total_stock": total_stock,
            "total_cost_value": total_cost_value,
            "total_retail_value": total_retail_value,
            "print_date": self.env.cr.now(),
        }
