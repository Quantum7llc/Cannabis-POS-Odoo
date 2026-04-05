from odoo import models, fields, api, tools


class GreenLightSalesReport(models.Model):
    """Read-only SQL view for sales analytics.

    Provides daily aggregated sales data from confirmed transactions
    suitable for Odoo graph, pivot, and list views.
    """

    _name = "greenlight.sales.report"
    _description = "Sales Analytics Report"
    _auto = False
    _order = "date_day desc"
    _rec_name = "date_day"

    date_day = fields.Date("Date", readonly=True)
    date_month = fields.Char("Month", readonly=True)
    date_year = fields.Char("Year", readonly=True)
    day_of_week = fields.Char("Day of Week", readonly=True)

    employee_id = fields.Many2one("greenlight.employee", "Employee", readonly=True)
    customer_id = fields.Many2one("greenlight.customer", "Customer", readonly=True)
    product_id = fields.Many2one("greenlight.product", "Product", readonly=True)
    category_id = fields.Many2one("greenlight.product.category", "Category", readonly=True)
    cannabis_type = fields.Selection(
        [
            ("flower", "Flower"),
            ("concentrate", "Concentrate"),
            ("infused", "Infused/Edible"),
            ("accessory", "Accessory"),
        ],
        readonly=True,
    )
    payment_method = fields.Selection(
        [("cash", "Cash"), ("debit", "Debit"), ("card", "Card")],
        readonly=True,
    )

    # Measures
    revenue = fields.Monetary("Revenue", currency_field="currency_id", readonly=True)
    tax_collected = fields.Monetary("Tax Collected", currency_field="currency_id", readonly=True)
    cogs = fields.Monetary("COGS", currency_field="currency_id", readonly=True)
    gross_margin = fields.Monetary("Gross Margin", currency_field="currency_id", readonly=True)
    quantity_sold = fields.Integer("Qty Sold", readonly=True)
    transaction_count = fields.Integer("# Transactions", readonly=True)
    avg_ticket = fields.Monetary("Avg Ticket", currency_field="currency_id", readonly=True)
    currency_id = fields.Many2one("res.currency", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                SELECT
                    row_number() OVER () AS id,
                    tl.create_date::date AS date_day,
                    to_char(tl.create_date, 'YYYY-MM') AS date_month,
                    to_char(tl.create_date, 'YYYY') AS date_year,
                    to_char(tl.create_date, 'Dy') AS day_of_week,
                    t.employee_id,
                    t.customer_id,
                    tl.product_id,
                    p.category_id,
                    p.cannabis_type,
                    t.payment_method,
                    SUM(tl.subtotal) AS revenue,
                    SUM(tl.tax) AS tax_collected,
                    SUM(tl.cogs) AS cogs,
                    SUM(tl.subtotal) - SUM(tl.cogs) AS gross_margin,
                    SUM(tl.quantity) AS quantity_sold,
                    COUNT(DISTINCT t.id) AS transaction_count,
                    CASE
                        WHEN COUNT(DISTINCT t.id) > 0
                        THEN SUM(tl.subtotal) / COUNT(DISTINCT t.id)
                        ELSE 0
                    END AS avg_ticket,
                    t.currency_id
                FROM greenlight_transaction_line tl
                JOIN greenlight_transaction t ON t.id = tl.transaction_id
                JOIN greenlight_product p ON p.id = tl.product_id
                WHERE t.state = 'confirmed'
                GROUP BY
                    tl.create_date::date,
                    to_char(tl.create_date, 'YYYY-MM'),
                    to_char(tl.create_date, 'YYYY'),
                    to_char(tl.create_date, 'Dy'),
                    t.employee_id,
                    t.customer_id,
                    tl.product_id,
                    p.category_id,
                    p.cannabis_type,
                    t.payment_method,
                    t.currency_id
            )
        """ % self._table)


class GreenLightProductPerformance(models.Model):
    """Read-only SQL view for product performance analytics."""

    _name = "greenlight.product.performance"
    _description = "Product Performance Report"
    _auto = False
    _order = "total_revenue desc"
    _rec_name = "product_id"

    product_id = fields.Many2one("greenlight.product", "Product", readonly=True)
    category_id = fields.Many2one("greenlight.product.category", "Category", readonly=True)
    cannabis_type = fields.Selection(
        [
            ("flower", "Flower"),
            ("concentrate", "Concentrate"),
            ("infused", "Infused/Edible"),
            ("accessory", "Accessory"),
        ],
        readonly=True,
    )
    total_revenue = fields.Monetary("Total Revenue", currency_field="currency_id", readonly=True)
    total_cogs = fields.Monetary("Total COGS", currency_field="currency_id", readonly=True)
    gross_margin = fields.Monetary("Gross Margin", currency_field="currency_id", readonly=True)
    margin_pct = fields.Float("Margin %", readonly=True, digits=(5, 2))
    total_qty_sold = fields.Integer("Total Qty Sold", readonly=True)
    transaction_count = fields.Integer("# Transactions", readonly=True)
    avg_unit_price = fields.Monetary("Avg Unit Price", currency_field="currency_id", readonly=True)
    current_stock = fields.Integer("Current Stock", readonly=True)
    currency_id = fields.Many2one("res.currency", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                SELECT
                    row_number() OVER () AS id,
                    tl.product_id,
                    p.category_id,
                    p.cannabis_type,
                    SUM(tl.subtotal) AS total_revenue,
                    SUM(tl.cogs) AS total_cogs,
                    SUM(tl.subtotal) - SUM(tl.cogs) AS gross_margin,
                    CASE
                        WHEN SUM(tl.subtotal) > 0
                        THEN ((SUM(tl.subtotal) - SUM(tl.cogs)) / SUM(tl.subtotal)) * 100
                        ELSE 0
                    END AS margin_pct,
                    SUM(tl.quantity)::int AS total_qty_sold,
                    COUNT(DISTINCT tl.transaction_id) AS transaction_count,
                    CASE
                        WHEN SUM(tl.quantity) > 0
                        THEN SUM(tl.subtotal) / SUM(tl.quantity)
                        ELSE 0
                    END AS avg_unit_price,
                    p.inventory_count AS current_stock,
                    (SELECT id FROM res_currency
                     WHERE id = (SELECT currency_id FROM res_company LIMIT 1)) AS currency_id
                FROM greenlight_transaction_line tl
                JOIN greenlight_transaction t ON t.id = tl.transaction_id
                JOIN greenlight_product p ON p.id = tl.product_id
                WHERE t.state = 'confirmed'
                GROUP BY tl.product_id, p.category_id, p.cannabis_type,
                         p.inventory_count
            )
        """ % self._table)


