# Cannabis-POS-Odoo

Green Light POS — Cannabis dispensary POS system built on **Odoo 19.0 Community Edition** custom addons.

Verified installing cleanly on Odoo 19.0-20260324.

## Project Context

This is the Odoo implementation of the Green Light POS system for Mississippi cannabis dispensaries. A parallel Rust + TypeScript implementation exists at [Quantum7llc/Cannabis-POS](https://github.com/Quantum7llc/Cannabis-POS).

Both versions target the same compliance requirements:
- **Mississippi MMCP** — 84g / 24 MMCEU rolling 30-day purchase limits
- **Metrc** — Seed-to-sale tracking integration (API access obtained)
- **MSPMP** — ASAP 4.2 daily batch reporting to PMP Clearinghouse
- **280E** — COGS tracking for federal tax compliance
- **HIPAA** — PHI encryption for patient data

## Modules

| Module | Purpose | Status |
|--------|---------|--------|
| `greenlight_pos` | Core POS — patients, products, transactions, employees, shifts, cash drawers, dispensary settings | Scaffold complete |
| `greenlight_compliance` | MMCEU purchase limit enforcement (advisory locks, rolling 30-day), 280E COGS | Scaffold complete |
| `greenlight_metrc` | Metrc API integration — config, package sync, sync log, webhook ingest | Models + views ready, API calls not yet implemented |
| `greenlight_mspmp` | Mississippi PMP reporting — ASAP 4.2 batch generation + SFTP upload via paramiko | Fully implemented |
| `greenlight_exchange` | **Test module** — currency exchange rate dashboard with dummy data. Standalone, no POS deps. Use to verify your Odoo environment. | Fully implemented |

## Quick Start

### Docker (recommended)

```bash
cd dev/docker
docker-compose up -d
# Odoo at http://localhost:8069
# Create a database, then install modules from Apps
```

### Manual

1. Clone into your Odoo custom addons directory:
   ```bash
   cd /opt/odoo/custom-addons
   git clone https://github.com/Quantum7llc/Cannabis-POS-Odoo.git
   ```

2. Add to `odoo.conf`:
   ```ini
   addons_path = /opt/odoo/odoo/addons,/opt/odoo/custom-addons/Cannabis-POS-Odoo
   ```

3. Install:
   ```bash
   odoo -d mydb -i greenlight_pos,greenlight_compliance,greenlight_metrc,greenlight_mspmp,greenlight_exchange
   ```

> **Note:** `greenlight_mspmp` requires `pip install paramiko` for SFTP upload.

## Architecture

```
greenlight_pos (core)
├── greenlight_compliance (MMCEU limits, inherits transaction confirm/void)
│   └── greenlight_mspmp (PMP reporting, depends on compliance for menu)
├── greenlight_metrc (Metrc API, standalone from compliance)
└── greenlight_exchange (test module, no POS deps)
```

### Key Patterns

- **Transaction lifecycle**: Draft → Confirmed (inventory decremented atomically) → Voided (inventory restored)
- **Compliance hook**: `greenlight_compliance` uses `_inherit = "greenlight.transaction"` to run MMCEU limit checks on confirm and mark limits voided on void
- **Concurrency safety**: `pg_advisory_xact_lock` on customer ID prevents two terminals from racing past purchase limits; atomic SQL for inventory updates
- **RBAC**: Budtender → Manager → Admin (3-tier, defined via `res.groups.privilege`)
- **Tax rate**: Configurable in Settings → Dispensary Settings (default 7% Mississippi sales tax)

## Compliance Documentation

Business logic that both the Rust and Odoo implementations must enforce identically:

| Document | What it covers |
|----------|---------------|
| [`docs/shared-compliance/mmceu-calculation.md`](docs/shared-compliance/mmceu-calculation.md) | MMCEU formulas by product type, rolling window rules, voiding |
| [`docs/shared-compliance/metrc-integration.md`](docs/shared-compliance/metrc-integration.md) | Metrc API endpoints, sync status tracking, audit trail |
| [`docs/shared-compliance/mspmp-reporting.md`](docs/shared-compliance/mspmp-reporting.md) | ASAP 4.2 format, SFTP delivery, required fields |
| [`docs/shared-compliance/280e-cogs.md`](docs/shared-compliance/280e-cogs.md) | COGS tracking, eligible expenses, reporting |

## Reference Library

Full Odoo 19.0 documentation is included at `docs/odoo-19-reference/`:
- **Developer**: ORM, views, actions, security, testing, frontend (Owl), controllers, reports, QWeb
- **Applications**: Point of Sale, inventory, accounting, sales, purchase, CRM
- **OCA Modules**: 20 community addon references (POS, REST framework, RMA, stock, etc.)

## Development

### Run tests
```bash
./dev/scripts/run_tests.sh greenlight_exchange
```

### Reset database
```bash
./dev/scripts/reset_db.sh
```

### Community vs Enterprise
All modules target **Odoo Community Edition**. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the compatibility table and what to avoid.

## Roadmap

See [open issues](https://github.com/Quantum7llc/Cannabis-POS-Odoo/issues) for the full backlog. Key items:
- [#1 Metrc API client](https://github.com/Quantum7llc/Cannabis-POS-Odoo/issues/1) — High priority
- [#2 POS touch-screen interface](https://github.com/Quantum7llc/Cannabis-POS-Odoo/issues/2) — High priority
- [#6 Payment processor](https://github.com/Quantum7llc/Cannabis-POS-Odoo/issues/6) — High priority
- [#3 Inventory management](https://github.com/Quantum7llc/Cannabis-POS-Odoo/issues/3) — Medium
- [#4 Reports](https://github.com/Quantum7llc/Cannabis-POS-Odoo/issues/4) — Medium

## Team

- **Rust + TypeScript version**: Quantum7 LLC (US)
- **Odoo version**: UK-based contributor

## License

LGPL-3.0 (standard for Odoo community modules)
