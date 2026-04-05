from odoo import api, models
from collections import Counter


class DailySalesReport(models.AbstractModel):
    """Custom report model for end-of-day sales summary.

    Computes top-5 products from the day's confirmed transactions.
    """
    _name = "report.greenlight_pos.report_daily_sales_document"
    _description = "Daily Sales Report Data"

    @api.model
    def _get_report_values(self, docids, data=None):
        closing_reports = self.env["greenlight.closing.report"].browse(docids)
        results = []
        for report in closing_reports:
            top_products = self._get_top_products(report)
            results.append({
                "report": report,
                "top_products": top_products,
            })
        return {
            "doc_ids": docids,
            "doc_model": "greenlight.closing.report",
            "docs": closing_reports,
            "results": results,
        }

    def _get_top_products(self, closing_report):
        """Find the top 5 best-selling products for the report date."""
        from datetime import timedelta
        day_start = closing_report.report_date
        day_end = day_start + timedelta(days=1)

        transactions = self.env["greenlight.transaction"].search([
            ("state", "=", "confirmed"),
            ("create_date", ">=", day_start),
            ("create_date", "<", day_end),
        ])

        product_counter = Counter()
        product_revenue = Counter()
        product_names = {}
        for txn in transactions:
            for line in txn.line_ids:
                pid = line.product_id.id
                product_counter[pid] += line.quantity
                product_revenue[pid] += line.subtotal
                product_names[pid] = line.product_id.name

        top_5 = product_counter.most_common(5)
        return [
            {
                "name": product_names[pid],
                "quantity": qty,
                "revenue": product_revenue[pid],
            }
            for pid, qty in top_5
        ]
