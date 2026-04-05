# MMCEU Calculation Rules

**Mississippi Medical Cannabis Equivalency Units**

Both the Rust and Odoo implementations MUST use identical calculation logic.

## Limits

- **Rolling window**: 30 calendar days
- **Maximum per patient**: 84 grams flower-equivalent OR 24 MMCEU
- **Per-purchase tracking**: Each transaction is recorded with its `reset_at` date (purchase_date + 30 days)

## MMCEU Formulas by Product Type

### Flower
```
mmceu = weight_grams / 3.5
```
One MMCEU = 3.5 grams of flower.

### Concentrate
```
mmceu = (weight_grams * thc_percent / 100 * 1000) / 1000
```
Simplified: `mmceu = weight_grams * thc_percent / 100`

### Edible / Infused
```
mmceu = (weight_grams * thc_percent / 100 * 1000) / 1000
```
Same formula as concentrate.

### Accessories
No MMCEU tracking required.

## Product Type Resolution

Product type is derived from the product's **category**, not a separate field:
- Category contains "flower" / "bud" / "pre-roll" -> `flower`
- Category contains "concentrate" / "extract" / "wax" / "shatter" / "rosin" -> `concentrate`
- Category contains "edible" / "gummy" / "chocolate" / "beverage" / "tincture" / "capsule" -> `infused`
- Otherwise -> `accessory`

See Rust implementation: `product_type_from_category()` in the Cannabis-POS backend.

## Voiding

When a transaction is voided, its corresponding `purchase_limits` record must be marked `voided = TRUE` and excluded from rolling totals.

## Timezone

All purchase dates and limit calculations use **US Central Time** (America/Chicago).
