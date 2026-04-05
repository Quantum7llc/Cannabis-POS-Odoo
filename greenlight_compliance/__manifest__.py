{
    "name": "Green Light POS - Compliance",
    "version": "19.0.1.0.0",
    "category": "Point of Sale",
    "summary": "MMCEU purchase limits, 280E COGS, audit trail for Mississippi cannabis",
    "author": "Quantum7 LLC",
    "website": "https://pos.ezdiscountproducts.com",
    "license": "LGPL-3",
    "depends": [
        "greenlight_pos",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/purchase_limit_views.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "auto_install": False,
}
