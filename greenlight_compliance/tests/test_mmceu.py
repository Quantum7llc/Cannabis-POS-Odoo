from odoo.tests.common import TransactionCase


class TestMMCEUCalculation(TransactionCase):
    """Ensure MMCEU calculations match the Rust implementation.

    See docs/shared-compliance/mmceu-calculation.md for canonical rules.
    """

    def setUp(self):
        super().setUp()
        self.PurchaseLimit = self.env["greenlight.purchase.limit"]

    def test_flower_mmceu(self):
        # 3.5g flower = 1.0 MMCEU
        self.assertAlmostEqual(self.PurchaseLimit.calculate_mmceu("flower", 3.5, 0), 1.0)
        # 7g flower = 2.0 MMCEU
        self.assertAlmostEqual(self.PurchaseLimit.calculate_mmceu("flower", 7.0, 0), 2.0)
        # 84g flower = 24.0 MMCEU (full limit)
        self.assertAlmostEqual(self.PurchaseLimit.calculate_mmceu("flower", 84.0, 0), 24.0)

    def test_concentrate_mmceu(self):
        # 1g concentrate at 80% THC = 0.8 MMCEU
        self.assertAlmostEqual(self.PurchaseLimit.calculate_mmceu("concentrate", 1.0, 80.0), 0.8)
        # 0.5g at 90% = 0.45
        self.assertAlmostEqual(self.PurchaseLimit.calculate_mmceu("concentrate", 0.5, 90.0), 0.45)

    def test_infused_mmceu(self):
        # 50g edible at 10% THC = 5.0 MMCEU
        self.assertAlmostEqual(self.PurchaseLimit.calculate_mmceu("infused", 50.0, 10.0), 5.0)

    def test_accessory_no_mmceu(self):
        self.assertEqual(self.PurchaseLimit.calculate_mmceu("accessory", 100.0, 50.0), 0.0)
