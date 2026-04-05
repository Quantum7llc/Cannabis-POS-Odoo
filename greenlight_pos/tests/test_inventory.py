from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestGreenLightInventoryAdjustment(TransactionCase):
    """Test inventory adjustment creation and stock changes."""

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

        self.product = self.env.ref("greenlight_pos.demo_product_og_kush", raise_if_not_found=False)
        if not self.product:
            categ = self.env["greenlight.product.category"].search([("name", "=", "Flower")], limit=1)
            if not categ:
                categ = self.env["greenlight.product.category"].create({"name": "Flower"})
            self.product = self.env["greenlight.product"].create({
                "name": "OG Kush - 3.5g",
                "sku": "FLW-OGK-35",
                "category_id": categ.id,
                "price": 45.00,
                "cost": 22.00,
                "inventory_count": 100,
            })

        self.reason = self.env.ref("greenlight_pos.demo_reason_damaged", raise_if_not_found=False)
        if not self.reason:
            self.reason = self.env["greenlight.reason.code"].create({
                "name": "Damaged",
                "code_type": "adjustment",
            })

    def test_positive_adjustment_adds_stock(self):
        initial = self.product.inventory_count
        adj = self.env["greenlight.inventory.adjustment"].create({
            "product_id": self.product.id,
            "quantity": 10,
            "reason_code_id": self.reason.id,
            "employee_id": self.employee.id,
            "notes": "Received extra units",
        })
        self.product.invalidate_recordset(["inventory_count"])
        self.assertEqual(self.product.inventory_count, initial + 10)
        self.assertEqual(adj.stock_before, initial)
        self.assertEqual(adj.stock_after, initial + 10)

    def test_negative_adjustment_removes_stock(self):
        initial = self.product.inventory_count
        adj = self.env["greenlight.inventory.adjustment"].create({
            "product_id": self.product.id,
            "quantity": -5,
            "reason_code_id": self.reason.id,
            "employee_id": self.employee.id,
            "notes": "Damaged goods removed",
        })
        self.product.invalidate_recordset(["inventory_count"])
        self.assertEqual(self.product.inventory_count, initial - 5)
        self.assertEqual(adj.stock_before, initial)
        self.assertEqual(adj.stock_after, initial - 5)

    def test_zero_adjustment_rejected(self):
        with self.assertRaises(UserError):
            self.env["greenlight.inventory.adjustment"].create({
                "product_id": self.product.id,
                "quantity": 0,
                "reason_code_id": self.reason.id,
                "employee_id": self.employee.id,
            })

    def test_adjustment_gets_sequence_name(self):
        adj = self.env["greenlight.inventory.adjustment"].create({
            "product_id": self.product.id,
            "quantity": 1,
            "reason_code_id": self.reason.id,
            "employee_id": self.employee.id,
        })
        self.assertTrue(adj.name and adj.name != "New")


