# 280E COGS Tracking

**IRS Section 280E** — Cannabis businesses cannot deduct normal business expenses but CAN deduct Cost of Goods Sold.

## Requirements

- Track COGS (cost basis) for every product at the SKU level
- Separate COGS-eligible expenses from non-deductible operating expenses
- Generate reports breaking down gross revenue, COGS, and gross profit
- Maintain audit trail for all cost adjustments

## COGS-Eligible Items

- Product purchase cost (wholesale price from supplier)
- Freight/shipping to dispensary
- Processing/packaging costs directly tied to product
- Quality testing / lab costs per batch

## Non-Deductible (280E blocked)

- Rent, utilities, marketing, payroll, insurance, legal, etc.
- These are tracked for internal P&L but cannot reduce taxable income

## Both Implementations Must

1. Store `cost_cents` per product (wholesale cost basis)
2. Calculate COGS per transaction: `sum(item.cost_cents * item.quantity)`
3. Generate daily/weekly/monthly COGS reports
4. Support cost adjustments with audit trail
