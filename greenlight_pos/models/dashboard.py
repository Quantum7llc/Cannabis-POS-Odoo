from odoo import models, fields, api
from datetime import datetime, timedelta


class GreenLightDashboard(models.TransientModel):
    _name = "greenlight.dashboard"
    _description = "POS Dashboard"

    # Summary KPIs
    today_sales_total = fields.Monetary(
        "Today's Sales", currency_field="currency_id", readonly=True,
    )
    transaction_count = fields.Integer("Transactions Today", readonly=True)
    avg_ticket = fields.Monetary(
        "Avg Ticket", currency_field="currency_id", readonly=True,
    )
    low_stock_count = fields.Integer("Low Stock Items", readonly=True)
    queue_waiting_count = fields.Integer("Patients Waiting", readonly=True)
    active_promotions_count = fields.Integer("Active Promotions", readonly=True)
    currency_id = fields.Many2one(
        "res.currency", default=lambda self: self.env.company.currency_id,
    )

    # Active shift
    active_shift_employee = fields.Char("On Shift", readonly=True)
    active_shift_start = fields.Datetime("Shift Start", readonly=True)

    # Top products (formatted as text for display)
    top_products_display = fields.Text("Top 5 Products Today", readonly=True)

    # Hourly sales (formatted for display/API consumption)
    hourly_sales_display = fields.Text("Hourly Sales Breakdown", readonly=True)

    @api.model
    def get_dashboard_data(self):
        """Compute and return all dashboard metrics. Used by views and API."""
        today_start = fields.Datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0,
        )
        today_end = today_start + timedelta(days=1)

        # Today's confirmed transactions
        Transaction = self.env["greenlight.transaction"]
        today_txns = Transaction.search([
            ("state", "=", "confirmed"),
            ("create_date", ">=", today_start),
            ("create_date", "<", today_end),
        ])

        today_total = sum(today_txns.mapped("total"))
        txn_count = len(today_txns)
        avg_ticket = today_total / txn_count if txn_count else 0.0

        # Top 5 products
        product_sales = {}
        for txn in today_txns:
            for line in txn.line_ids:
                name = line.product_id.name or "Unknown"
                product_sales[name] = product_sales.get(name, 0) + line.quantity
        top_5 = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:5]
        top_products_text = "\n".join(
            f"{i+1}. {name} ({qty} sold)" for i, (name, qty) in enumerate(top_5)
        ) or "No sales yet today"

        # Hourly sales breakdown
        hourly = {}
        for txn in today_txns:
            hour = txn.create_date.hour
            hourly[hour] = hourly.get(hour, 0.0) + txn.total
        hourly_text = "\n".join(
            f"{h:02d}:00 - ${amt:,.2f}" for h, amt in sorted(hourly.items())
        ) or "No sales yet today"

        # Low stock count (products with <=5 units, active only)
        Product = self.env["greenlight.product"]
        low_stock = Product.search_count([
            ("is_active", "=", True),
            ("inventory_count", "<=", 5),
            ("inventory_count", ">=", 0),
        ])

        # Queue waiting
        Queue = self.env["greenlight.customer.queue"]
        waiting = Queue.search_count([("state", "=", "waiting")])

        # Active promotions
        Promo = self.env["greenlight.promotion"]
        now = fields.Datetime.now()
        active_promos = Promo.search_count([
            ("is_active", "=", True),
            ("start_date", "<=", now),
            ("end_date", ">=", now),
        ])

        # Active shift
        Shift = self.env["greenlight.shift"]
        active_shift = Shift.search([("is_open", "=", True)], limit=1)
        shift_employee = active_shift.employee_id.name if active_shift else "No active shift"
        shift_start = active_shift.clock_in if active_shift else False

        return {
            "today_sales_total": today_total,
            "transaction_count": txn_count,
            "avg_ticket": avg_ticket,
            "low_stock_count": low_stock,
            "queue_waiting_count": waiting,
            "active_promotions_count": active_promos,
            "active_shift_employee": shift_employee,
            "active_shift_start": shift_start,
            "top_products_display": top_products_text,
            "hourly_sales_display": hourly_text,
        }

    @api.model
    def open_dashboard(self):
        """Create a transient record and open the dashboard form."""
        data = self.get_dashboard_data()
        rec = self.create(data)
        return {
            "type": "ir.actions.act_window",
            "name": "Dashboard",
            "res_model": "greenlight.dashboard",
            "view_mode": "form",
            "res_id": rec.id,
            "target": "current",
        }
