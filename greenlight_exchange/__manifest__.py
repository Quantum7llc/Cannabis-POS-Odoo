{
    "name": "Green Light - Currency Exchange Dashboard",
    "version": "19.0.1.0.0",
    "category": "Tools",
    "summary": "Test module: currency exchange rate dashboard with dummy data",
    "description": """
        Currency Exchange Rate Dashboard (Test Module)
        ===============================================

        A simple test module to verify the Odoo custom addons scaffold works
        correctly on both Community and Enterprise editions.

        Features:
        - Currency pair model with exchange rates over time
        - Dashboard view (list + graph) showing rate trends
        - Wizard to generate dummy data for testing
        - Scheduled action (cron) to simulate rate updates
        - REST-style controller endpoint for external access

        This module has NO dependency on the greenlight_pos modules — it can be
        installed standalone to verify the Odoo environment is working.
    """,
    "author": "Quantum7 LLC",
    "license": "LGPL-3",
    "depends": [
        "base",
        "web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/currency_pairs.xml",
        "data/cron.xml",
        "wizard/generate_dummy_views.xml",
        "views/exchange_rate_views.xml",
        "views/dashboard_views.xml",
        "views/menu.xml",
    ],
    "demo": [
        "data/demo_rates.xml",
    ],
    "assets": {
        "web.assets_backend": [],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
}
