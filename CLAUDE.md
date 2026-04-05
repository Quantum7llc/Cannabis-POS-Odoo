# Green Light POS — Odoo 19.0 Custom Addons

Cannabis dispensary POS system for Mississippi. Built as Odoo 19.0 Community Edition custom addons.

A parallel Rust + TypeScript implementation exists at `Quantum7llc/Cannabis-POS` — compliance rules must stay in sync between both repos.

## Module Map

| Module | What it does | Key models |
|--------|-------------|------------|
| `greenlight_pos` | Core POS with 20+ models covering the full dispensary workflow | See domain table below |
| `greenlight_compliance` | MMCEU purchase limit enforcement, 280E COGS tracking | `greenlight.purchase.limit` + `_inherit` on `greenlight.transaction` |
| `greenlight_metrc` | Metrc seed-to-sale API integration (sync packages, report sales, webhooks) | `greenlight.metrc.config`, `greenlight.metrc.sync.log`, `greenlight.metrc.package` |
| `greenlight_mspmp` | Mississippi PMP daily batch reporting (ASAP 4.2 format, SFTP upload) | `greenlight.mspmp.batch` |
| `greenlight_exchange` | **Test module** — currency exchange rate dashboard. Standalone, no POS deps. | `greenlight.currency.pair`, `greenlight.exchange.rate` |

### greenlight_pos Domain Breakdown

