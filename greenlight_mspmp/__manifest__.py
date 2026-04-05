{
    "name": "Green Light POS - MSPMP Reporting",
    "version": "19.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Mississippi PMP (ASAP 4.2) daily batch reporting via SFTP",
    "author": "Quantum7 LLC",
    "website": "https://pos.ezdiscountproducts.com",
    "license": "LGPL-3",
    "depends": [
        "greenlight_pos",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/mspmp_views.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "auto_install": False,
    "external_dependencies": {
        "python": ["paramiko"],
    },
}
