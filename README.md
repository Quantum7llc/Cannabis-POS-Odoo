# Cannabis-POS-Odoo

Green Light POS — Cannabis dispensary POS system built on **Odoo 19.0** custom addons.

## Project Context

This is the Odoo implementation of the Green Light POS system for Mississippi cannabis dispensaries. A parallel Rust + TypeScript implementation exists at [Quantum7llc/Cannabis-POS](https://github.com/Quantum7llc/Cannabis-POS).

Both versions target the same compliance requirements:
- **Mississippi MMCP** — 84g / 24 MMCEU rolling 30-day purchase limits
- **Metrc** — Seed-to-sale tracking integration (API access obtained)
- **MSPMP** — ASAP 4.2 daily batch reporting to PMP Clearinghouse
- **280E** — COGS tracking for federal tax compliance
- **HIPAA** — PHI encryption for patient data

## Module Overview

| Module | Purpose |
|--------|---------|
| `greenlight_pos` | Core POS — products, customers, transactions, employees, cash drawers, receipts, inventory |
| `greenlight_metrc` | Metrc API integration — package sync, sale reporting, webhook ingest |
| `greenlight_mspmp` | Mississippi PMP reporting — ASAP 4.2 batch generation, SFTP upload |
| `greenlight_compliance` | MMCEU purchase limit tracking, 280E COGS, audit trail |

## Setup

### Prerequisites
- Odoo 19.0 (Community or Enterprise)
- PostgreSQL 16+
- Python 3.12+

### Installation

1. Clone this repo into your Odoo custom addons directory:
   ```bash
   cd /opt/odoo/custom-addons
   git clone https://github.com/Quantum7llc/Cannabis-POS-Odoo.git
   ```

2. Add the path to your `odoo.conf`:
   ```ini
   addons_path = /opt/odoo/odoo/addons,/opt/odoo/custom-addons/Cannabis-POS-Odoo
   ```

3. Restart Odoo and install the modules:
   ```bash
   ./odoo-bin -u greenlight_pos,greenlight_compliance,greenlight_metrc,greenlight_mspmp
   ```

## Shared Compliance Rules

Business logic that **both** implementations (Rust and Odoo) must enforce identically is documented in [`docs/shared-compliance/`](docs/shared-compliance/). Any change to compliance rules must be reflected in both repos.

## Team

- **Rust + TypeScript version**: Quantum7 LLC (US)
- **Odoo version**: UK-based contributor

## License

LGPL-3.0 (standard for Odoo community modules)
