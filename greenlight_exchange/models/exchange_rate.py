from odoo import models, fields, api
import random
import logging

_logger = logging.getLogger(__name__)

# Realistic base rates for dummy data generation
BASE_RATES = {
    "USD/GBP": 0.79,
    "USD/EUR": 0.92,
    "GBP/EUR": 1.17,
    "USD/JPY": 149.50,
    "USD/CAD": 1.36,
    "GBP/USD": 1.27,
    "EUR/USD": 1.09,
    "USD/CHF": 0.88,
}


class ExchangeRate(models.Model):
    _name = "greenlight.exchange.rate"
    _description = "Exchange Rate Entry"
    _order = "rate_date desc, pair_id"

    pair_id = fields.Many2one(
        "greenlight.currency.pair",
        required=True,
        ondelete="cascade",
        index=True,
    )
    pair_name = fields.Char(related="pair_id.name", store=True, string="Pair")
    rate_date = fields.Date(required=True, default=fields.Date.today, index=True)
    rate = fields.Float("Exchange Rate", required=True, digits=(12, 6))
    open_rate = fields.Float("Open", digits=(12, 6))
    high_rate = fields.Float("High", digits=(12, 6))
    low_rate = fields.Float("Low", digits=(12, 6))
    close_rate = fields.Float("Close", digits=(12, 6))
    change_pct = fields.Float("Change %", compute="_compute_change", digits=(8, 4), store=True)
    source = fields.Selection(
        [
            ("manual", "Manual"),
            ("dummy", "Dummy Data"),
            ("api", "External API"),
        ],
        default="manual",
    )

    _sql_constraints = [
        (
            "pair_date_uniq",
            "unique(pair_id, rate_date)",
            "Only one rate per pair per date.",
        ),
    ]

    @api.depends("rate", "pair_id")
    def _compute_change(self):
        for rec in self:
            # Find previous day's rate
            prev = self.search(
                [
                    ("pair_id", "=", rec.pair_id.id),
                    ("rate_date", "<", rec.rate_date),
                ],
                order="rate_date desc",
                limit=1,
            )
            if prev and prev.rate:
                rec.change_pct = ((rec.rate - prev.rate) / prev.rate) * 100
            else:
                rec.change_pct = 0.0

    @api.model
    def generate_dummy_rates(self, days=90):
        """Generate realistic dummy exchange rate data for all active pairs.

        Called by the wizard or cron job. Uses random walk around base rates
        to simulate realistic market movements.
        """
        from datetime import date, timedelta

        pairs = self.env["greenlight.currency.pair"].search([("is_active", "=", True)])
        today = date.today()
        created = 0

        for pair in pairs:
            pair_key = pair.name
            base_rate = BASE_RATES.get(pair_key, 1.0)
            current_rate = base_rate

            for day_offset in range(days, -1, -1):
                rate_date = today - timedelta(days=day_offset)

                # Skip if rate already exists for this date
                existing = self.search_count([
                    ("pair_id", "=", pair.id),
                    ("rate_date", "=", rate_date),
                ])
                if existing:
                    continue

                # Random walk: daily change between -1.5% and +1.5%
                daily_change = random.uniform(-0.015, 0.015)
                current_rate *= (1 + daily_change)

                # OHLC simulation
                intraday_vol = abs(current_rate * random.uniform(0.001, 0.008))
                open_rate = current_rate * (1 + random.uniform(-0.003, 0.003))
                high_rate = max(open_rate, current_rate) + intraday_vol
                low_rate = min(open_rate, current_rate) - intraday_vol

                self.create({
                    "pair_id": pair.id,
                    "rate_date": rate_date,
                    "rate": round(current_rate, 6),
                    "open_rate": round(open_rate, 6),
                    "high_rate": round(high_rate, 6),
                    "low_rate": round(low_rate, 6),
                    "close_rate": round(current_rate, 6),
                    "source": "dummy",
                })
                created += 1

        _logger.info("Generated %d dummy exchange rate entries for %d pairs", created, len(pairs))
        return created

    @api.model
    def cron_add_daily_rate(self):
        """Cron job: add today's simulated rate for all active pairs."""
        self.generate_dummy_rates(days=0)
