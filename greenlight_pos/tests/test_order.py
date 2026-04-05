from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestGreenLightOrder(TransactionCase):
    """Test order status workflow: placed -> in_progress -> ready -> completed."""

    def setUp(self):
        super().setUp()
        self.env["greenlight.settings"].get_active_settings()

        self.employee = self.env.ref("greenlight_pos.demo_admin", raise_if_not_found=False)
        if not self.employee:
            self.employee = self.env["greenlight.employee"].create({
                "name": "Test Admin",
                "pin_hash": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
                "role": "admin",
            })

        self.customer = self.env.ref("greenlight_pos.demo_customer_sarah", raise_if_not_found=False)
        if not self.customer:
            self.customer = self.env["greenlight.customer"].create({
                "first_name": "Test",
                "last_name": "OrderCustomer",
                "dob": "1990-01-01",
                "id_number": "MSTEST003",
                "id_state": "MS",
                "id_expiry": "2030-01-01",
            })

        self.product = self.env.ref("greenlight_pos.demo_product_gummy", raise_if_not_found=False)
        if not self.product:
            categ = self.env["greenlight.product.category"].search([("name", "=", "Gummy")], limit=1)
            if not categ:
                categ = self.env["greenlight.product.category"].create({"name": "Gummy"})
            self.product = self.env["greenlight.product"].create({
                "name": "THC Gummies 10pk",
                "sku": "EDI-GUM-10",
                "category_id": categ.id,
                "price": 35.00,
                "cost": 15.00,
                "inventory_count": 200,
            })

    def _create_order(self, source="in_store", qty=2):
        return self.env["greenlight.order"].create({
            "customer_id": self.customer.id,
            "employee_id": self.employee.id,
            "source": source,
            "line_ids": [(0, 0, {
                "product_id": self.product.id,
                "quantity": qty,
                "unit_price": self.product.price,
            })],
        })

    def test_order_created_as_placed(self):
        order = self._create_order()
        self.assertEqual(order.state, "order_placed")
        self.assertTrue(order.name and order.name != "New")

    def test_order_totals_computed(self):
        order = self._create_order(qty=3)
        tax_rate = self.env["greenlight.settings"].get_tax_rate()
        expected_subtotal = 3 * self.product.price
        expected_total = expected_subtotal * (1 + tax_rate)
        self.assertAlmostEqual(order.subtotal, expected_subtotal, places=2)
        self.assertAlmostEqual(order.total, expected_total, places=2)

    def test_order_line_count(self):
        order = self._create_order()
        self.assertEqual(order.line_count, 1)

    def test_start_workflow(self):
        order = self._create_order()
        order.action_start()
        self.assertEqual(order.state, "in_progress")

    def test_start_only_from_placed(self):
        order = self._create_order()
        order.action_start()
        with self.assertRaises(UserError):
            order.action_start()

    def test_ready_workflow(self):
        order = self._create_order()
        order.action_start()
        order.action_ready()
        self.assertEqual(order.state, "ready_for_pickup")

    def test_ready_only_from_in_progress(self):
        order = self._create_order()
        with self.assertRaises(UserError):
            order.action_ready()

    def test_complete_workflow(self):
        order = self._create_order()
        order.action_start()
        order.action_ready()
        order.action_complete()
        self.assertEqual(order.state, "completed")
        self.assertTrue(order.completed_date)

    def test_complete_only_from_ready(self):
        order = self._create_order()
        order.action_start()
        with self.assertRaises(UserError):
            order.action_complete()

    def test_cancel_from_placed(self):
        order = self._create_order()
        order.action_cancel()
        self.assertEqual(order.state, "cancelled")

    def test_cancel_from_in_progress(self):
        order = self._create_order()
        order.action_start()
        order.action_cancel()
        self.assertEqual(order.state, "cancelled")

    def test_cancel_from_ready(self):
        order = self._create_order()
        order.action_start()
        order.action_ready()
        order.action_cancel()
        self.assertEqual(order.state, "cancelled")

    def test_cancel_completed_rejected(self):
        order = self._create_order()
        order.action_start()
        order.action_ready()
        order.action_complete()
        with self.assertRaises(UserError):
            order.action_cancel()

    def test_cancel_already_cancelled_rejected(self):
        order = self._create_order()
        order.action_cancel()
        with self.assertRaises(UserError):
            order.action_cancel()

    def test_full_workflow_end_to_end(self):
        """Walk through the entire happy path: placed -> started -> ready -> completed."""
        order = self._create_order(source="leafly", qty=1)
        self.assertEqual(order.source, "leafly")
        self.assertEqual(order.state, "order_placed")

        order.action_start()
        self.assertEqual(order.state, "in_progress")

        order.action_ready()
        self.assertEqual(order.state, "ready_for_pickup")

        order.action_complete()
        self.assertEqual(order.state, "completed")
        self.assertTrue(order.completed_date)

    def test_multiple_line_items(self):
        product2 = self.env.ref("greenlight_pos.demo_product_preroll", raise_if_not_found=False)
        if not product2:
            categ = self.env["greenlight.product.category"].search(
                [("name", "=", "Pre-Roll")], limit=1
            )
            if not categ:
                categ = self.env["greenlight.product.category"].create({"name": "Pre-Roll"})
            product2 = self.env["greenlight.product"].create({
                "name": "Pre-Roll 1g",
                "sku": "PRE-TST-10",
                "category_id": categ.id,
                "price": 12.00,
                "cost": 5.00,
                "inventory_count": 300,
            })

        order = self.env["greenlight.order"].create({
            "customer_id": self.customer.id,
            "employee_id": self.employee.id,
            "source": "website",
            "line_ids": [
                (0, 0, {
                    "product_id": self.product.id,
                    "quantity": 2,
                    "unit_price": 35.00,
                }),
                (0, 0, {
                    "product_id": product2.id,
                    "quantity": 3,
                    "unit_price": 12.00,
                }),
            ],
        })
        self.assertEqual(order.line_count, 2)
        expected_subtotal = (2 * 35.00) + (3 * 12.00)
        self.assertAlmostEqual(order.subtotal, expected_subtotal, places=2)