class GreenLightEmployeePerformance(models.Model):
    """Read-only SQL view for employee performance analytics."""

    _name = "greenlight.employee.performance"
    _description = "Employee Performance Report"
    _auto = False
    _order = "total_revenue desc"
    _rec_name = "employee_id"

    employee_id = fields.Many2one("greenlight.employee", "Employee", readonly=True)
    total_revenue = fields.Monetary("Total Revenue", currency_field="currency_id", readonly=True)
    total_tax = fields.Monetary("Total Tax", currency_field="currency_id", readonly=True)
    total_cogs = fields.Monetary("Total COGS", currency_field="currency_id", readonly=True)
    gross_margin = fields.Monetary("Gross Margin", currency_field="currency_id", readonly=True)
    transaction_count = fields.Integer("# Transactions", readonly=True)
    avg_ticket = fields.Monetary("Avg Ticket", currency_field="currency_id", readonly=True)
    items_sold = fields.Integer("Items Sold", readonly=True)
    unique_customers = fields.Integer("Unique Customers", readonly=True)
    currency_id = fields.Many2one("res.currency", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                SELECT
                    row_number() OVER () AS id,
                    t.employee_id,
                    SUM(t.total - t.tax_amount) AS total_revenue,
                    SUM(t.tax_amount) AS total_tax,
                    SUM(t.cogs_total) AS total_cogs,
                    SUM(t.total - t.tax_amount) - SUM(t.cogs_total) AS gross_margin,
                    COUNT(t.id) AS transaction_count,
                    CASE
                        WHEN COUNT(t.id) > 0
                        THEN SUM(t.total) / COUNT(t.id)
                        ELSE 0
                    END AS avg_ticket,
                    SUM(
                        (SELECT COALESCE(SUM(tl.quantity), 0)
                         FROM greenlight_transaction_line tl
                         WHERE tl.transaction_id = t.id)
                    )::int AS items_sold,
                    COUNT(DISTINCT t.customer_id) AS unique_customers,
                    t.currency_id
                FROM greenlight_transaction t
                WHERE t.state = 'confirmed'
                GROUP BY t.employee_id, t.currency_id
            )
        """ % self._table)


class GreenLightCustomerAnalytics(models.Model):
    """Read-only SQL view for customer analytics."""

    _name = "greenlight.customer.analytics"
    _description = "Customer Analytics Report"
    _auto = False
    _order = "lifetime_spend desc"
    _rec_name = "customer_id"

    customer_id = fields.Many2one("greenlight.customer", "Customer", readonly=True)
    lifetime_spend = fields.Monetary("Lifetime Spend", currency_field="currency_id", readonly=True)
    visit_count = fields.Integer("Visit Count", readonly=True)
    avg_ticket = fields.Monetary("Avg Ticket", currency_field="currency_id", readonly=True)
    first_visit = fields.Date("First Visit", readonly=True)
    last_visit = fields.Date("Last Visit", readonly=True)
    days_since_last = fields.Integer("Days Since Last Visit", readonly=True)
    loyalty_points = fields.Integer("Loyalty Points", readonly=True)
    currency_id = fields.Many2one("res.currency", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                SELECT
                    row_number() OVER () AS id,
                    t.customer_id,
                    SUM(t.total) AS lifetime_spend,
                    COUNT(t.id) AS visit_count,
                    CASE
                        WHEN COUNT(t.id) > 0
                        THEN SUM(t.total) / COUNT(t.id)
                        ELSE 0
                    END AS avg_ticket,
                    MIN(t.create_date)::date AS first_visit,
                    MAX(t.create_date)::date AS last_visit,
                    EXTRACT(DAY FROM (NOW() - MAX(t.create_date)))::int AS days_since_last,
                    c.loyalty_points,
                    t.currency_id
                FROM greenlight_transaction t
                JOIN greenlight_customer c ON c.id = t.customer_id
                WHERE t.state = 'confirmed'
                GROUP BY t.customer_id, c.loyalty_points, t.currency_id
            )
        """ % self._table)


