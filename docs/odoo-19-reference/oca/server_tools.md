# OCA/server-tools


> **OCA Community Modules (19.0)**
> Source: https://github.com/OCA/server-tools/tree/19.0

## Purpose

OCA server utilities: sequence reset, database cleanup, attachment management, scheduled action logging, and configuration export. Use for server-side maintenance and administration tasks.

---


## Module Overview


# server-tools

server-tools

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[auditlog](auditlog/) | 19.0.1.0.1 |  | Audit Log
[base_cron_exclusion](base_cron_exclusion/) | 19.0.1.0.0 |  | Allow you to select scheduled actions that should not run simultaneously.
[base_exception](base_exception/) | 19.0.1.0.0 |   | This module provide an abstract model to manage customizable exceptions to be applied on different models (sale order, invoice, ...)
[base_partition](base_partition/) | 19.0.1.0.0 |  | Base module that provide the partition method on all models
[base_technical_user](base_technical_user/) | 19.0.1.0.0 |  | Add a technical user parameter on the company
[base_time_window](base_time_window/) | 19.0.1.0.0 |  | Base model to handle time windows
[base_view_inheritance_extension](base_view_inheritance_extension/) | 19.0.1.0.0 |  | Adds more operators for view inheritance
[bus_alt_connection](bus_alt_connection/) | 19.0.1.0.0 |  | Needed when using PgBouncer as a connection pooler
[database_cleanup](database_cleanup/) | 19.0.1.0.1 |  | Database cleanup
[field_vector](field_vector/) | 19.0.1.0.0 |  | New specialized field to store vector data
[iap_alternative_provider](iap_alternative_provider/) | 19.0.1.0.0 |  | Base module for providing alternative provider for iap apps
[module_auto_update](module_auto_update/) | 19.0.1.0.0 |  | Automatically update Odoo modules
[module_change_auto_install](module_change_auto_install/) | 19.0.1.0.0 |  | Customize auto installables modules by configuration
[onchange_helper](onchange_helper/) | 19.0.1.0.0 |  | Technical module that ease execution of onchange in Python code
[sequence_python](sequence_python/) | 19.0.1.0.0 |  | Calculate a sequence number from a Python expression
[session_db](session_db/) | 19.0.1.0.0 |  | Store sessions in DB
[test_auditlog](test_auditlog/) | 19.0.1.0.0 |  | Additional unit tests for Audit Log based on accounting models
[upgrade_analysis](upgrade_analysis/) | 19.0.1.0.3 |   | Performs a difference analysis between modules installed on two different Odoo instances

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.