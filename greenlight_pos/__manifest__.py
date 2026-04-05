{
    "name": "Green Light POS",
    "version": "19.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Cannabis dispensary POS for Mississippi",
    "description": """
        Green Light POS — Cannabis Dispensary Point of Sale
        ==================================================

        Core POS module for Mississippi cannabis dispensaries.

        Features:
        - Patient/customer management with ID verification
        - Product catalog with THC/CBD tracking
        - Transaction processing with multiple payment methods
        - Employee management with PIN authentication and RBAC
        - Cash drawer management and shift tracking
        - Receipt generation and printing
        - Inventory management with lot/batch tracking
        - Loyalty points and rewards program
        - Promotion and discount engine
        - Queue management for walk-in patients

        Compliance:
        - Mississippi MMCP purchase limits (via greenlight_compliance)
        - Metrc seed-to-sale integration (via greenlight_metrc)
        - MSPMP PMP reporting (via greenlight_mspmp)
    """,
    "author": "Quantum7 LLC",
    "website": "https://pos.ezdiscountproducts.com",
    "license": "LGPL-3",
    "depends": [
        "base",
        "mail",
    ],
    "data": [
        "security/security_groups.xml",
        "security/ir.model.access.csv",
        "data/sequences.xml",
        "data/product_categories.xml",
        "data/default_settings.xml",
        "data/receipt_email_template.xml",
        "views/customer_views.xml",
        "views/product_views.xml",
        "views/transaction_views.xml",
        "views/employee_views.xml",
        "views/cash_drawer_views.xml",
        "views/settings_views.xml",
        "views/inventory_views.xml",
        "views/receipt_views.xml",
        "views/order_views.xml",
        "views/queue_views.xml",
        "views/promotion_views.xml",
        "views/dashboard_views.xml",
        "views/menu.xml",
    ],
    "demo": [
        "data/demo_data.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
