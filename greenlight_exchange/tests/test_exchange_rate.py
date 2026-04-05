from datetime import date, timedelta
from odoo.tests.common import TransactionCase


class TestExchangeRate(TransactionCase):

    def setUp(self):
        super().setUp()
        self.pair = self.env["greenlight.currency.pair"].create({
            "base_currency": "USD",
            "quote_currency": "GBP",
        })

    def test_pair_name_computed(self):
        self.assertEqual(self.pair.name, "USD/GBP")

    def test_create_rate(self):
        rate = self.env["greenlight.exchange.rate"].create({
            "pair_id": self.pair.id,
            "rate_date": date.today(),
            "rate": 0.7920,
            "open_rate": 0.7910,
            "high_rate": 0.7950,
            "low_rate": 0.7890,
            "close_rate": 0.7920,
        })
        self.assertEqual(rate.rate, 0.7920)
        self.assertEqual(rate.pair_name, "USD/GBP")

    def test_latest_rate_computation(self):
        self.env["greenlight.exchange.rate"].create({
            "pair_id": self.pair.id,
            "rate_date": date.today() - timedelta(days=1),
            "rate": 0.7900,
        })
        self.env["greenlight.exchange.rate"].create({
            "pair_id": self.pair.id,
            "rate_date": date.today(),
            "rate": 0.7935,
        })
        self.pair.invalidate_recordset()
        self.assertAlmostEqual(self.pair.latest_rate, 0.7935, places=4)

    def test_change_pct_computation(self):
        self.env["greenlight.exchange.rate"].create({
            "pair_id": self.pair.id,
            "rate_date": date.today() - timedelta(days=1),
            "rate": 1.0000,
        })
        rate2 = self.env["greenlight.exchange.rate"].create({
            "pair_id": self.pair.id,
            "rate_date": date.today(),
            "rate": 1.0150,
        })
        self.assertAlmostEqual(rate2.change_pct, 1.5, places=1)

    def test_unique_pair_constraint(self):
        with self.assertRaises(Exception):
            self.env["greenlight.currency.pair"].create({
                "base_currency": "USD",
                "quote_currency": "GBP",
            })

    def test_unique_rate_date_constraint(self):
        self.env["greenlight.exchange.rate"].create({
            "pair_id": self.pair.id,
            "rate_date": date.today(),
            "rate": 0.7920,
        })
        with self.assertRaises(Exception):
            self.env["greenlight.exchange.rate"].create({
                "pair_id": self.pair.id,
                "rate_date": date.today(),
                "rate": 0.7930,
            })

    def test_generate_dummy_rates(self):
        count = self.env["greenlight.exchange.rate"].generate_dummy_rates(days=5)
        self.assertGreater(count, 0)
        rates = self.env["greenlight.exchange.rate"].search([("pair_id", "=", self.pair.id)])
        self.assertEqual(len(rates), 6)  # 5 days back + today