class GreenLightCogsReport(models.Model):
    """Read-only SQL view for 280E COGS compliance reporting.

    Section 280E of the Internal Revenue Code restricts cannabis businesses
    from deducting ordinary business expenses. Only COGS is deductible.
    This report provides the detailed COGS breakdown needed for tax compliance.
    """

    _name = "greenlight.cogs.report"
    _description = "280E COGS Report"
    _auto = False
    _order = "date_month desc, category_id"
    _rec_name = "date_month"

    date_month = fields.Char("Month", readonly=True)
    category_id = fields.Many2one("greenlight.product.category", "Category", readonly=True)
    cannabis_type = fields.Selection(
        [
            ("flower", "Flower"),
            ("concentrate", "Concentrate"),
            ("infused", "Infused/Edible"),
            ("accessory", "Accessory"),
        ],
        readonly=True,
    )
    total_revenue = fields.Monetary("Revenue", currency_field="currency_id", readonly=True)
    total_cogs = fields.Monetary("COGS", currency_field="currency_id", readonly=True)
    total_tax = fields.Monetary("Tax Collected", currency_field="currency_id", readonly=True)
    gross_profit = fields.Monetary("Gross Profit", currency_field="currency_id", readonly=True)
    margin_pct = fields.Float("Margin %", readonly=True, digits=(5, 2))
    units_sold = fields.Integer("Units Sold", readonly=True)
    currency_id = fields.Many2one("res.currency", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                SELECT
                    row_number() OVER () AS id,
                    to_char(t.create_date, 'YYYY-MM') AS date_month,
                    p.category_id,
                    p.cannabis_type,
                    SUM(tl.subtotal) AS total_revenue,
                    SUM(tl.cogs) AS total_cogs,
                    SUM(tl.tax) AS total_tax,
                    SUM(tl.subtotal) - SUM(tl.cogs) AS gross_profit,
                    CASE
                        WHEN SUM(tl.subtotal) > 0
                        THEN ((SUM(tl.subtotal) - SUM(tl.cogs)) / SUM(tl.subtotal)) * 100
                        ELSE 0
                    END AS margin_pct,
                    SUM(tl.quantity)::int AS units_sold,
                    t.currency_id
                FROM greenlight_transaction_line tl
                JOIN greenlight_transaction t ON t.id = tl.transaction_id
                JOIN greenlight_product p ON p.id = tl.product_id
                WHERE t.state = 'confirmed'
                GROUP BY
                    to_char(t.create_date, 'YYYY-MM'),
                    p.category_id,
                    p.cannabis_type,
                    t.currency_id
            )
        """ % self._table)


class GreenLightInventoryAlert(models.Model):
    """Read-only SQL view for inventory alerts: low stock, dead stock, reorder."""

    _name = "greenlight.inventory.alert"
    _description = "Inventory Alerts"
    _auto = False
    _order = "alert_type, inventory_count"
    _rec_name = "product_id"

    product_id = fields.Many2one("greenlight.product", "Product", readonly=True)
    category_id = fields.Many2one("greenlight.product.category", "Category", readonly=True)
    inventory_count = fields.Integer("Current Stock", readonly=True)
    last_sold_date = fields.Date("Last Sold", readonly=True)
    days_since_sold = fields.Integer("Days Since Sold", readonly=True)
    total_sold_30d = fields.Integer("Sold (30 days)", readonly=True)
    daily_avg_sold = fields.Float("Daily Avg Sold", readonly=True, digits=(10, 2))
    days_of_stock = fields.Float("Days of Stock Left", readonly=True, digits=(10, 1))
    alert_type = fields.Selection(
        [
            ("low_stock", "Low Stock"),
            ("dead_stock", "Dead Stock (30+ days)"),
            ("out_of_stock", "Out of Stock"),
        ],
        readonly=True,
    )

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                WITH product_sales AS (
                    SELECT
                        tl.product_id,
                        MAX(t.create_date)::date AS last_sold_date,
                        SUM(CASE
                            WHEN t.create_date >= NOW() - INTERVAL '30 days'
                            THEN tl.quantity ELSE 0
                        END)::int AS total_sold_30d
                    FROM greenlight_transaction_line tl
                    JOIN greenlight_transaction t ON t.id = tl.transaction_id
                    WHERE t.state = 'confirmed'
                    GROUP BY tl.product_id
                )
                SELECT
                    row_number() OVER () AS id,
                    p.id AS product_id,
                    p.category_id,
                    p.inventory_count,
                    ps.last_sold_date,
                    COALESCE(
                        EXTRACT(DAY FROM (NOW() - ps.last_sold_date::timestamp))::int,
                        9999
                    ) AS days_since_sold,
                    COALESCE(ps.total_sold_30d, 0) AS total_sold_30d,
                    COALESCE(ps.total_sold_30d::float / 30, 0) AS daily_avg_sold,
                    CASE
                        WHEN COALESCE(ps.total_sold_30d, 0) > 0
                        THEN p.inventory_count::float / (ps.total_sold_30d::float / 30)
                        ELSE 9999
                    END AS days_of_stock,
                    CASE
                        WHEN p.inventory_count <= 0 THEN 'out_of_stock'
                        WHEN ps.last_sold_date IS NULL
                             OR ps.last_sold_date < (NOW() - INTERVAL '30 days')::date
                        THEN 'dead_stock'
                        WHEN p.inventory_count <= 5 THEN 'low_stock'
                    END AS alert_type
                FROM greenlight_product p
                LEFT JOIN product_sales ps ON ps.product_id = p.id
                WHERE p.is_active = True
                  AND (
                      p.inventory_count <= 5
                      OR ps.last_sold_date IS NULL
                      OR ps.last_sold_date < (NOW() - INTERVAL '30 days')::date
                  )
            )
        """ % self._table)
