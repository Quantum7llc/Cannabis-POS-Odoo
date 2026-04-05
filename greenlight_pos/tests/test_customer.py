from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestGreenLightCustomer(TransactionCase):

    def setUp(self):
        super().setUp()
        self.customer = self.env["greenlight.customer"].create({
            "first_name": "John",
            "last_name": "Doe",
            "dob": "1990-01-15",
            "id_number": "MS12345678",
            "id_state": "MS",
            "id_expiry": "2028-01-15",
        })

    def test_full_name(self):
        self.assertEqual(self.customer.full_name, "John Doe")

    def test_age_computation(self):
        self.assertGreater(self.customer.age, 0)

    def test_id_not_expired(self):
        self.assertFalse(self.customer.id_expired)

    def test_underage_rejected(self):
        with self.assertRaises(ValidationError):
            self.env["greenlight.customer"].create({
                "first_name": "Minor",
                "last_name": "Test",
                "dob": "2015-01-01",
                "id_number": "MS99999999",
                "id_state": "MS",
                "id_expiry": "2030-01-01",
            })

    def test_duplicate_id_rejected(self):
        with self.assertRaises(Exception):
            self.env["greenlight.customer"].create({
                "first_name": "Jane",
                "last_name": "Doe",
                "dob": "1985-06-01",
                "id_number": "MS12345678",  # duplicate
                "id_state": "MS",
                "id_expiry": "2028-01-15",
            })