class TestGreenLightInventoryCount(TransactionCase):
    """Test inventory count workflow: draft -> in_progress -> completed."""

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

        # Ensure at least one active product exists for the count
        self.product = self.env.ref("greenlight_pos.demo_product_og_kush", raise_if_not_found=False)
        if not self.product:
            categ = self.env["greenlight.product.category"].search([("name", "=", "Flower")], limit=1)
            if not categ:
                categ = self.env["greenlight.product.category"].create({"name": "Flower"})
            self.product = self.env["greenlight.product"].create({
                "name": "OG Kush - 3.5g",
                "sku": "FLW-OGK-35",
                "category_id": categ.id,
                "price": 45.00,
                "cost": 22.00,
                "inventory_count": 100,
                "is_active": True,
            })

    def _create_count(self):
        return self.env["greenlight.inventory.count"].create({
            "employee_id": self.employee.id,
        })

    def test_count_starts_as_draft(self):
        count = self._create_count()
        self.assertEqual(count.state, "draft")
        self.assertTrue(count.name and count.name != "New")

    def test_start_populates_items(self):
        count = self._create_count()
        count.action_start()
        self.assertEqual(count.state, "in_progress")
        self.assertGreater(len(count.item_ids), 0)
        # All items should have counted_qty=0 and expected_qty matching product inventory
        for item in count.item_ids:
            self.assertEqual(item.counted_qty, 0)
            self.assertGreaterEqual(item.expected_qty, 0)

    def test_start_only_from_draft(self):
        count = self._create_count()
        count.action_start()
        with self.assertRaises(UserError):
            count.action_start()

    def test_complete_applies_discrepancies(self):
        count = self._create_count()
        count.action_start()

        # Find the item for our test product
        item = count.item_ids.filtered(lambda i: i.product_id.id == self.product.id)
        self.assertTrue(item)
        initial_stock = self.product.inventory_count
        # Simulate counting 5 more than expected
        item.write({"counted_qty": initial_stock + 5})

        count.action_complete()
        self.assertEqual(count.state, "completed")
        self.assertTrue(count.completed_at)

        self.product.invalidate_recordset(["inventory_count"])
        self.assertEqual(self.product.inventory_count, initial_stock + 5)

    def test_complete_only_from_in_progress(self):
        count = self._create_count()
        with self.assertRaises(UserError):
            count.action_complete()

    def test_discrepancy_computation(self):
        count = self._create_count()
        count.action_start()
        item = count.item_ids[0]
        item.write({"counted_qty": item.expected_qty + 3})
        self.assertEqual(item.discrepancy, 3)

    def test_reset_to_draft(self):
        count = self._create_count()
        count.action_start()
        count.action_reset_to_draft()
        self.assertEqual(count.state, "draft")
        self.assertEqual(len(count.item_ids), 0)

    def test_completed_count_cannot_reset(self):
        count = self._create_count()
        count.action_start()
        # Set counted = expected so no stock changes
        for item in count.item_ids:
            item.write({"counted_qty": item.expected_qty})
        count.action_complete()
        with self.assertRaises(UserError):
            count.action_reset_to_draft()


class TestGreenLightPurchaseOrder(TransactionCase):
    """Test purchase order workflow and inventory receive."""

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

        self.product = self.env.ref("greenlight_pos.demo_product_blue_dream", raise_if_not_found=False)
        if not self.product:
            categ = self.env["greenlight.product.category"].search([("name", "=", "Flower")], limit=1)
            if not categ:
                categ = self.env["greenlight.product.category"].create({"name": "Flower"})
            self.product = self.env["greenlight.product"].create({
                "name": "Blue Dream - 3.5g",
                "sku": "FLW-BLD-35",
                "category_id": categ.id,
                "price": 40.00,
                "cost": 18.00,
                "inventory_count": 150,
            })

    def _create_po(self, qty=20):
        return self.env["greenlight.purchase.order"].create({
            "supplier_name": "Mississippi Cannabis Farms",
            "employee_id": self.employee.id,
            "line_ids": [(0, 0, {
                "product_id": self.product.id,
                "quantity": qty,
                "unit_cost": self.product.cost,
            })],
        })

    def test_po_starts_as_draft(self):
        po = self._create_po()
        self.assertEqual(po.state, "draft")
        self.assertTrue(po.name and po.name != "New")

    def test_po_total_cost_computed(self):
        po = self._create_po(qty=20)
        expected = 20 * self.product.cost
        self.assertAlmostEqual(po.total_cost, expected, places=2)
        self.assertEqual(po.total_items, 20)

    def test_order_workflow(self):
        po = self._create_po()
        po.action_order()
        self.assertEqual(po.state, "ordered")
        self.assertTrue(po.ordered_at)

    def test_order_without_lines_rejected(self):
        po = self.env["greenlight.purchase.order"].create({
            "supplier_name": "Empty Supplier",
            "employee_id": self.employee.id,
        })
        with self.assertRaises(UserError):
            po.action_order()

    def test_receive_increments_inventory(self):
        initial_stock = self.product.inventory_count
        po = self._create_po(qty=25)
        po.action_order()
        po.action_receive()
        self.product.invalidate_recordset(["inventory_count"])
        self.assertEqual(self.product.inventory_count, initial_stock + 25)
        self.assertEqual(po.state, "received")
        self.assertTrue(po.received_at)

    def test_receive_only_from_ordered(self):
        po = self._create_po()
        with self.assertRaises(UserError):
            po.action_receive()

    def test_cancel_draft(self):
        po = self._create_po()
        po.action_cancel()
        self.assertEqual(po.state, "cancelled")

    def test_cancel_ordered(self):
        po = self._create_po()
        po.action_order()
        po.action_cancel()
        self.assertEqual(po.state, "cancelled")

    def test_cancel_received_rejected(self):
        po = self._create_po()
        po.action_order()
        po.action_receive()
        with self.assertRaises(UserError):
            po.action_cancel()
