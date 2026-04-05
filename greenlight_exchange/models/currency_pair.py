from odoo import models, fields, api


class CurrencyPair(models.Model):
    _name = "greenlight.currency.pair"
    _description = "Currency Pair"
    _order = "name"

    name = fields.Char(compute="_compute_name", store=True)
    base_currency = fields.Char("Base Currency", required=True, size=3, help="e.g. USD, GBP, EUR")
    quote_currency = fields.Char("Quote Currency", required=True, size=3)
    is_active = fields.Boolean(default=True)
    rate_ids = fields.One2many("greenlight.exchange.rate", "pair_id", string="Rate History")
    rate_count = fields.Integer(compute="_compute_rate_count")
    latest_rate = fields.Float(compute="_compute_latest_rate", digits=(12, 6))
    latest_date = fields.Date(compute="_compute_latest_rate")

    @api.depends("base_currency", "quote_currency")
    def _compute_name(self):
        for rec in self:
            base = (rec.base_currency or "").upper()
            quote = (rec.quote_currency or "").upper()
            rec.name = f"{base}/{quote}" if base and quote else ""

    @api.depends("rate_ids")
    def _compute_rate_count(self):
        for rec in self:
            rec.rate_count = len(rec.rate_ids)

    @api.depends("rate_ids.rate", "rate_ids.rate_date")
    def _compute_latest_rate(self):
        for rec in self:
            latest = rec.rate_ids.sorted("rate_date", reverse=True)[:1]
            rec.latest_rate = latest.rate if latest else 0.0
            rec.latest_date = latest.rate_date if latest else False
