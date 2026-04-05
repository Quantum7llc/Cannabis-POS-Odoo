from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestGreenLightTransaction(TransactionCase):
    """Test transaction confirm, void, and totals computation."""

    def setUp(self):
        super().setUp()
        # Ensure settings exist (needed for tax_rate in line compute)
        self.env["greenlight.settings"].get_active_settings()

        # Look up demo data or create minimal records
        self.employee = self.env.ref("greenlight_pos.demo_admin", raise_if_not_found=False)
        if not self.employee:
            self.employee = self.env["greenlight.employee"].create({
                "name": "Test Admin",
                "pin_hash": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
                "role": "admin",
            })

        self.customer = self.env.ref("greenlight_pos.demo_customer_james", raise_if_not_found=False)
        if not self.customer:
            self.customer = self.env["greenlight.customer"].create({
                "first_name": "Test",
                "last_name": "Customer",
                "dob": "1985-01-01",
                "id_number": "MSTEST001",
                "id_state": "MS",
                "id_expiry": "2030-01-01",
            })

        self.product = self.env.ref("greenlight_pos.demo_product_og_kush", raise_if_not_found=False)
        if not self.product:
            categ = self.env["greenlight.product.category"].search([("name", "=", "Flower")], limit=1)
            if not categ:
                categ = self.env["greenlight.product.category"].create({"name": "Flower"})
            self.product = self.env["greenlight.product"].create({
                "name": "OG Kush - 3.5g",
                "sku": "FLW-OGK-35",
                "category_id": categ.id,
                "thc_percentage": 22.5,
                "weight_grams": 3.5,
                "price": 45.00,
                "cost": 22.00,
                "inventory_count": 100,
            })

    def _create_transaction(self, qty=2):
        """Helper: create a draft transaction with one line."""
        txn = self.env["greenlight.transaction"].create({
            "customer_id": self.customer.id,
            "employee_id": self.employee.id,
            "payment_method": "cash",
            "line_ids": [(0, 0, {
                "product_id": self.product.id,
                "quantity": qty,
                "unit_price": self.product.price,
            })],
        })
        return txn

    def test_transaction_created_as_draft(self):
        txn = self._create_transaction()
        self.assertEqual(txn.state, "draft")
        self.assertTrue(txn.name and txn.name != "New")

    def test_totals_computed(self):
        txn = self._create_transaction(qty=2)
        tax_rate = self.env["greenlight.settings"].get_tax_rate()
        expected_subtotal = 2 * self.product.price
        expected_tax = expected_subtotal * tax_rate
        self.assertAlmostEqual(txn.subtotal, expected_subtotal, places=2)
        self.assertAlmostEqual(txn.tax_amount, expected_tax, places=2)
        self.assertAlmostEqual(txn.total, expected_subtotal + expected_tax, places=2)

    def test_cogs_computed(self):
        txn = self._create_transaction(qty=3)
        expected_cogs = 3 * self.product.cost
        self.assertAlmostEqual(txn.cogs_total, expected_cogs, places=2)

    def test_confirm_decrements_inventory(self):
        initial_stock = self.product.inventory_count
        txn = self._create_transaction(qty=5)
        txn.action_confirm()
        self.product.invalidate_recordset(["inventory_count"])
        self.assertEqual(self.product.inventory_count, initial_stock - 5)
        self.assertEqual(txn.state, "confirmed")

    def test_confirm_draft_only(self):
        txn = self._create_transaction()
        txn.action_confirm()
        with self.assertRaises(UserError):
            txn.action_confirm()

    def test_void_restores_inventory(self):
        initial_stock = self.product.inventory_count
        txn = self._create_transaction(qty=3)
        txn.action_confirm()
        self.product.invalidate_recordset(["inventory_count"])
        self.assertEqual(self.product.inventory_count, initial_stock - 3)

        txn.action_void()
        self.product.invalidate_recordset(["inventory_count"])
        self.assertEqual(self.product.inventory_count, initial_stock)
        self.assertEqual(txn.state, "voided")

    def test_void_confirmed_only(self):
        txn = self._create_transaction()
        with self.assertRaises(UserError):
            txn.action_void()

    def test_void_already_voided_rejected(self):
        txn = self._create_transaction()
        txn.action_confirm()
        txn.action_void()
        with self.assertRaises(UserError):
            txn.action_void()

    def test_multiple_lines_totals(self):
        product2 = self.env.ref("greenlight_pos.demo_product_gummy", raise_if_not_found=False)
        if not product2:
            categ = self.env["greenlight.product.category"].search([("name", "=", "Gummy")], limit=1)
            if not categ:
                categ = self.env["greenlight.product.category"].create({"name": "Gummy"})
            product2 = self.env["greenlight.product"].create({
                "name": "Gummies",
                "sku": "EDI-GUM-99",
                "category_id": categ.id,
                "price": 35.00,
                "cost": 15.00,
                "inventory_count": 200,
            })

        txn = self.env["greenlight.transaction"].create({
            "customer_id": self.customer.id,
            "employee_id": self.employee.id,
            "payment_method": "debit",
            "line_ids": [
                (0, 0, {
                    "product_id": self.product.id,
                    "quantity": 1,
                    "unit_price": 45.00,
                }),
                (0, 0, {
                    "product_id": product2.id,
                    "quantity": 2,
                    "unit_price": 35.00,
                }),
            ],
        })
        expected_subtotal = 45.00 + 70.00
        self.assertAlmostEqual(txn.subtotal, expected_subtotal, places=2)
        expected_cogs = 22.00 + 30.00
        self.assertAlmostEqual(txn.cogs_total, expected_cogs, places=2)
