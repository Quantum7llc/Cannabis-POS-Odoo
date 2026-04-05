# Green Light POS — Odoo 19.0 Custom Addons

Cannabis dispensary POS system for Mississippi. Built as Odoo 19.0 Community Edition custom addons.

A parallel Rust + TypeScript implementation exists at `Quantum7llc/Cannabis-POS` — compliance rules must stay in sync between both repos.

## Module Map

| Module | What it does | Key models |
|--------|-------------|------------|
| `greenlight_pos` | Core POS: patients, products, transactions, employees, shifts, cash drawers, settings | `greenlight.customer`, `greenlight.product`, `greenlight.transaction`, `greenlight.employee`, `greenlight.settings` |
| `greenlight_compliance` | MMCEU purchase limit enforcement, 280E COGS tracking | `greenlight.purchase.limit` + `_inherit` on `greenlight.transaction` |
| `greenlight_metrc` | Metrc seed-to-sale API integration | `greenlight.metrc.config`, `greenlight.metrc.sync.log`, `greenlight.metrc.package` |
| `greenlight_mspmp` | Mississippi PMP daily batch reporting (ASAP 4.2 format, SFTP upload) | `greenlight.mspmp.batch` |
| `greenlight_exchange` | **Test module** — currency exchange rate dashboard. Standalone, no POS deps. Use to verify Odoo environment works. |

## Compliance Rules (CRITICAL)

These rules are law — get them wrong and the dispensary loses its license.

- **MMCEU limits**: 84g flower / 24 MMCEU rolling 30-day window per patient. See `docs/shared-compliance/mmceu-calculation.md`.
- **MMCEU formulas**: Flower = weight/3.5, Concentrate/Edible = weight * THC% / 100. Product type derived from category name keywords.
- **Metrc**: Seed-to-sale tracking. Every sale must be reported. API spec in `docs/shared-compliance/metrc-integration.md`.
- **MSPMP**: Daily ASAP 4.2 batch file via SFTP to PMP Clearinghouse. Spec in `docs/shared-compliance/mspmp-reporting.md`.
- **280E COGS**: Track cost basis per product. Spec in `docs/shared-compliance/280e-cogs.md`.
- **Any change to compliance logic must be reflected in BOTH the Odoo and Rust repos.**

## Odoo 19.0 Gotchas

Things that changed from Odoo 17/18 that we already hit during development:

- **Security groups**: Use `res.groups.privilege` (not `ir.module.category`). Groups use `privilege_id` (not `category_id`).
- **Cron jobs**: `ir.cron` no longer has `state`, `code`, `model_id`, `numbercall`. Create an `ir.actions.server` record and reference it via `ir_actions_server_id`.
- **Search views**: No `<field>` elements allowed. No `<group expand="0">` wrapper for group-by filters. Just use flat `<filter>` elements.
- **Computed fields in domains**: Non-stored computed fields cannot be used in search view filter domains. Add `store=True` if you need to filter by them.
- **`_sql_constraints`**: Deprecated. Use `model.Constraint` instead (we haven't migrated yet — it's a warning, not an error).
- **Graph views**: `type="col"` is removed. Use `type="row"` for grouping dimensions.

The full Odoo 19.0 reference library is at `docs/odoo-19-reference/` (ORM, views, controllers, frontend, testing, POS, inventory, accounting, 20 OCA modules).

## Architecture Patterns

- **Transaction lifecycle**: Draft → Confirmed → Voided. `action_confirm()` decrements inventory (atomic SQL), `action_void()` restores it.
- **Compliance hook**: `greenlight_compliance` uses `_inherit = "greenlight.transaction"` to intercept `action_confirm` and `action_void`. Calls `check_and_record()` with `sudo()` and `pg_advisory_xact_lock` for concurrency safety.
- **Tax rate**: Configurable via `greenlight.settings` model (admin-only). `get_tax_rate()` class method used by transaction line compute.
- **Sensitive fields**: `pin_hash` and `totp_secret` on employees are restricted to `groups="greenlight_pos.group_admin"`.
- **RBAC**: 3-tier — Budtender (counter staff) → Manager → Admin. Defined in `security/security_groups.xml`, enforced via `security/ir.model.access.csv`.

## Community vs Enterprise

**All modules MUST work on Odoo Community Edition.** Do not use:
- `<dashboard>` view tag (Enterprise only)
- `web_enterprise` dependency
- Cohort, Map, or Gantt views
- Studio customizations
- IoT Box integration

See `CONTRIBUTING.md` for the full compatibility table.

## Development

### Docker (recommended)
```bash
cd dev/docker
docker-compose up -d
# Odoo at http://localhost:8069
# Auto-installs greenlight_exchange with demo data
```

### Install all modules
```bash
odoo -d mydb -i greenlight_pos,greenlight_compliance,greenlight_metrc,greenlight_mspmp,greenlight_exchange \
  --addons-path=/path/to/this/repo,/path/to/odoo/addons
```

### Run tests
```bash
./dev/scripts/run_tests.sh greenlight_exchange
```

### Module install order
Dependencies resolve automatically, but if installing manually: `greenlight_pos` → `greenlight_compliance` → `greenlight_metrc` / `greenlight_mspmp` (both depend on pos, mspmp also depends on compliance).

## File Conventions

- Models: `greenlight_<module>/models/<entity>.py` — one file per model
- Views: `greenlight_<module>/views/<entity>_views.xml` — form + list + search per model
- Security: `security/security_groups.xml` (groups), `security/ir.model.access.csv` (ACLs)
- Data: `data/` — seed data (`noupdate="1"`), sequences, cron jobs
- Tests: `tests/test_<entity>.py` — must be imported in `tests/__init__.py` or Odoo won't discover them

## What NOT to Do

- Don't add `point_of_sale`, `stock`, or `account` to dependencies unless you're actually extending those models. They pull in heavy JS bundles and may not be installed in test environments.
- Don't use `display_name` as a custom field — it's reserved by the ORM.
- Don't forget `ir.model.access.csv` entries for new models — budtenders will get `AccessError`.
- Don't use `ondelete` default (`set null`) on required Many2one fields — use `restrict` or `cascade`.
- Don't put `<field>` elements in search views (Odoo 19 RNG schema rejects them).
