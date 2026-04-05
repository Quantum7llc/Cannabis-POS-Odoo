# Contributing to Cannabis-POS-Odoo

## Quick Start

```bash
# Clone and start
git clone https://github.com/Quantum7llc/Cannabis-POS-Odoo.git
cd Cannabis-POS-Odoo/dev/docker
docker compose up -d

# Access Odoo at http://localhost:8069
# Default credentials: admin / admin
# The exchange rate test module auto-installs with demo data
```

## Community vs Enterprise

**Our modules target Odoo 19.0 Community** — they MUST work without Enterprise.

### What's safe to use (works everywhere)

| Feature | Community | Enterprise |
|---------|-----------|------------|
| **Form views** | Yes | Yes |
| **List/tree views** | Yes | Yes |
| **Graph views** (line, bar, pie) | Yes | Yes |
| **Pivot views** | Yes | Yes |
| **Kanban views** | Yes | Yes |
| **Search views** | Yes | Yes |
| **Calendar views** | Yes | Yes |
| **Wizards** (TransientModel) | Yes | Yes |
| **Controllers** (http.route) | Yes | Yes |
| **Cron jobs** (ir.cron) | Yes | Yes |
| **Reports** (QWeb PDF) | Yes | Yes |
| **Mail thread** (chatter) | Yes | Yes |
| **Security** (groups, ACL, rules) | Yes | Yes |
| **ORM** (all of it) | Yes | Yes |

### Enterprise-only (DO NOT use in core modules)

| Feature | Notes |
|---------|-------|
| **Dashboard view** (`<dashboard>`) | Use graph+pivot combo instead |
| **Cohort view** | Enterprise analytics |
| **Map view** | Enterprise only |
| **Gantt view** | Enterprise only |
| **Studio** | Enterprise customization tool |
| **IoT Box** integration | Enterprise POS hardware |
| **Barcode app** | Enterprise (the base barcode scanning works though) |
| **Knowledge** | Enterprise only |

### If tutorials show Enterprise features

Many Odoo tutorials assume Enterprise. When you see code that fails on Community:

1. **`<dashboard>` tag in views** — Replace with a graph + pivot + list combo action (see `greenlight_exchange/views/dashboard_views.xml` for the pattern)
2. **`web_enterprise` in depends** — Remove it; find a Community alternative
3. **`spreadsheet` views** — Use pivot views instead
4. **Theme imports from enterprise** — Use `web` module assets instead

### Testing on both editions

```bash
# Community (default)
cd dev/docker && docker compose up -d

# Enterprise (if you have access)
cd dev/docker && docker compose -f docker-compose.yml -f docker-compose.enterprise.yml up -d
```

## Module Development Workflow

### Creating a new module

```bash
mkdir greenlight_yourmodule
# Follow the structure of greenlight_exchange as a template:
# __manifest__.py, __init__.py, models/, views/, security/, tests/
```

### Key files every module needs

1. **`__manifest__.py`** — Module metadata, dependencies, data files
2. **`__init__.py`** — Python package imports (models, controllers, wizard)
3. **`security/ir.model.access.csv`** — Access control (REQUIRED or you get permission errors)
4. **`views/*.xml`** — UI views and menu items
5. **`models/*.py`** — Business logic (ORM models)

### Running tests

```bash
./dev/scripts/run_tests.sh greenlight_exchange
```

### Common gotchas

- **Missing access rights**: If you get "Access Denied", you forgot `ir.model.access.csv` entries
- **Module not found**: Check `addons_path` in odoo.conf or docker command
- **XML ID not found**: Data files must be listed in `__manifest__.py` `data` list IN ORDER (dependencies first)
- **`noupdate="1"`**: Records in `<data noupdate="1">` won't update on module upgrade — use for seed data only
- **Computed fields**: Always set `store=True` if you want to search/filter/group by the field

## Project Rules

1. All modules must work on **Odoo 19.0 Community Edition**
2. Follow [OCA coding standards](https://github.com/OCA/odoo-community.org/blob/master/website/Ede/Coding_guidelines.rst)
3. Compliance logic (MMCEU, Metrc, MSPMP, 280E) must match the Rust implementation — see `docs/shared-compliance/`
4. Every model needs access rights in `ir.model.access.csv`
5. Include tests for business logic
