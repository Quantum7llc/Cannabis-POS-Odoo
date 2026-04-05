from datetime import timedelta
from odoo import fields
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestGreenLightPromotion(TransactionCase):
    """Test promotion validity, date range, max uses, and constraints."""

    def setUp(self):
        super().setUp()
        self.env["greenlight.settings"].get_active_settings()

        self.categ_concentrate = self.env.ref(
            "greenlight_pos.categ_concentrate", raise_if_not_found=False
        )
        if not self.categ_concentrate:
            self.categ_concentrate = self.env["greenlight.product.category"].search(
                [("name", "=", "Concentrate")], limit=1
            )
            if not self.categ_concentrate:
                self.categ_concentrate = self.env["greenlight.product.category"].create(
                    {"name": "Concentrate"}
                )

        self.product = self.env.ref("greenlight_pos.demo_product_live_resin", raise_if_not_found=False)
        if not self.product:
            self.product = self.env["greenlight.product"].create({
                "name": "Live Resin - 1g",
                "sku": "CON-LVR-10",
                "category_id": self.categ_concentrate.id,
                "price": 65.00,
                "cost": 32.00,
                "inventory_count": 50,
            })

    def _now(self):
        return fields.Datetime.now()

    def _create_promo(self, **overrides):
        vals = {
            "name": "Test Promotion",
            "discount_type": "percentage",
            "discount_value": 10.0,
            "start_date": self._now() - timedelta(days=1),
            "end_date": self._now() + timedelta(days=30),
            "max_uses": 0,
            "display_on_pos": True,
        }
        vals.update(overrides)
        return self.env["greenlight.promotion"].create(vals)

    def test_promo_is_usable(self):
        promo = self._create_promo()
        self.assertTrue(promo.is_active)
        self.assertFalse(promo.is_expired)
        self.assertFalse(promo.is_maxed)
        self.assertTrue(promo.is_usable)

    def test_promo_expired(self):
        promo = self._create_promo(
            start_date=self._now() - timedelta(days=60),
            end_date=self._now() - timedelta(days=1),
        )
        self.assertTrue(promo.is_expired)
        self.assertFalse(promo.is_usable)

    def test_promo_maxed_out(self):
        promo = self._create_promo(max_uses=5, current_uses=5)
        self.assertTrue(promo.is_maxed)
        self.assertFalse(promo.is_usable)

    def test_promo_not_maxed_when_below_limit(self):
        promo = self._create_promo(max_uses=10, current_uses=3)
        self.assertFalse(promo.is_maxed)
        self.assertTrue(promo.is_usable)

    def test_promo_unlimited_uses(self):
        promo = self._create_promo(max_uses=0, current_uses=999)
        self.assertFalse(promo.is_maxed)
        self.assertTrue(promo.is_usable)

    def test_promo_deactivated(self):
        promo = self._create_promo()
        promo.action_deactivate()
        self.assertFalse(promo.is_active)
        self.assertFalse(promo.is_usable)

    def test_promo_reactivated(self):
        promo = self._create_promo()
        promo.action_deactivate()
        promo.action_activate()
        self.assertTrue(promo.is_active)
        self.assertTrue(promo.is_usable)

    def test_increment_use(self):
        promo = self._create_promo(max_uses=10)
        self.assertEqual(promo.current_uses, 0)
        promo.action_increment_use()
        self.assertEqual(promo.current_uses, 1)
        promo.action_increment_use()
        self.assertEqual(promo.current_uses, 2)

    def test_discount_value_must_be_positive(self):
        with self.assertRaises(ValidationError):
            self._create_promo(discount_value=0)

    def test_discount_value_negative_rejected(self):
        with self.assertRaises(ValidationError):
            self._create_promo(discount_value=-5.0)

    def test_percentage_over_100_rejected(self):
        with self.assertRaises(ValidationError):
            self._create_promo(discount_type="percentage", discount_value=150.0)

    def test_fixed_discount_over_100_allowed(self):
        """Fixed amount discounts > 100 are valid (e.g. $150 off)."""
        promo = self._create_promo(discount_type="fixed", discount_value=150.0)
        self.assertEqual(promo.discount_value, 150.0)

    def test_end_date_before_start_rejected(self):
        with self.assertRaises(ValidationError):
            self._create_promo(
                start_date=self._now(),
                end_date=self._now() - timedelta(days=1),
            )

    def test_scope_product_and_category_exclusive(self):
        with self.assertRaises(ValidationError):
            self._create_promo(
                product_id=self.product.id,
                category_id=self.categ_concentrate.id,
            )

    def test_scope_display_store_wide(self):
        promo = self._create_promo()
        self.assertEqual(promo.scope_display, "Store-Wide")

    def test_scope_display_category(self):
        promo = self._create_promo(category_id=self.categ_concentrate.id)
        self.assertIn("Concentrate", promo.scope_display)

    def test_scope_display_product(self):
        promo = self._create_promo(product_id=self.product.id)
        self.assertIn(self.product.name, promo.scope_display)

    def test_get_active_promotions(self):
        """Active promotions should appear in get_active_promotions."""
        promo = self._create_promo(name="Active Test Promo")
        active = self.env["greenlight.promotion"].get_active_promotions()
        self.assertIn(promo.id, active.ids)

    def test_expired_promo_not_in_active(self):
        promo = self._create_promo(
            name="Expired Promo",
            start_date=self._now() - timedelta(days=60),
            end_date=self._now() - timedelta(days=1),
        )
        active = self.env["greenlight.promotion"].get_active_promotions()
        self.assertNotIn(promo.id, active.ids)

    def test_get_applicable_by_category(self):
        promo = self._create_promo(
            name="Concentrate Promo",
            category_id=self.categ_concentrate.id,
        )
        applicable = self.env["greenlight.promotion"].get_applicable_promotions(
            category_id=self.categ_concentrate.id,
        )
        self.assertIn(promo.id, applicable.ids)

    def test_get_applicable_by_product(self):
        promo = self._create_promo(
            name="Product Promo",
            product_id=self.product.id,
        )
        applicable = self.env["greenlight.promotion"].get_applicable_promotions(
            product_id=self.product.id,
        )
        self.assertIn(promo.id, applicable.ids)

    def test_store_wide_promo_applies_to_everything(self):
        promo = self._create_promo(name="Store-Wide Sale")
        applicable = self.env["greenlight.promotion"].get_applicable_promotions(
            product_id=self.product.id,
        )
        self.assertIn(promo.id, applicable.ids)
