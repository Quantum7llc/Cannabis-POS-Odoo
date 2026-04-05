from odoo import api, models
from collections import defaultdict


class Cogs280eReport(models.AbstractModel):
    """Custom report model for IRC Section 280E COGS summary.

    Aggregates gross revenue, COGS, and gross profit by product category,
    with monthly breakdown within each category.
    """
    _name = "report.greenlight_pos.report_cogs_280e_document"
    _description = "280E COGS Report Data"

    @api.model
    def _get_report_values(self, docids, data=None):
        transactions = self.env["greenlight.transaction"].browse(docids)

        # Determine date range from the selected transactions
        all_dates = [t.create_date for t in transactions if t.create_date]
        date_from = min(all_dates) if all_dates else None
        date_to = max(all_dates) if all_dates else None

        # Aggregate by category and month
        # Structure: {category_name: {month_key: {revenue, cogs, ...}}}
        category_data = defaultdict(lambda: defaultdict(lambda: {
            "revenue": 0.0,
            "cogs": 0.0,
            "tax": 0.0,
        }))
        category_totals = defaultdict(lambda: {
            "revenue": 0.0,
            "cogs": 0.0,
            "tax": 0.0,
        })

        for txn in transactions:
            if txn.state != "confirmed":
                continue
            month_key = txn.create_date.strftime("%Y-%m") if txn.create_date else "Unknown"
            for line in txn.line_ids:
                cat_name = line.product_id.category_id.name or "Uncategorized"
                category_data[cat_name][month_key]["revenue"] += line.subtotal
                category_data[cat_name][month_key]["cogs"] += line.cogs
                category_data[cat_name][month_key]["tax"] += line.tax
                category_totals[cat_name]["revenue"] += line.subtotal
                category_totals[cat_name]["cogs"] += line.cogs
                category_totals[cat_name]["tax"] += line.tax

        # Build structured output
        categories = []
        grand_revenue = 0.0
        grand_cogs = 0.0
        grand_tax = 0.0

        for cat_name in sorted(category_data.keys()):
            months = []
            for month_key in sorted(category_data[cat_name].keys()):
                m = category_data[cat_name][month_key]
                gross_profit = m["revenue"] - m["cogs"]
                margin = (gross_profit / m["revenue"] * 100.0) if m["revenue"] else 0.0
                months.append({
                    "month": month_key,
                    "revenue": m["revenue"],
                    "cogs": m["cogs"],
                    "tax": m["tax"],
                    "gross_profit": gross_profit,
                    "margin_pct": margin,
                })

            totals = category_totals[cat_name]
            cat_gross_profit = totals["revenue"] - totals["cogs"]
            cat_margin = (cat_gross_profit / totals["revenue"] * 100.0) if totals["revenue"] else 0.0

            categories.append({
                "name": cat_name,
                "months": months,
                "total_revenue": totals["revenue"],
                "total_cogs": totals["cogs"],
                "total_tax": totals["tax"],
                "total_gross_profit": cat_gross_profit,
                "total_margin_pct": cat_margin,
            })

            grand_revenue += totals["revenue"]
            grand_cogs += totals["cogs"]
            grand_tax += totals["tax"]

        grand_gross_profit = grand_revenue - grand_cogs
        grand_margin = (grand_gross_profit / grand_revenue * 100.0) if grand_revenue else 0.0

        return {
            "doc_ids": docids,
            "doc_model": "greenlight.transaction",
            "docs": transactions,
            "categories": categories,
            "grand_revenue": grand_revenue,
            "grand_cogs": grand_cogs,
            "grand_tax": grand_tax,
            "grand_gross_profit": grand_gross_profit,
            "grand_margin_pct": grand_margin,
            "date_from": date_from,
            "date_to": date_to,
        }
