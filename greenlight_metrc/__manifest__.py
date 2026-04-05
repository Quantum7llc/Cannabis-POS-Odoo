{
    "name": "Green Light POS - Metrc Integration",
    "version": "19.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Metrc seed-to-sale tracking API integration for Mississippi cannabis",
    "author": "Quantum7 LLC",
    "website": "https://pos.ezdiscountproducts.com",
    "license": "LGPL-3",
    "depends": [
        "greenlight_pos",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/cron.xml",
        "views/metrc_config_views.xml",
        "views/metrc_sync_views.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "auto_install": False,
    "external_dependencies": {
        "python": ["requests"],
    },
}
