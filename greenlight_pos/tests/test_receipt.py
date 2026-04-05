from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestGreenLightReceipt(TransactionCase):
    """Test receipt creation, void, and refund processing."""

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

        self.customer = self.env.ref("greenlight_pos.demo_customer_james", raise_if_not_found=False)
        if not self.customer:
            self.customer = self.env["greenlight.customer"].create({
                "first_name": "Test",
                "last_name": "Customer",
                "dob": "1985-01-01",
                "id_number": "MSTEST002",
                "id_state": "MS",
                "id_expiry": "2030-01-01",
                "email": "test@example.com",
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
                "weight_grams": 3.5,
                "inventory_count": 100,
            })

    def _create_confirmed_transaction(self, qty=2):
        """Create and confirm a transaction, then return it."""
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
        txn.action_confirm()
        return txn

    def _create_receipt(self, txn):
        """Create a receipt for a confirmed transaction."""
        return self.env["greenlight.receipt"].create({
            "transaction_id": txn.id,
        })

    def test_receipt_created_with_number(self):
        txn = self._create_confirmed_transaction()
        receipt = self._create_receipt(txn)
        self.assertTrue(receipt.receipt_number)
        self.assertEqual(receipt.state, "active")

    def test_receipt_snapshots_amounts(self):
        txn = self._create_confirmed_transaction(qty=2)
        receipt = self._create_receipt(txn)
        self.assertAlmostEqual(receipt.subtotal, txn.subtotal, places=2)
        self.assertAlmostEqual(receipt.tax_amount, txn.tax_amount, places=2)
        self.assertAlmostEqual(receipt.total, txn.total, places=2)

    def test_receipt_snapshots_dispensary_info(self):
        settings = self.env["greenlight.settings"].get_active_settings()
        txn = self._create_confirmed_transaction()
        receipt = self._create_receipt(txn)
        self.assertEqual(receipt.dispensary_name, settings.dispensary_name or "")

    def test_receipt_customer_linked(self):
        txn = self._create_confirmed_transaction()
        receipt = self._create_receipt(txn)
        self.assertEqual(receipt.customer_id.id, self.customer.id)

    def test_void_receipt_not_active_rejected(self):
        """Cannot void a receipt that is already voided."""
        txn = self._create_confirmed_transaction()
        receipt = self._create_receipt(txn)
        # Directly set state to voided for testing the guard
        receipt.write({"state": "voided"})
        with self.assertRaises(UserError):
            receipt.action_void()

    def test_refund_draft_creation(self):
        txn = self._create_confirmed_transaction(qty=3)
        receipt = self._create_receipt(txn)
        refund = self.env["greenlight.refund"].create({
            "receipt_id": receipt.id,
            "transaction_id": txn.id,
            "reason": "Customer unsatisfied",
            "line_ids": [(0, 0, {
                "product_id": self.product.id,
                "quantity": 1,
                "unit_price": self.product.price,
            })],
        })
        self.assertEqual(refund.state, "draft")
        self.assertTrue(refund.refund_number)
        self.assertAlmostEqual(refund.refund_total, self.product.price, places=2)

    def test_refund_cancel(self):
        txn = self._create_confirmed_transaction()
        receipt = self._create_receipt(txn)
        refund = self.env["greenlight.refund"].create({
            "receipt_id": receipt.id,
            "transaction_id": txn.id,
            "reason": "Changed mind",
            "line_ids": [(0, 0, {
                "product_id": self.product.id,
                "quantity": 1,
                "unit_price": self.product.price,
            })],
        })
        refund.action_cancel()
        self.assertEqual(refund.state, "cancelled")

    def test_refund_cancel_only_draft(self):
        txn = self._create_confirmed_transaction()
        receipt = self._create_receipt(txn)
        refund = self.env["greenlight.refund"].create({
            "receipt_id": receipt.id,
            "transaction_id": txn.id,
            "reason": "Test",
            "line_ids": [(0, 0, {
                "product_id": self.product.id,
                "quantity": 1,
                "unit_price": self.product.price,
            })],
        })
        refund.action_cancel()
        with self.assertRaises(UserError):
            refund.action_cancel()

    def test_refund_count_on_receipt(self):
        txn = self._create_confirmed_transaction(qty=3)
        receipt = self._create_receipt(txn)
        self.assertEqual(receipt.refund_count, 0)
        self.env["greenlight.refund"].create({
            "receipt_id": receipt.id,
            "transaction_id": txn.id,
            "reason": "Refund 1",
            "line_ids": [(0, 0, {
                "product_id": self.product.id,
                "quantity": 1,
                "unit_price": self.product.price,
            })],
        })
        receipt.invalidate_recordset()
        self.assertEqual(receipt.refund_count, 1)

    def test_refund_total_on_receipt_computed(self):
        """Total refunded on receipt only includes processed refunds."""
        txn = self._create_confirmed_transaction(qty=5)
        receipt = self._create_receipt(txn)
        self.env["greenlight.refund"].create({
            "receipt_id": receipt.id,
            "transaction_id": txn.id,
            "reason": "Draft refund - not processed",
            "line_ids": [(0, 0, {
                "product_id": self.product.id,
                "quantity": 1,
                "unit_price": 45.00,
            })],
        })
        receipt.invalidate_recordset()
        # Draft refund should not count toward total_refunded
        self.assertAlmostEqual(receipt.total_refunded, 0.0, places=2)

    def test_create_refund_on_voided_receipt_rejected(self):
        txn = self._create_confirmed_transaction()
        receipt = self._create_receipt(txn)
        receipt.write({"state": "voided"})
        # The action_create_refund should raise for voided receipts
        with self.assertRaises(UserError):
            receipt.action_create_refund()