| Domain | Models | File |
|--------|--------|------|
| Products | `greenlight.product`, `greenlight.product.category` | `models/product.py` |
| Customers | `greenlight.customer` | `models/customer.py` |
| Transactions | `greenlight.transaction`, `greenlight.transaction.line` | `models/transaction.py` |
| Employees | `greenlight.employee`, `greenlight.shift` | `models/employee.py` |
| Cash Drawers | `greenlight.cash.drawer`, `greenlight.cash.drawer.event` | `models/cash_drawer.py` |
| Settings | `greenlight.settings` (tax rate, dispensary info) | `models/settings.py` |
| Receipts | `greenlight.receipt`, `greenlight.refund`, `greenlight.refund.line` | `models/receipt.py` |
| Inventory | `greenlight.inventory.adjustment`, `.count`, `.count.item`, `greenlight.purchase.order`, `.order.line`, `greenlight.reason.code` | `models/inventory.py` |
| Orders | `greenlight.order`, `greenlight.order.line` (5 channels) | `models/order.py` |
| Queue | `greenlight.customer.queue` | `models/queue.py` |
| Promotions | `greenlight.promotion` | `models/promotion.py` |
| Dashboard | `greenlight.dashboard` (TransientModel, today's KPIs) | `models/dashboard.py` |
| Locations | `greenlight.location`, `.room`, `.location.inventory`, `greenlight.stock.transfer`, `.transfer.line` | `models/location.py` |
| Shifts Enhanced | `_inherit greenlight.shift` (cash reconciliation, blind count) | `models/shift_enhanced.py` |
| Closing Reports | `greenlight.closing.report` (end-of-day aggregation) | `models/closing_report.py` |
| POS Hardware | `greenlight.pos.station`, `greenlight.pos.device` | `models/pos_hardware.py` |
| Webhooks | `greenlight.webhook`, `greenlight.webhook.delivery` (HMAC-SHA256) | `models/webhook.py` |
| Audit | `greenlight.audit.log`, `greenlight.change.log` | `models/audit_log.py` |
| Security Roles | `greenlight.security.role`, `greenlight.permission` (35 seeded), `greenlight.role.permission` | `models/security_role.py` |
| Analytics | `greenlight.sales.report`, `.product.performance`, `.employee.performance`, `.customer.analytics`, `.cogs.report`, `.inventory.alert` (SQL views) | `models/analytics.py` |

## Compliance Rules (CRITICAL)

These rules are law — get them wrong and the dispensary loses its license.

- **MMCEU limits**: 84g flower / 24 MMCEU rolling 30-day window per patient. See `docs/shared-compliance/mmceu-calculation.md`.
- **MMCEU formulas**: Flower = weight/3.5, Concentrate/Edible = weight * THC% / 100. Product type derived from category name keywords.
- **Metrc**: Seed-to-sale tracking. Every sale must be reported. API spec in `docs/shared-compliance/metrc-integration.md`.
- **MSPMP**: Daily ASAP 4.2 batch file via SFTP to PMP Clearinghouse. Spec in `docs/shared-compliance/mspmp-reporting.md`.
- **280E COGS**: Track cost basis per product. Spec in `docs/shared-compliance/280e-cogs.md`.
- **Any change to compliance logic must be reflected in BOTH the Odoo and Rust repos.**

## Odoo 19.0 Gotchas

Things that changed from Odoo 17/18 that we discovered during real install testing:

- **Security groups**: Use `res.groups.privilege` (not `ir.module.category`). Groups use `privilege_id` (not `category_id`).
- **Cron jobs**: `ir.cron` no longer has `state`, `code`, `model_id`, `numbercall`. Create an `ir.actions.server` record and reference it via `ir_actions_server_id`.
- **Search views**: No `<field>` elements allowed. No `<group expand="0">` wrapper for group-by filters. Just use flat `<filter>` elements.
- **Computed fields in domains**: Non-stored computed fields cannot be used in search view filter domains. Add `store=True` if you need to filter by them.
- **`_sql_constraints`**: Deprecated. Remove them — use `@api.constrains` for Python-level validation instead.
- **Graph views**: `type="col"` is removed. Use `type="row"` for grouping dimensions.
- **Stat buttons**: `%(action_name)d` in form views requires the action to be defined BEFORE the view in the XML. If you can't reorder, use a Python method button instead.
- **`self._cr`**: Deprecated. Use `self.env.cr` instead.

The full Odoo 19.0 reference library is at `docs/odoo-19-reference/`.

## Architecture Patterns

- **Transaction lifecycle**: Draft → Confirmed (inventory decremented atomically via SQL) → Voided (inventory restored).
- **Compliance hook**: `greenlight_compliance` uses `_inherit = "greenlight.transaction"` to intercept `action_confirm` and `action_void`. Calls `check_and_record()` with `sudo()` and `pg_advisory_xact_lock` for concurrency safety.
- **Receipt lifecycle**: Created from transaction → can be voided (reverses inventory + purchase limits, requires manager) or partially refunded (item-level, restores inventory proportionally).
- **Inventory operations**: Adjustments (atomic SQL), counts (draft→in_progress→completed workflow), purchase orders (draft→ordered→received), stock transfers (confirm deducts source, receive credits destination).
- **Tax rate**: Configurable via `greenlight.settings` model (admin-only). `get_tax_rate()` class method used by transaction line compute.
- **Sensitive fields**: `pin_hash` and `totp_secret` on employees are restricted to `groups="greenlight_pos.group_admin"`.
- **RBAC**: 3-tier Budtender → Manager → Admin via `res.groups.privilege`. Plus granular 35-permission system via `greenlight.security.role`.
- **Webhooks**: HMAC-SHA256 signed outbound events. `Webhook.trigger_event(event_type, payload)` dispatches to all matching active webhooks.
- **Analytics**: SQL-based read-only views (`_auto = False`) for sales, product performance, employee metrics, customer analytics, 280E COGS, inventory alerts.

## Community vs Enterprise

**All modules MUST work on Odoo Community Edition.** Do not use:
- `<dashboard>` view tag, Cohort/Map/Gantt views, `web_enterprise` dependency
- Studio customizations, IoT Box integration

See `CONTRIBUTING.md` for the full compatibility table.

## Development

### Docker (recommended)
```bash
cd dev/docker
docker-compose up -d
# Odoo at http://localhost:8069
```

### Install all modules
```bash
odoo -d mydb -i greenlight_pos,greenlight_compliance,greenlight_metrc,greenlight_mspmp,greenlight_exchange \
  --addons-path=/path/to/this/repo,/path/to/odoo/addons
```

### Run tests
```bash
./dev/scripts/run_tests.sh greenlight_pos
./dev/scripts/run_tests.sh greenlight_exchange
```

### Live test instance
- URL: https://odoo.ezdiscountproducts.com
- Database: `greenlight`

## File Conventions

- Models: `greenlight_<module>/models/<entity>.py` — one file per model or domain group
- Views: `greenlight_<module>/views/<entity>_views.xml` — form + list + search per model
- Security: `security/security_groups.xml` (groups FIRST), `security/ir.model.access.csv` (ACLs SECOND)
- Data: `data/` — seed data (`noupdate="1"`), sequences, cron jobs, permissions
- Tests: `tests/test_<entity>.py` — MUST be imported in `tests/__init__.py`
- Wizards: `wizard/` — TransientModel files with their own `__init__.py`

## What NOT to Do

- Don't add `point_of_sale`, `stock`, or `account` to dependencies unless extending those models.
- Don't use `display_name` as a custom field — reserved by the ORM.
- Don't forget `ir.model.access.csv` entries for new models — budtenders get `AccessError`.
- Don't use `ondelete` default (`set null`) on required Many2one fields — use `restrict` or `cascade`.
- Don't put `<field>` elements in search views (Odoo 19 RNG rejects them).
- Don't use `%(action_id)d` in views that load before the action is defined.
- Don't use `_sql_constraints` — deprecated, use `@api.constrains`.
- Don't use `self._cr` — deprecated, use `self.env.cr`.
