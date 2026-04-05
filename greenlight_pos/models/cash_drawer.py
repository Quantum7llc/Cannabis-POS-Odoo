from odoo import models, fields, api


class GreenLightCashDrawer(models.Model):
    _name = "greenlight.cash.drawer"
    _description = "Cash Drawer Session"
    _order = "opened_at desc"

    name = fields.Char(compute="_compute_name", store=True)
    employee_id = fields.Many2one("greenlight.employee", required=True)
    opened_at = fields.Datetime(required=True, default=fields.Datetime.now)
    closed_at = fields.Datetime()
    opening_balance = fields.Monetary(currency_field="currency_id", required=True)
    closing_balance = fields.Monetary(currency_field="currency_id")
    expected_balance = fields.Monetary(currency_field="currency_id", compute="_compute_expected")
    variance = fields.Monetary(currency_field="currency_id", compute="_compute_variance")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)

    state = fields.Selection(
        [("open", "Open"), ("closed", "Closed")],
        default="open",
    )

    event_ids = fields.One2many("greenlight.cash.drawer.event", "drawer_id")
    notes = fields.Text("Closing Notes")

    @api.depends("employee_id", "opened_at")
    def _compute_name(self):
        for rec in self:
            emp = rec.employee_id.name or "Unknown"
            dt = rec.opened_at.strftime("%Y-%m-%d %H:%M") if rec.opened_at else ""
            rec.name = f"{emp} - {dt}"

    @api.depends("opening_balance", "event_ids.amount")
    def _compute_expected(self):
        for rec in self:
            rec.expected_balance = rec.opening_balance + sum(rec.event_ids.mapped("amount"))

    @api.depends("closing_balance", "expected_balance")
    def _compute_variance(self):
        for rec in self:
            if rec.closing_balance:
                rec.variance = rec.closing_balance - rec.expected_balance
            else:
                rec.variance = 0.0


class GreenLightCashDrawerEvent(models.Model):
    _name = "greenlight.cash.drawer.event"
    _description = "Cash Drawer Event"
    _order = "create_date"

    drawer_id = fields.Many2one("greenlight.cash.drawer", required=True, ondelete="cascade")
    event_type = fields.Selection(
        [
            ("sale", "Sale"),
            ("refund", "Refund"),
            ("drop", "Cash Drop"),
            ("payout", "Payout"),
            ("adjustment", "Adjustment"),
        ],
        required=True,
    )
    amount = fields.Monetary(currency_field="currency_id")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)
    note = fields.Char()
    transaction_id = fields.Many2one("greenlight.transaction")
