from odoo import models, fields, api
from odoo.exceptions import UserError


class GreenLightShiftEnhanced(models.Model):
    """Enhance shifts with cash reconciliation for end-of-shift closeout."""

    _inherit = "greenlight.shift"

    opening_cash = fields.Monetary(
        "Opening Cash",
        currency_field="currency_id",
        help="Cash in drawer when shift starts.",
    )
    closing_cash = fields.Monetary(
        "Closing Cash",
        currency_field="currency_id",
        help="Actual cash counted at shift close.",
    )
    expected_cash = fields.Monetary(
        "Expected Cash",
        currency_field="currency_id",
        compute="_compute_expected_cash",
        store=True,
        help="Opening cash plus net cash transactions during the shift.",
    )
    cash_variance = fields.Monetary(
        "Cash Variance",
        currency_field="currency_id",
        compute="_compute_cash_variance",
        store=True,
        help="Difference between closing cash and expected cash.",
    )
    is_blind_count = fields.Boolean(
        "Blind Count",
        default=True,
        help="Employee enters closing amount without seeing expected cash.",
    )
    currency_id = fields.Many2one(
        "res.currency",
        default=lambda self: self.env.company.currency_id,
    )
    state = fields.Selection(
        [("open", "Open"), ("closed", "Closed")],
        default="open",
        string="Status",
    )
    cash_transaction_ids = fields.One2many(
        "greenlight.transaction",
        compute="_compute_cash_transactions",
        string="Cash Transactions",
    )
    notes = fields.Text("Closing Notes")

    @api.depends(
        "opening_cash",
        "clock_in",
        "clock_out",
        "employee_id",
    )
    def _compute_expected_cash(self):
        Transaction = self.env["greenlight.transaction"]
        for rec in self:
            if not rec.clock_in or not rec.employee_id:
                rec.expected_cash = rec.opening_cash or 0.0
                continue
            domain = [
                ("employee_id", "=", rec.employee_id.id),
                ("payment_method", "=", "cash"),
                ("state", "=", "confirmed"),
                ("create_date", ">=", rec.clock_in),
            ]
            if rec.clock_out:
                domain.append(("create_date", "<=", rec.clock_out))
            txns = Transaction.search(domain)
            net_cash = sum(txns.mapped("total"))
            rec.expected_cash = (rec.opening_cash or 0.0) + net_cash

    @api.depends("closing_cash", "expected_cash")
    def _compute_cash_variance(self):
        for rec in self:
            if rec.closing_cash and rec.state == "closed":
                rec.cash_variance = rec.closing_cash - rec.expected_cash
            else:
                rec.cash_variance = 0.0

    def _compute_cash_transactions(self):
        Transaction = self.env["greenlight.transaction"]
        for rec in self:
            if not rec.clock_in or not rec.employee_id:
                rec.cash_transaction_ids = Transaction
                continue
            domain = [
                ("employee_id", "=", rec.employee_id.id),
                ("payment_method", "=", "cash"),
                ("state", "=", "confirmed"),
                ("create_date", ">=", rec.clock_in),
            ]
            if rec.clock_out:
                domain.append(("create_date", "<=", rec.clock_out))
            rec.cash_transaction_ids = Transaction.search(domain)

    def action_open_shift(self):
        """Open a shift. Only one active shift per employee allowed."""
        for rec in self:
            existing = self.search([
                ("employee_id", "=", rec.employee_id.id),
                ("state", "=", "open"),
                ("id", "!=", rec.id),
            ], limit=1)
            if existing:
                raise UserError(
                    f"Employee {rec.employee_id.name} already has an open shift "
                    f"(started {existing.clock_in}). Close it before opening a new one."
                )
            rec.state = "open"
            rec.clock_in = rec.clock_in or fields.Datetime.now()
            rec.employee_id.current_shift_id = rec.id

    def action_close_shift(self):
        """Close the shift and compute expected cash from transactions."""
        for rec in self:
            if rec.state == "closed":
                raise UserError("This shift is already closed.")
            rec.clock_out = fields.Datetime.now()
            rec.state = "closed"
            # Trigger recompute of expected_cash now that clock_out is set
            rec._compute_expected_cash()
            rec._compute_cash_variance()
            # Clear employee's current shift
            if rec.employee_id.current_shift_id == rec:
                rec.employee_id.current_shift_id = False
