from odoo import models, fields, api
from odoo.exceptions import UserError


class GreenLightClosingReport(models.Model):
    _name = "greenlight.closing.report"
    _description = "End-of-Day Closing Report"
    _order = "report_date desc"

    name = fields.Char(compute="_compute_name", store=True)
    report_date = fields.Date(required=True, default=fields.Date.today)
    employee_id = fields.Many2one(
        "greenlight.employee",
        string="Closed By",
        required=True,
        ondelete="restrict",
    )
    currency_id = fields.Many2one(
        "res.currency",
        default=lambda self: self.env.company.currency_id,
    )

    # Aggregated totals by payment method
    total_cash = fields.Monetary("Total Cash", currency_field="currency_id")
    total_debit = fields.Monetary("Total Debit", currency_field="currency_id")
    total_card = fields.Monetary("Total Card", currency_field="currency_id")
    gross_sales = fields.Monetary("Gross Sales", currency_field="currency_id")
    tax_collected = fields.Monetary("Tax Collected", currency_field="currency_id")
    net_sales = fields.Monetary(
        "Net Sales",
        currency_field="currency_id",
        compute="_compute_net_sales",
        store=True,
    )

    transaction_count = fields.Integer("Transaction Count")
    void_count = fields.Integer("Voided Transactions")
    refund_total = fields.Monetary("Total Refunds", currency_field="currency_id")

    # Cash reconciliation
    expected_cash = fields.Monetary("Expected Cash", currency_field="currency_id")
    actual_cash = fields.Monetary("Actual Cash Counted", currency_field="currency_id")
    cash_variance = fields.Monetary(
        "Cash Variance",
        currency_field="currency_id",
        compute="_compute_cash_variance",
        store=True,
    )

    notes = fields.Text("Notes")
    state = fields.Selection(
        [("draft", "Draft"), ("confirmed", "Confirmed")],
        default="draft",
    )

    @api.depends("report_date", "employee_id")
    def _compute_name(self):
        for rec in self:
            date_str = rec.report_date.strftime("%Y-%m-%d") if rec.report_date else "?"
            emp = rec.employee_id.name or "Unknown"
            rec.name = f"Close {date_str} - {emp}"

    @api.depends("gross_sales", "tax_collected")
    def _compute_net_sales(self):
        for rec in self:
            rec.net_sales = (rec.gross_sales or 0.0) - (rec.tax_collected or 0.0)

    @api.depends("actual_cash", "expected_cash")
    def _compute_cash_variance(self):
        for rec in self:
            if rec.actual_cash:
                rec.cash_variance = rec.actual_cash - (rec.expected_cash or 0.0)
            else:
                rec.cash_variance = 0.0

    def action_generate(self):
        """Aggregate all transactions for the report date into this report."""
        Transaction = self.env["greenlight.transaction"]
        for rec in self:
            if rec.state == "confirmed":
                raise UserError("Cannot regenerate a confirmed report.")

            day_start = fields.Datetime.to_datetime(rec.report_date)
            from datetime import timedelta
            day_end = day_start + timedelta(days=1)

            # Confirmed transactions for the date
            txns = Transaction.search([
                ("state", "=", "confirmed"),
                ("create_date", ">=", day_start),
                ("create_date", "<", day_end),
            ])
            voided = Transaction.search([
                ("state", "=", "voided"),
                ("create_date", ">=", day_start),
                ("create_date", "<", day_end),
            ])

            cash_txns = txns.filtered(lambda t: t.payment_method == "cash")
            debit_txns = txns.filtered(lambda t: t.payment_method == "debit")
            card_txns = txns.filtered(lambda t: t.payment_method == "card")

            rec.total_cash = sum(cash_txns.mapped("total"))
            rec.total_debit = sum(debit_txns.mapped("total"))
            rec.total_card = sum(card_txns.mapped("total"))
            rec.gross_sales = sum(txns.mapped("subtotal"))
            rec.tax_collected = sum(txns.mapped("tax_amount"))
            rec.transaction_count = len(txns)
            rec.void_count = len(voided)
            rec.expected_cash = rec.total_cash

            # Sum refunds for the day
            Refund = self.env["greenlight.refund"]
            refunds = Refund.search([
                ("state", "=", "confirmed"),
                ("create_date", ">=", day_start),
                ("create_date", "<", day_end),
            ])
            rec.refund_total = sum(refunds.mapped("refund_total"))

    def action_confirm(self):
        for rec in self:
            rec.state = "confirmed"
