# OCA/sale-workflow


> **OCA Community Modules (19.0)**
> Source: https://github.com/OCA/sale-workflow/tree/19.0

## Purpose

OCA sales workflow extensions: order approval, double validation, invoice from picking, and sale exception handling. Use when adding approval gates or custom sales process steps.

---


## Module Overview


# sale-workflow

sale-workflow

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[product_form_sale_link](product_form_sale_link/) | 19.0.1.0.0 |  | Adds a button on product forms to access Sale Lines
[sale_advance_payment](sale_advance_payment/) | 19.0.1.0.0 |  | Allow to add advance payments on sales and then use them on invoices
[sale_automatic_workflow](sale_automatic_workflow/) | 19.0.1.0.0 |  | Sale Automatic Workflow
[sale_cancel_restrict](sale_cancel_restrict/) | 19.0.1.0.0 |  | Sale Cancel Restrict
[sale_commercial_partner](sale_commercial_partner/) | 19.0.1.0.0 |  | Add stored related field 'Commercial Entity' on sale orders
[sale_confirm_group](sale_confirm_group/) | 19.0.1.0.0 |  | Allows configuring a list of groups per-company who are granted permission to confirm sale orders
[sale_delivery_split_date](sale_delivery_split_date/) | 19.0.1.0.0 |  | Sale Deliveries split by date
[sale_delivery_state](sale_delivery_state/) | 19.0.1.0.0 |  | Show the delivery state on the sale order
[sale_exception](sale_exception/) | 19.0.1.0.0 |  | Custom exceptions on sale order
[sale_fixed_discount](sale_fixed_discount/) | 19.0.1.0.0 |  | Allows to apply fixed amount discounts in sales orders.
[sale_force_invoiced](sale_force_invoiced/) | 19.0.1.0.0 |  | Allows to force the invoice status of the sales order to Invoiced
[sale_fully_invoiced](sale_fully_invoiced/) | 19.0.1.0.0 |  | Useful filters in Sales to know the actual status of invoices.
[sale_global_discount](sale_global_discount/) | 19.0.1.0.0 |  | Sale Global Discount
[sale_invoice_blocking](sale_invoice_blocking/) | 19.0.1.0.0 |  | Allow you to block the creation of invoices from a sale order.
[sale_invoice_frequency](sale_invoice_frequency/) | 19.0.1.0.0 |    | Define the invoice frequency for customers
[sale_last_price_info](sale_last_price_info/) | 19.0.1.0.0 |  | Product Last Price Info - Sale
[sale_order_archive](sale_order_archive/) | 19.0.1.0.0 |  | Archive Sale Orders
[sale_order_disable_user_autosubscribe](sale_order_disable_user_autosubscribe/) | 19.0.1.0.0 |  | Remove the salesperson from autosubscribed sale followers
[sale_order_general_discount](sale_order_general_discount/) | 19.0.1.0.1 |  | General discount per sale order
[sale_order_line_date](sale_order_line_date/) | 19.0.1.0.0 |  | Adds a commitment date to each sale order line.
[sale_order_line_menu](sale_order_line_menu/) | 19.0.1.0.0 |  | Adds a Sale Order Lines Menu
[sale_order_line_note](sale_order_line_note/) | 19.0.1.0.0 |  | Note on sale order line
[sale_order_line_price_history](sale_order_line_price_history/) | 19.0.1.0.0 |   | Sale order line price history
[sale_order_line_sequence](sale_order_line_sequence/) | 19.0.1.0.0 |  | Propagates SO line sequence to invoices and stock picking.
[sale_order_line_tag](sale_order_line_tag/) | 19.0.1.0.0 |    | Add tags to classify sales order line reasons
[sale_order_price_recalculation](sale_order_price_recalculation/) | 19.0.1.0.0 |  | Recalculate prices / Reset descriptions on sale order lines
[sale_order_priority](sale_order_priority/) | 19.0.1.0.0 |  | Define priority on sale orders
[sale_order_type](sale_order_type/) | 19.0.1.1.0 |  | Sale Order Type
[sale_partner_incoterm](sale_partner_incoterm/) | 19.0.1.0.0 |  | Set the customer preferred incoterm on each sales order
[sale_require_po_doc](sale_require_po_doc/) | 19.0.1.0.0 |  | Sale Orders Require PO or Sales Documentation
[sale_stock_delivery_address](sale_stock_delivery_address/) | 19.0.1.0.0 |  | Sale Stock Delivery Address
[sale_stock_picking_blocking](sale_stock_picking_blocking/) | 19.0.1.0.0 |  | Allow you to block the creation of deliveries from a sale order.
[sale_stock_picking_note](sale_stock_picking_note/) | 19.0.1.0.0 |     | Add picking note in sale and purchase order
[sale_stock_reference_by_line](sale_stock_reference_by_line/) | 19.0.1.0.0 |  | Base module for definition of stock references creation rules for Sale order
[sale_substate](sale_substate/) | 19.0.1.0.0 |  | Sale Sub State

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.


---

## Module Details (35 of 35 ported)


### product_form_sale_link

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/product_form_sale_link
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-product_form_sale_link
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
  image: |-
    ```{image} https://user-images.githubusercontent.com/19529533/61035935-5ec0ef80-a3c8-11e9-836a-4aca2e7dec70.png
    ```
---

# Product Form Sale Link

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:4508fb3682d674f289146b0348886e4fab06cf62b28c8137b6377bc7ee07f21c
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module adds a button on product forms with a link to sale order
lines for that product.

**Table of contents**

```{contents}
:local: true
```

# Usage

Go to Sales > Products > Products

Choose a product and click on 'Sales' button.

{{ image }}

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20product_form_sale_link%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- ACSONE SA/NV

## Contributors

- Denis Roussel \<<mailto:denis.roussel@acsone.eu>>
- Heliconia Solutions Pvt. Ltd. \<<https://www.heliconia.io>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/product_form_sale_link) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_advance_payment

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_advance_payment
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_advance_payment
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Advance Payment

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:892a02de5f96ed6aaf77d7bc58fad3d78604340bef42d3a6f5e8ead4c5dc18e4
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

The module allows to add advance payments on sales and then use them on
invoices.

**Table of contents**

```{contents}
:local: true
```

# Usage

To use this module, you need to:

- Go to a sale order.
- Click on "Pay Sale Advance".
- Select the Journal and specify the amount of the advanced payment.
- "Make Advance Payment".

When generating the invoice, the system displays the advanced payments,
select those you want to add to the invoice.

# Known issues / Roadmap

Split several computed values in separate fields (mls, advance_amount,
amount_residual). This allows a better comprehension of logic, and a
better inheritance possibility.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_advance_payment%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Comunitea

## Contributors

- Omar Castiñeira Saaevdra \<<mailto:omar@comunitea.com>>

- Daniel Reis \<<mailto:dreis@opensourceintegrators.com>>

- Nikul Chaudhary \<<mailto:nchaudhary@opensourceintegrators.com>>

- Manuel Regidor \<<mailto:manuel.regidor@sygel.es>>

- Urvisha Desai \<<mailto:udesai@opensourceintegrators.com>>

- [Heliconia Solutions Pvt. Ltd.](https://www.heliconia.io)

  - Bhavesh Heliconia

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_advance_payment) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_automatic_workflow

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_automatic_workflow
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_automatic_workflow
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Automatic Workflow

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:3e6047303b2e32a8322bb1d582f9e04b09ddb6fb5b6c5e6590a1623fe4825bf1
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

Create workflows with more or less automatization and apply it on sales
orders.

A workflow can:

- Apply default values:

  - Shipping Policy (Deliver each product when available or Deliver all
    products at once)
  - Set the invoice's date to the sale order's date
  - Set a sales team

- Apply automatic actions:

  - Validate the order (only if paid, always, never)
  - Send order confirmation mail (only when order confirmed)
  - Create an invoice
  - Validate the invoice
  - Confirm the picking

This module is used by Magentoerpconnect and Prestashoperpconnect. It is
well suited for other E-Commerce connectors as well.

**Table of contents**

```{contents}
:local: true
```

# Usage

To use this module, you need to:

1. Go to \*Sale > Configuration > Automatic Workflow > Automatic
   Workflow
2. You can create/edit/delete automatic workflow

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_automatic_workflow%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Akretion
- Camptocamp
- Sodexis

## Contributors

- Guewen Baconnier
- Beau Sebastien
- Leonardo Pistone
- Stéphane Bidoul
- Damien Crier
- Alexandre Fayolle
- Sodexis
- Dave Lasley \<<mailto:dave@laslabs.com>>
- Akim Juillerat \<<mailto:akim.juillerat@camptocamp.com>>
- Thomas Fossoul \<<mailto:thomas@niboo.com>>
- Phuc Tran Thanh \<<mailto:phuc@trobz.com>>
- Sander Lienaerts \<<mailto:sander.lienaerts@codeforward.nl>>
- Tri Doan \<<mailto:tridm@trobz.com>>
- Chau Le \<<mailto:chaulb@trobz.com>>

## Other credits

The development of this module has been financially supported by:

- Camptocamp

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_automatic_workflow) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_cancel_restrict

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_cancel_restrict
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_cancel_restrict
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Cancel Restrict

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:d6fc1d587d23ca49b379b705098375f16d63432555b14c21c4ddd6270a2e2c4a
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

When you try to cancel a sales order, if there is some delivery done or
an invoice not cancelled will prevent the sales order from being
cancelled.

**Table of contents**

```{contents}
:local: true
```

# Usage

To use this module, you need to:

- Enable Sale Cancel Confirmed Invoice at Sales -> Settings -> Enable
  Sale Cancel Restrict.
- Click at "Cancel Order" button from a sales order which state equal to
  Sales Order
- It will show an alert that prevents the sale order from being
  cancelled.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_cancel_restrict%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- ForgeFlow

## Contributors

- David Jiménez \<<mailto:david.jimenez@forgeflow.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_cancel_restrict) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_commercial_partner

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :alt: Production/Stable
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_commercial_partner
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_commercial_partner
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
  maintainer-alexis-via: |-
    ```{image} https://github.com/alexis-via.png?size=40px
    :alt: alexis-via
    :target: https://github.com/alexis-via
    ```
---

# Sale Commercial Partner

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:bbf4a632af1c319af46cf6d3b3064f2f8b2d15e48169afbca6135c4dd1d485a1
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module adds a related stored field *Commercial Entity* on sale
orders.

This module is the twin brother of the OCA module
*purchase_commercial_partner* located in the [purchase-workflow
project](https://github.com/OCA/purchase-workflow/).

**Table of contents**

```{contents}
:local: true
```

# Usage

You can group by *Commercial Entity*:

- in *Sales > Orders > Quotations*,
- in *Sales > Orders > Orders*,
- in *Sales > Reporting > Sales* (it is a native feature in this menu)

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_commercial_partner%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Akretion

## Contributors

- Alexis de Lattre \<<mailto:alexis.delattre@akretion.com>>

- Serpent Consulting Services Pvt. Ltd. \<<mailto:support@serpentcs.com>>

- Rattapong Chokmasermkul \<<mailto:rattapongc@ecosoft.co.th>>

- Tharathip Chaweewongphan \<<mailto:tharathipc@ecosoft.co.th>>

- [APSL](https://apsl.tech):

  - Antoni Marroig \<<mailto:amarroig@apsl.net>>

- [Dynapps](https://www.dynapps.eu):

  - Bert Van Groenendael \<<mailto:bert.vangroenendael@dynapps.eu>>

- [Trobz](https://www.trobz.com):

  - Nhan Tran \<<mailto:nhant@trobz.com>>

## Other credits

The migration of this module from 17.0 to 18.0 was financially supported
by Camptocamp

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

Current [maintainer](https://odoo-community.org/page/maintainer-role):

{{ maintainer-alexis-via }}

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_commercial_partner) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_confirm_group

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_confirm_group
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_confirm_group
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Confirmation Group

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:5365f3cb1ba6d0b270b99c620f25462dc86668e90da786cc1457f5a1c9424f4b
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module allows configuring a list of groups per-company who are
granted permission to confirm sale orders:

1. button "Confirm" in sale views is always hidden for users not in
   those groups
2. if users outside those groups try to confirm a SO, an error is raised

**Table of contents**

```{contents}
:local: true
```

# Configuration

- go to Sales / Configuration / Settings

- scroll until you find the "Use SO Confirmation Groups" checkbox

- if you want to restrict SO confirmation permission:

  - activate the checkbox
  - add at least 1 security group to the list below the checkbox

- if you don't want to restrict SO confirmation permission:

  - deactivate the checkbox, or remove all security groups from the list
    below the checkbox

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_confirm_group%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Camptocamp

## Contributors

- Silvio Gregorini \<<mailto:silvio.gregorini@camptocamp.com>>
- Simone Orsi \<<mailto:simone.orsi@camptocamp.com>>
- Joshua Jan \<<mailto:joshua@openerp.cn>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_confirm_group) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_delivery_split_date

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_delivery_split_date
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_delivery_split_date
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Delivery Split Date

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:28828191b5116fc66058ad517175abd56e39610ac2011eb4cde0c995b9f2bbd6
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

When this module is installed, each sale order you confirm will generate
one delivery order per requested date indicated in the sale order lines.

Furthermore, the delivery orders can be searched by selecting the
scheduled date, which is now displayed in the delivery tree view.

**Table of contents**

```{contents}
:local: true
```

# Known issues / Roadmap

- Incompatible with
  [sale_procurement_group_by_commitment_date](https://github.com/OCA/sale-workflow/tree/12.0/sale_procurement_group_by_commitment_date)

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_delivery_split_date%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Agile Business Group

## Contributors

- Alex Comba \<<mailto:alex.comba@agilebg.com>> (<https://www.agilebg.com/>)
- Carmen Rondon Regalado \<<mailto:crondon@archeti.com>>
  (<https://odoo.archeti.com/>)
- Tatiana Deribina \<<mailto:tatiana.deribina@sprintit.fi>>

## Other credits

The migration of this module from 18.0 to 19.0 was financially supported
by SprintIT Ltd.

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_delivery_split_date) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_delivery_state

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_delivery_state
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_delivery_state
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale delivery State

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:90e3523004e502279596afc4849b48cd0129b1650d43048405e3541917bdb346
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This odoo module add delivery state on the sale order.

Delivery state is computed based on qty_delivered field on sale order
lines.

This is usefull for other modules to provide the state of delivery. The
state of the sale order can be forced to fully delivered in case some
quantities were cancelled by the customer and you consider you have
nothing more to deliver.

Sale order lines can have products or services, as long as the field
qty_delivered is set, it will trigger the computation of delivery state.

Sale order lines with the Skip Delivery State field set to True will be
ignored when computing the delivery state. This field is automatically
set depending on the field Sales > Configuration > Quotations & Orders >
Skip Service products for Sale Delivery State. If set to True, the field
Skip Delivery State in sale order lines containing service products will
be automatically set to True, but it can manually changed.

This module also works with delivery.carrier fees that are added as a
sale order line. Thoses line are special as they will never be
considered delivered. Delivery fees lines are ignored in the computation
of the delivery state.

When the 'sale_stock' module is installed, the glue module
'sale_stock_delivery_state' should also be installed; this module is
designed to override the compute method of the delivery status field
from 'sale_stock'.

**Table of contents**

```{contents}
:local: true
```

# Configuration

#. Go to *Sales > Configuration > Quotations & Orders*. #. Check the
Skip Service products for Sale Delivery State checkbox to automatically
set the field Skip Delivery State in sale order lines to True when the
line contains a service product.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_delivery_state%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Akretion

## Contributors

- Pierrick BRUN \<<mailto:pierrick.brun@akretion.com>>
- Benoît Guillot \<<mailto:benoit.guillot@akretion.com>>
- Yannick Vaucher \<<mailto:yannick.vaucher@camptocamp.com>>
- Daniel Reis \<<mailto:dreis@opensourceintegrators.com>>, [Open Source
  Integrators](https://opensourceintegrators.com)
- Carlos Lopez \<<mailto:celm1990@gmail.com>>
- Virendrasinh Dabhi \<<mailto:veer.190.dabhi@gmail.com>>
- Manuel Regidor <mailto:manuel.regidor@sygel.es>
- Simone Orsi <mailto:simone.orsi@camptocamp.com>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_delivery_state) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_exception

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_exception
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_exception
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Exception

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:0f49cb2cf71af43034cbba403de9d0e4b68f9442931be70fda1c06096e8a3441
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module allows you attach several customizable exceptions to your
sale order in a way that you can filter orders by exceptions type and
fix them.

This is especially useful in an scenario for mass sales order import
because it's likely some orders have errors when you import them (like
product not found in Odoo, wrong line format etc.)

**Table of contents**

```{contents}
:local: true
```

# Configuration

If you are going to use Customer sale warning and Product warning, for
setting corresponding information, you need to:

1. Go to *Settings > User & Companies > Users*.
2. Edit your user.
3. Check "A warning can be set on a product or a customer (Sale)" group.
4. Install sale_management addon.

# Usage

Not Enough Virtual Stock: #. Go to *Sales > Products > Products*. #.
Create new storable product without stock available. #. Go to *Sales >
Orders > Quotations* #. Create new quotation. #. Add product without
stock available. #. An exception will be displayed.

No ZIP code on destination: #. Go to *Contacts*. #. Edit or create new
contact. #. Set empty zip code. #. Go to *Sales > Orders > Quotations*
#. Create new quotation. #. Set delivery address with no zip code. #. An
exception will be displayed.

Product warning: #. Go to *Sales > Products > Products*. #. Edit or
create new product. #. Go to *Sales* tab. #. Set your desired warning
option under the *Warning when Selling this Product* group. #. Set some
warning message. #. Go to *Sales > Orders > Quotations* #. Create new
quotation. #. Add product with warning message. #. An exception will be
displayed.

Partner warning: #. Go to *Contacts*. #. Edit or create new contact. #.
Go to *Internal notes* tab. #. Set warning option according to *Warning
on the Sales Order* group. #. Set some warning message. #. Go to *Sales
\> Orders > Quotations* #. Create new quotation. #. Set partner with
warning message. #. An exception will be displayed.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_exception%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Akretion
- Sodexis
- Camptocamp

## Contributors

- Raphaël Valyi \<<mailto:raphael.valyi@akretion.com>>
- Renato Lima \<<mailto:renato.lima@akretion.com>>
- Sébastien BEAU \<<mailto:sebastien.beau@akretion.com>>
- Guewen Baconnier \<<mailto:guewen.baconnier@camptocamp.com>>
- Yannick Vaucher \<<mailto:yannick.vaucher@camptocamp.com>>
- Simone Orsi \<<mailto:simahawk@gmail.com>>
- SodexisTeam \<<mailto:dev@sodexis.com>>
- Mourad EL HADJ MIMOUNE \<<mailto:mourad.elhadj.mimoune@akretion.com>>
- Raphaël Reverdy \<<mailto:raphael.reverdy@akretion.com>>
- Florian da Costa \<<mailto:florian.dacosta@akretion.com>>
- Iván Todorovich \<<mailto:ivan.todorovich@druidoo.io>>
- Nguyen Minh Chien \<<mailto:chien@trobz.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_exception) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_fixed_discount

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_fixed_discount
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_fixed_discount
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Fixed Discount

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:79a48a6c1fd7b24c084d7bc837ec3d4021036f0221d7554a032824ef5fd2ea03
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module extends the functionality of Sales to allow you to apply
fixed amount discount at sales order line level.

The module also extends the sales order report to show fixed discount.

**Table of contents**

```{contents}
:local: true
```

# Installation

This module depends on module 'account_invoice_fixed_discount',
available in
<https://github.com/OCA/account-invoicing/tree/18.0/account_invoice_fixed_discount>

# Configuration

To configure this module, you need to:

1. Go to *Sales > Configuration > Settings*.
2. In the *Pricing* section select *Discounts* option to grant discounts
   on sales order lines.

# Usage

To use this module, you need to:

1. Go to *Sales*.
2. Create a Sales Order and specify the type of discount and
   fixed/percent discount in a line.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_fixed_discount%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- ForgeFlow

## Contributors

- Lois Rilo \<<mailto:lois.rilo@forgeflow.com>>
  ([www.forgeflow.com](http://www.forgeflow.com))

- Jordi Ballester \<<mailto:jordi.ballester@forgeflow.com>>
  ([www.forgeflow.com](http://www.forgeflow.com))

- Pieter Paulussen \<<mailto:pieterpaulussen@code-source.be>>
  ([www.code-source.be](http://www.code-source.be))

- OERP Canada \<<https://www.oerp.ca/>>:

  - Foram Darji \<<mailto:fd@oerp.ca>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_fixed_discount) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_force_invoiced

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_force_invoiced
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_force_invoiced
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Force Invoiced

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:03958775991c19c15915ee0cd95642be9b3770fb47caca0eea458cdad878de76
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module adds the possibility for users to force the invoice status
of the sales orders to 'Invoiced', even when not all the quantities
ordered or delivered have been invoiced.

This feature useful in the following scenario:

- The customer disputes the quantities to be invoiced for, after the
  products have been delivered to her/him, and you agree to reduce the
  quantity to invoice (without sending a refund).
- When migrating from a previous Odoo version, in some cases there is
  less quantity invoiced to what was delivered, and you don't want these
  old sales orders to appear in your 'To Invoice' list.

**Table of contents**

```{contents}
:local: true
```

# Usage

1. Create a sales order and confirm it.
2. Deliver the products/services.
3. Create an invoice and reduce the invoiced quantity. The sales order
   invoicing status is 'To Invoice'.
4. Check the field 'Force Invoiced'. The sales order invoicing status
   and Sale Order Line invoicing status will be 'Invoiced'.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_force_invoiced%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- ForgeFlow

## Contributors

- Jordi Ballester \<<mailto:jordi.ballester@forgeflow.com>>
- Erwin van der Ploeg \<<mailto:erwin@odooexperts.nl>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_force_invoiced) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_fully_invoiced

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_fully_invoiced
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_fully_invoiced
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
  maintainer-AaronHForgeFlow: |-
    ```{image} https://github.com/AaronHForgeFlow.png?size=40px
    :alt: AaronHForgeFlow
    :target: https://github.com/AaronHForgeFlow
    ```
---

# Sales Fully Invoiced

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:c6e704d5f8058cc9a3199a881069cb5e1261d3cefe579aac7ad2d43e211aaa66
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

The standard invoice_status field shows information about the status
invoices related to a sales Order. However, it may happen that
invoice_status is "invoiced" while the invoices are still in draft.

This module introduces a field, Fully Invoiced, that considers the
status of the invoices.

**Table of contents**

```{contents}
:local: true
```

# Usage

1. Filter the list of Sale Orders by Fully Invoice Validated

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_fully_invoiced%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Forgeflow

## Contributors

- Aaron Henriquez \<<mailto:aaron.henriquez@forgeflow.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

Current [maintainer](https://odoo-community.org/page/maintainer-role):

{{ maintainer-AaronHForgeFlow }}

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_fully_invoiced) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_global_discount

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_global_discount
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_global_discount
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Global Discount

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:ca976d68ef28ace3b29647c4a5efb68e0febf3b7df0ac0fbf589d09d7546a0f1
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

Apply global financial discounts to sales that will be transmited to
invoices and accounting.

**Table of contents**

```{contents}
:local: true
```

# Configuration

To configure this module please refer to configure section of the
base_global_discount module.

# Usage

To use this module, you need to:

1. See usage section of the base_global_discount module.
2. Create a new sale order and choose a partner.
3. If the partner has customer global discounts set, those will be
   applied to the order by default.
4. Otherwise, you can set them manually from the header of the sale
   order.
5. In the order footer, you can see the computed discounts.
6. When you create an invoice from the order, the proper global
   discounts will be applied on it.

# Known issues / Roadmap

- Not all the taxes combination can be compatible with global discounts.
  An error is raised in that cases.
- Currently, taxes in invoice lines are mandatory with global discounts.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_global_discount%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Tecnativa

## Contributors

- [Tecnativa](https://www.tecnativa.com)

  - David Vidal
  - Pedro M. Baeza

- Omar Castiñeira \<<mailto:omar@comunitea.com>>

- [Studio73](https://www.studio73.es)

  - Miguel Gandia
  - Eugenio Micó
  - Arantxa Gandia

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_global_discount) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_invoice_blocking

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_invoice_blocking
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_invoice_blocking
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Invoice Blocking

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:9d802ad63a781f0e6d10b1d3b1a0b357abb1667de191d688f826e60a062c8c08
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module extends the functionality of sales to allow you to block the
creation of invoices from a sales order and give a reason.

**Table of contents**

```{contents}
:local: true
```

# Configuration

To configure this module, you need to:

1. Go to 'Sales > Configuration > Sales Orders > Invoicing block
   reasons'.
2. Create the different reasons that can lead to block the invoices of a
   sales order.

# Usage

To use this module, you need to:

1. Create a new sale order and provide a 'Blocking for invoicing'.
2. When you try to create Regular Invoice if an invoicing blocking
   reason is set on the sale order. It will show blocking reasons.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_invoice_blocking%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Camptocamp

## Contributors

- Damien Crier \<<mailto:damien.crier@camptocamp.com>>
- Dhara Solanki \<<mailto:dhara.solanki@initos.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_invoice_blocking) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_invoice_frequency

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_invoice_frequency
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_invoice_frequency
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
  maintainer-EmilioPascual: |-
    ```{image} https://github.com/EmilioPascual.png?size=40px
    :alt: EmilioPascual
    :target: https://github.com/EmilioPascual
    ```
  maintainer-Shide: |-
    ```{image} https://github.com/Shide.png?size=40px
    :alt: Shide
    :target: https://github.com/Shide
    ```
  maintainer-yajo: |-
    ```{image} https://github.com/yajo.png?size=40px
    :alt: yajo
    :target: https://github.com/yajo
    ```
---

# Sale Invoice Frequency

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:edc787b5d9f0a9a131d1a0cf4c8b4086d83347c1417f9f5eee13480aa69021d5
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module extends the functionality of sales to support group by
Invoicing frequency and to allow you to choose the right orders to
invoice based on the frequency defined on the customer. On the partner,
Invoicing frequency field is propagated to its children when changed.

**Table of contents**

```{contents}
:local: true
```

# Usage

To use this module, you need to:

1. Go to *Sales/Configuration/Invoicing frequency* and create your
   custom frequencies.
2. Set these frequencies in the customer form *Invoicing* tab.
3. When a sale is created, the Invoicing frequency of the field
   `partner_id` is propagated.
4. An user can change Invoicing frequency on sales and customers if has
   group `account.group_account_invoice`.
5. You can change Invoicing frequency on a sale on the *Other
   information* tab without changing the customer frequency.
6. When you want to invoice, group sales by Invoicing frequency and
   invoice it.
7. You can create a CRON for each frequency to automate invoicing
   action.

# Known issues / Roadmap

- Add an automation to auto-invoice orders. Now must be done grouping
  orders by invoicing frequency and invoice them manually.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_invoice_frequency%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Moduon

## Contributors

- Eduardo de Miguel ([Moduon](https://www.moduon.team/))
- Rafael Blasco ([Moduon](https://www.moduon.team/))

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

Current [maintainers](https://odoo-community.org/page/maintainer-role):

{{ maintainer-Shide }} {{ maintainer-yajo }} {{ maintainer-EmilioPascual }}

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_invoice_frequency) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_last_price_info

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_last_price_info
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_last_price_info
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Product Last Price Info - Sale

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:c83fb14c041c94bfb95a0e5a20a319a4e5de03b6d8d124a5342a4d7d83829dfc
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module adds the last sale info of the product. * Last Sale Price
\* Last Sale Date * Last Customer

**Table of contents**

```{contents}
:local: true
```

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_last_price_info%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- AvanzOSC
- Tecnativa

## Contributors

- Alfredo de la Fuente \<<mailto:alfredodelafuente@avanzosc.es>>
- Oihane Crucelaegui \<<mailto:oihanecrucelaegi@avanzosc.es>>
- Pedro M. Baeza \<<mailto:pedro.baeza@serviciosbaeza.com>>
- Ana Juaristi \<<mailto:anajuaristi@avanzosc.es>>
- Serpent Consulting Services Pvt. Ltd. \<<mailto:support@serpentcs.com>>
- Tharathip Chaweewongphan \<<mailto:tharathipc@ecosoft.co.th>>
- Ruchir Shukla \<<mailto:ruchir@bizzappdev.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_last_price_info) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_archive

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_archive
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_archive
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Order Archive

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:e714dac523c980fb55910799b1ec60b4fa7c166c213803e8adaafa99f860f688
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

On a system with a high volume of sales, the number of sale orders
displayed in the list view can become huge. This module allows to
archive Sale Orders that are in status Locked or Cancelled.

If a sale order is archived, it will be hidden from the sale orders list
view.

This module only depends on module sale, but it could be used in
combination with OCA module 'record_archiver' in order to automatically
archive old sale orders.

**Table of contents**

```{contents}
:local: true
```

# Installation

You need to install *sale_management* module for accessing the needed
menus.

# Usage

To archive sale orders, you need to:

1. Open the tree view of sale orders.
2. Select a sale order (in status Locked or Cancelled) you want to
   archive.
3. Click on Action > Archive. Confirm.
4. The sale order is now archived.

To unarchive sale orders, you need to:

1. Open the tree view of sale orders.
2. In the filter box select the Archived filter. The list of archived
   sale orders will be displayed.
3. Select the sale order (in status Locked or Cancelled) you want to
   restore to Active.
4. Click on the Action > Unarchive.
5. The sale order is now active.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_archive%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Onestein

## Contributors

- Andrea Stirpe \<<mailto:a.stirpe@onestein.nl>>

- Kinner Vachhani

- Ruchir Shukla \<<mailto:ruchir@bizzappdev.com>>

- [Heliconia Solutions Pvt. Ltd.](https://www.heliconia.io)

  - Bhavesh Heliconia

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_archive) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_disable_user_autosubscribe

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_disable_user_autosubscribe
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_disable_user_autosubscribe
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Order Disable User Autosubscribe

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:230426735112602aba241ad2031f7f1fe923324b688ff1ffd7b78a0ce1fa813e
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module removes the order's salesperson from default followers.

**Table of contents**

```{contents}
:local: true
```

# Known issues / Roadmap

- Make it generic, and move it in OCA/social

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_disable_user_autosubscribe%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Camptocamp SA

## Contributors

- Matthieu Mequignon \<<mailto:matthieu.mequignon@camptocamp.com>>

- [Trobz](https://trobz.com):

  - Nguyen Hoang Hiep \<<mailto:hiepnh@trobz.com>>
  - Do Anh Duy \<<mailto:duyda@trobz.com>>

## Other credits

The migration of this module from 13.0 to 14.0 was financially supported
by Camptocamp. The migration of this module from 14.0 to 18.0 was
financially supported by Camptocamp.

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_disable_user_autosubscribe) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_general_discount

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :alt: Production/Stable
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_general_discount
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_general_discount
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Order General Discount

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:dc77d9917dd2128ebbdc7d99dd2b878d5303e6b599da95e0b19d41a7a52973c2
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module allows to set a general discount in a sales order. This
general discount is set to each line order in the standard discount
field.

You can configure:

- a default general discount on customers
- On each product define if general discount is applied

**Table of contents**

```{contents}
:local: true
```

# Installation

You need to install sale_management module for accessing the needed
menus.

# Usage

To use this module, you need to:

1. Create a sale order and set a discount, this discount will be set in
   all lines.
2. You can set a discount in a partner.
3. On product you can define if you apply general discount on sale order
   line linked to that product

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_general_discount%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Tecnativa

## Contributors

- [Tecnativa](https://www.tecnativa.com):

  - Sergio Teruel \<<mailto:sergio.teruel@tecnativa.com>>
  - Stefan Ungureanu \<<mailto:stefan.ungureanu@tecnativa.com>>

- Raf Ven \<<mailto:raf.ven@dynapps.be>>

- Sudhir Arya \<<mailto:sudhir@erpharbor.com>>

- Heliconia Solutions Pvt. Ltd. \<<https://www.heliconia.io>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_general_discount) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_line_date

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_date
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_line_date
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Order Line Date

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:c8b8e3d7c77f60b0093bc4365565dd6c7965892ff5d1a2a82d1104c1f3d57590
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module adds a commitment date to each sale order line and propagate
it to stock moves and pickings. The commitment date of the wholesale
order is computed based on each sale order line date and the sale order
shipping policy. It can't be modified.

**Table of contents**

```{contents}
:local: true
```

# Usage

Create a Quotation or a Sales Order and it fills the requested date in
the sale order line

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_line_date%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- OdooMRP team
- AvanzOSC
- Serv. Tecnol. Avanzados - Pedro M. Baeza
- SprintIT Ltd.

## Contributors

- Oihane Crucelaegui \<<mailto:oihanecrucelaegi@avanzosc.es>>
- Esther Martín \<<mailto:esthermartin@avanzosc.es>>
- Pedro M. Baeza \<<mailto:pedro.baeza@tecnativa.com>>
- Ana Juaristi \<<mailto:anajuaristi@avanzosc.es>>
- Jordi Ballester \<<mailto:jordi.ballester@forgeflow.com>>
- Aaron Henriquez \<<mailto:ahenriquez@forgeflow.com>>
- Serpent Consulting Services Pvt. Ltd. \<<mailto:support@serpentcs.com>>
- Francesco Apruzzese \<<mailto:f.apruzzese@apuliasoftware.it>>
- Mykhailo Panarin \<<mailto:m.panarin@mobilunity.com>>
- Open-Net Sàrl \<<mailto:jae@open-net.ch>>
- Miquel Raïch \<<mailto:miquel.raich@forgeflow.com>>
- Moaad Bourhim \<<mailto:moaad.bourhim@gmail.com>>
- Bernat Puig \<<mailto:bernat.puig@forgeflow.com>>
- Nhan Tran \<<mailto:nhant@trobz.com>>
- Tatiana Deribina \<<mailto:tatiana.deribina@sprintit.fi>>

## Other credits

The migration of this module from 18.0 to 19.0 was financially supported
by SprintIT Ltd.

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_date) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_line_menu

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_menu
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_line_menu
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Order Line Menu

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:162e6b98ecb7b3713748854e6346c280023cb217acf19fb733891242c0db05e3
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

Adds a menu item and some views to navigate through Sale Order lines.

**Table of contents**

```{contents}
:local: true
```

# Usage

Menu option available at Sales > Orders > Order Lines.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_line_menu%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Open Source Integrators

## Contributors

- \`Open Source Integrators \<<https://opensourceintegrators.com>>\`:

  - Daniel Reis \<<mailto:dreis@opensourceintegrators.com>>
  - Freni Patel \<<mailto:fpatel@opensourceintegrators.com>>
  - Murtaza Mithaiwala \<<mailto:mmithaiwala@opensourceintegrators.com>>

- \`Moduon Team \<<https://moduon.team>>\`:

  - Eduardo de Miguel \<<mailto:edu@moduon.team>>
  - Emilio Pascual \<<mailto:emilio@moduon.team>>
  - Rafael Blasco \<<mailto:rafaelbn@moduon.team>>

- [Heliconia Solutions Pvt. Ltd.](https://www.heliconia.io)

  - Bhavesh Heliconia

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_menu) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_line_note

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_note
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_line_note
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# sale_order_line_note

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:296dfdfc6f30d5990a88bdd1d79d7fd8e9ecc3a6b2363d05946147cd2e285383
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module add the field note on the sale order line

**Table of contents**

```{contents}
:local: true
```

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_line_note%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Akretion

## Other credits

The migration of this module from 16.0 to 18.0 was financially supported
by Camptocamp.

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_note) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_line_price_history

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :alt: Production/Stable
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_price_history
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_line_price_history
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
  maintainer-CarlosRoca13: |-
    ```{image} https://github.com/CarlosRoca13.png?size=40px
    :alt: CarlosRoca13
    :target: https://github.com/CarlosRoca13
    ```
  maintainer-Shide: |-
    ```{image} https://github.com/Shide.png?size=40px
    :alt: Shide
    :target: https://github.com/Shide
    ```
---

# Sale order line price history

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:87e91d649b3d5d83cd86659aab139d13e59a27d93998ab00ecf184a966c5515a
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module extends the functionality of Sales to allow you to see the
price history of a product from a sale order line and set one of these
old prices in the sale order line.

**Table of contents**

```{contents}
:local: true
```

# Usage

To use this module, you need to:

1. Go to System Parameters and configure the
   `sale_order_line_price_history.order_line_limit` parameter to limit
   the number of Sale Order Lines to show on the Wizard.
2. Go to *Sales -> Quotations* and select a Quotation. Default is 20
   lines.
3. Click on the new clock button in one of the sale order lines.
4. A pop-up will open and you will see the *price history* for the
   product of the sale order line and for the customer of the sale
   order.
5. You can select other customer or leave it empty to see the price
   history for all customers.
6. You can also set the price of one of the price history lines in the
   sale order line. To do that, you have to open the price history line
   desired and click the smart button named *Set price*.

# Known issues / Roadmap

- A backend tour would be nice to have.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_line_price_history%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Tecnativa

## Contributors

- [Tecnativa](https://www.tecnativa.com):

  - Pedro M. Baeza
  - Ernesto Tejeda
  - David Vidal
  - Carlos Roca

- Serpent Consulting Services Pvt. Ltd. \<<mailto:support@serpentcs.com>>

- Dhara Solanki \<<mailto:dhara.solanki@initos.com>>

- Ruchir Shukla \<<mailto:ruchir@bizzappdev.com>>

- Eduardo de Miguel ([Moduon](https://www.moduon.team/))

- Sodexis Team \<<mailto:dev@sodexis.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

Current [maintainers](https://odoo-community.org/page/maintainer-role):

{{ maintainer-CarlosRoca13 }} {{ maintainer-Shide }}

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_price_history) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_line_sequence

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_sequence
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_line_sequence
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Order Line Sequence

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:1f4f0371b977c0b0bb62d6e8ddd3dfa9bc4f67f08a0e5691182f5d751823c28a
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

Displays the sequence of Sale order line and helps to maintain the
order. The line sequence number is also displayed in sale order reports.

**Table of contents**

```{contents}
:local: true
```

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_line_sequence%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- ForgeFlow
- Serpent CS

## Contributors

- ForgeFlow S.L. \<<mailto:contact@forgeflow.com>>

- Serpent Consulting Services Pvt. Ltd. \<<mailto:support@serpentcs.com>>

- Rattapong Chokmasermkul \<<mailto:rattapongc@ecosoft.co.th>>

- Marcin Chechłacz \<<mailto:marcin.chechlacz@braintec.com>>

- [Heliconia Solutions Pvt. Ltd.](https://www.heliconia.io)

  - Bhavesh Heliconia

## Other credits

### Images

- Odoo Community Association:
  [Icon](https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg).

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_sequence) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_line_tag

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_tag
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_line_tag
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
  maintainer-ckolobow: |-
    ```{image} https://github.com/ckolobow.png?size=40px
    :alt: ckolobow
    :target: https://github.com/ckolobow
    ```
  maintainer-dreispt: |-
    ```{image} https://github.com/dreispt.png?size=40px
    :alt: dreispt
    :target: https://github.com/dreispt
    ```
  maintainer-smaciaosi: |-
    ```{image} https://github.com/smaciaosi.png?size=40px
    :alt: smaciaosi
    :target: https://github.com/smaciaosi
    ```
---

# Sale Order Line Tag

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:9d72c80881f0d310fb4f20f5f52b30a4cf2112d63b59291dbdbbe7e12808e1ee
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module allows the user to tag sales order lines in order to
classify them.

**Table of contents**

```{contents}
:local: true
```

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_line_tag%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Open Source Integrators

## Contributors

- Samuel Macias \<<mailto:smacias@opensourceintegrators.com>>
- Alejandro Parrales \<<mailto:alejandro17parrales@gmail.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

Current [maintainers](https://odoo-community.org/page/maintainer-role):

{{ maintainer-smaciaosi }} {{ maintainer-dreispt }} {{ maintainer-ckolobow }}

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_line_tag) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_price_recalculation

---
substitutions:
  Sale order price recalculation: |-
    ```{image} https://raw.githubusercontent.com/sale_order_price_recalculation/static/description/sale_order_price_recalculation.drawio.png
    ```
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_price_recalculation
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_price_recalculation
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Price recalculation in sales orders

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:7bc387a6f34174481b664caab3e72b331dd395cfb62a3c7c15f2e7691030e71d
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module adds 2 buttons on sale orders (below sale order lines) that:

- Recalculates the prices of the order lines that contain a product in
  them.
- Reset product descriptions from current product information.

It is launched manually as a button to get the user to decide if they
want to recalculate prices when the pricelist is changed or, after
duplicating a sale order, wether to update sales information or not.

**Table of contents**

```{contents}
:local: true
```

# Installation

You need to install sale_management module for accessing the needed
menus.

# Usage

Inside a sale order, you can click on "Recalculate prices" to launch a
recalculation of all the prices of the lines, losing previous custom
prices.

The second "Reset descriptions" will get descriptions from products,
losing custom descriptions.

{{ Sale order price recalculation }}

# Known issues / Roadmap

- In a sale order with lot of lines, the recalculation may slow down,
  because sale general data (amount untaxed, amount taxed...) are
  recalculated for each line.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_price_recalculation%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- AvanzOSC
- Grupo Vermon
- Tecnativa

## Contributors

- Carlos Sánchez Cifuentes \<<mailto:csanchez@grupovermon.com>>

- Pedro M. Baeza \<<mailto:pedro.baeza@tecnativa.com>>

- Oihane Crucelaegui \<<mailto:oihanecrucelaegi@avanzosc.es>>

- Pierre Verkest \<<mailto:pverkest@anybox.fr>>

- Vicent Cubells \<<mailto:vicent.cubells@tecnativa.com>>

- David Vidal \<<mailto:david.vidal@tecnativa.com>>

- Duc, Dao Dong \<<mailto:duc.dd@komit-consulting.com>>
  (<https://komit-consulting.com>)

- Raf Ven \<<mailto:raf.ven@dynapps.be>>

- [Heliconia Solutions Pvt. Ltd.](https://www.heliconia.io)

  - Bhavesh Heliconia

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_price_recalculation) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_priority

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_priority
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_priority
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Order Priority

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:e43ac41173834880ae53be9a915b623d0a5ca5a971bb63f8cc901b592faa19ba
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module adds the field *Priority* in sale order lines and sale
orders: priority of the sale order is computed as the maximum of the
priorities of its lines, setting the priority in the order sets the
priority of all its lines accordingly.

When a picking is created as a result of sale order confirmation, the
created procurement inherits the priority of the order, then the stock
moves and the picking inherit the procurement's priority.

**Table of contents**

```{contents}
:local: true
```

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_priority%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Agile Business Group

## Contributors

- Simone Rubino \<<mailto:simone.rubino@agilebg.com>>

- George Daramouskas \<<mailto:gdaramouskas@therp.nl>>

- `360ERP <https://www.360erp.com>`:

  - Andrea Stirpe

- Alejandro Parrales \<<mailto:alejandro17parrales@gmail.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_priority) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_order_type

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_order_type
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_order_type
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Order Type

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:ab9a63d2a693db7dd21a938d66bbc264ad9204bb65d47e2d21ee8dea4233e542
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module adds a typology for the sales orders. In each different
type, you can define, invoicing and refunding journal, a warehouse, a
stock route, a sequence, the shipping policy, the invoicing policy, a
payment term, a pricelist and an incoterm.

You can see sale types as lines of business.

You are able to select a sales order type by partner so that when you
add a partner to a sales order it will get the related info to it.

**Table of contents**

```{contents}
:local: true
```

# Configuration

To configure Sale Order Types you need to:

1. Go to **Sales > Configuration > Sales Orders Types**
2. Create a new sale order type with all the settings you want

# Usage

1. Go to **Sales > Sales Orders** and create a new sale order. Select
   the new type you have created before and all settings will be
   propagated.
2. You can also define a type for a particular partner if you go to
   *Sales & Purchases* and set a sale order type.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_type%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Grupo Vermon
- AvanzOSC
- Tecnativa
- Agile Business Group
- Niboo

## Contributors

- [Vermon](http://www.grupovermon.com)

  - Carlos Sánchez Cifuentes \<<mailto:csanchez@grupovermon.com>>

- [AvanzOsc](http://avanzosc.es)

  - Oihane Crucelaegui \<<mailto:oihanecrucelaegi@avanzosc.es>>
  - Ana Juaristi \<<mailto:anajuaristi@avanzosc.es>>
  - Daniel Campos \<<mailto:danielcampos@avanzosc.es>>
  - Ainara Galdona \<<mailto:ainaragaldona@avanzosc.es>>

- [Agile Business Group](https://www.agilebg.com)

  - Lorenzo Battistini \<<mailto:lorenzo.battistini@agilebg.com>>

- [Niboo](https://www.niboo.be/)

  - Samuel Lefever \<<mailto:sam@niboo.be>>
  - Pierre Faniel \<<mailto:pierre@niboo.be>>

- [Tecnativa](https://www.tecnativa.com)

  - Pedro M. Baeza
  - David Vidal
  - Carlos Dauden
  - Sergio Teruel

- [Pesol](https://www.pesol.es)

  - Angel Moya Pardo \<<mailto:angel.moya@pesol.es>>
  - Antonio J Rubio Lorente \<<mailto:antonio.rubio@pesol.es>>

- Rattapong Chokmasermkul \<<mailto:rattapongc@ecosoft.co.th>>

- [Druidoo](https://www.druidoo.io)

  - Iván Todorovich \<<mailto:ivan.todorovich@druidoo.io>>

- [GSLab.it](https://www.gslab.it)

  - Giovanni Serra \<<mailto:giovanni@gslab.it>>

- Tharathip Chaweewongphan \<<mailto:tharathipc@ecosoft.co.th>>

- Isaac Gallart \<<mailto:igallart@puntsistemes.es>>

- Denis Rousse \<<mailto:denis.roussel@acsone.eu>>

Do not contact contributors directly about support or help with
technical issues.

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_order_type) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_partner_incoterm

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_partner_incoterm
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_partner_incoterm
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Default sales incoterm per partner

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:27b03c59c223dfbd7306d7bb187298f0170ee988f8f04479c320f62876d6f833
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module adds a field on the Sales & Purchases tab of the partner
form where you can register the default incoterms for new sales orders
for this customer.

A different incoterm can be set per contact within the same company.

When the partner is selected on a new quotation, the incoterm is
retrieved from the partner record.

**Table of contents**

```{contents}
:local: true
```

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_partner_incoterm%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Opener B.V.

## Contributors

- Stefan Rijnhart \<<mailto:stefan@opener.amsterdam>>
- Jim Hoefnagels \<<mailto:jim.hoefnagels@dynapps.be>>
- Reed Hayashikawa \<<mailto:rhayashikawa@opensourceintegrators.com>>
- Alejandro Padron \<<mailto:alejandro.padron@braintec.com>>
- Heliconia Solutions Pvt. Ltd. \<<https://www.heliconia.io>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_partner_incoterm) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_require_po_doc

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_require_po_doc
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_require_po_doc
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Orders Require PO or Sales Documentation

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:052259ef7b4b21d24ddfe11b9add85d6b2efd02d637eb34f079c209064c74f5d
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

The goal of this development is to create a field for validation to
notate which customers require a purchase order in order to create an
invoice.

**Table of contents**

```{contents}
:local: true
```

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_require_po_doc%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Open Source Integrators

## Contributors

- Daniel Reis \<<mailto:dreis@opensourceintegrators.com>>
- Chandresh Thakkar \<<mailto:cthakkar@opensourceintegrators.com>>
- Chau Le \<<mailto:chaulb@trobz.com>>

## Other credits

- Open Source Integrators \<<mailto:contact@opensourceintegrators.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_require_po_doc) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_stock_delivery_address

---
substitutions:
  Source Location: |-
    ```{image} https://raw.githubusercontent.com/OCA/sale-workflow/19.0/sale_stock_delivery_address/static/description/source_location.png
    ```
  Transfers: |-
    ```{image} https://raw.githubusercontent.com/OCA/sale-workflow/19.0/sale_stock_delivery_address/static/description/img_transfers_01.png
    ```
  Transfers 2: |-
    ```{image} https://raw.githubusercontent.com/OCA/sale-workflow/19.0/sale_stock_delivery_address/static/description/img_transfers_02.png
    ```
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :alt: Production/Stable
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_stock_delivery_address
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_stock_delivery_address
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
  partner_locations: |-
    ```{image} https://raw.githubusercontent.com/OCA/sale-workflow/19.0/sale_stock_delivery_address/static/description/partner_locations.gif
    ```
  rule: |-
    ```{image} https://raw.githubusercontent.com/OCA/sale-workflow/19.0/sale_stock_delivery_address/static/description/img_rule.png
    ```
  sale order destination address: |-
    ```{image} https://raw.githubusercontent.com/OCA/sale-workflow/19.0/sale_stock_delivery_address/static/description/sale_order_destination_address.gif
    ```
---

# Sale Stock Delivery Address

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:8d9a75838104d51596667e92c436e93dd49206bd5058b9b8d4fed98c66a5e571
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module allows to specify a different delivery address per sales
order line, splitting deliveries if needed. Also, you can specify
different stock locations associated to those addresses, then the sales
order procurements will be run from this location.

**Table of contents**

```{contents}
:local: true
```

# Usage

1. Activate the developer mode
2. Add different addresses to one partner {{ partner_locations }}
3. The rules associated with those destination locations should have the
   "Destination location origin from rule" set to True. When set to True
   the destination location of the stock.move will be the rule.
   Otherwise, it takes it from the picking type. {{ rule }}
4. When entering a sales order line specify a *Destination Address*.
   {{ sale order destination address }} The deliveries will be split with
   two different destination locations: {{ Transfers }}
5. Specify different stock locations associated to those addresses
   {{ Source Location }} The sales order procurements will be run from this
   location {{ Transfers 2 }}

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_stock_delivery_address%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- ForgeFlow

## Contributors

- Lois Rilo \<<mailto:lois.rilo@forgeflow.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_stock_delivery_address) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_stock_picking_blocking

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_stock_picking_blocking
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_stock_picking_blocking
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Stock Picking Blocking

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:b36d412db7c6b9b418de25161fa936858a3072a9b00d8bc29b3e80b77252f200
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module extends the functionality of sales to allow you to block the
creation of deliveries from a sales order and give a reason.

**Table of contents**

```{contents}
:local: true
```

# Configuration

To configure this module, you need to:

1. Go to 'Sales > Configuration > Sales Orders > Delivery Block Reason'.
2. Create the different reasons that can lead to block the deliveries of
   a sales order.
3. Add some users to the group 'Release Delivery Block in Sales Orders'.

Additionally, you can set a customer with a 'Default Delivery Block
Reason' policy to add that delivery block to his sales by default:

1. Go to 'Sales > Sales > Customers'.
2. In the 'Sales & Purchases' add a 'Default Delivery Block Reason'.
3. The 'Default Delivery Block Reason' will be added automatically when
   creating a new sales order for the customer.

You can also set a payment term with a 'Default Delivery Block Reason'
policy to add that delivery block to his sales by default (only if the
customer does not have one set), in a similar way to the customers:

#. Go to 'Invoicing > Configuration > Invoicing > Payment Terms'. #. Add
a 'Default Delivery Block Reason'. #. The 'Default Delivery Block
Reason' will be added automatically when creating a new sales order for
the payment term, in case the customer does not have one.

# Usage

To use this module, you need to:

1. Create a new sales order and provide a 'Delivery Block Reason'.
2. Confirm Sale (No delivery would be created).
3. Release Delivery Block when it is time to create the deliveries for
   the sales order.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_stock_picking_blocking%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- ForgeFlow

## Contributors

- Lois Rilo \<<mailto:lois.rilo@forgeflow.com>>
- Laura Cazorla \<<mailto:laura.cazorla@forgeflow.com>>
- Sudhir Arya \<<mailto:sudhir@erpharbor.com>>
- Julien Coux \<<mailto:julien.coux@camptocamp.com>>
- Nguyen Minh Chien \<<mailto:chien@trobz.com>>
- Vincent Van Rossem \<<mailto:vincent.vanrossem@camptocamp.com>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_stock_picking_blocking) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_stock_picking_note

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_stock_picking_note
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_stock_picking_note
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
  maintainer-EmilioPascual: |-
    ```{image} https://github.com/EmilioPascual.png?size=40px
    :alt: EmilioPascual
    :target: https://github.com/EmilioPascual
    ```
  maintainer-carlosdauden: |-
    ```{image} https://github.com/carlosdauden.png?size=40px
    :alt: carlosdauden
    :target: https://github.com/carlosdauden
    ```
  maintainer-chienandalu: |-
    ```{image} https://github.com/chienandalu.png?size=40px
    :alt: chienandalu
    :target: https://github.com/chienandalu
    ```
  maintainer-victoralmau: |-
    ```{image} https://github.com/victoralmau.png?size=40px
    :alt: victoralmau
    :target: https://github.com/victoralmau
    ```
---

# Sale Stock Picking Note

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:d0b4003bb87e8009432c912ba321ac84b398b900cdc7fca4ce4cfa430a989437
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module extends sales order to include both a external (customer)
and internal picking note that will be transferred to the picking.

**Table of contents**

```{contents}
:local: true
```

# Usage

1. Go to Sales > Orders > Customers.
2. Create new customer and set **Picking Internal Note** and **Picking
   Customer Comments** in *Sales & Purchase* tab.
3. Go to Sales > Orders > Orders.
4. Create new sale order with storable products and select customer
   created before.
5. Go to *Other information* tab.
6. Fields **Picking Internal Note** and **Picking Customer Comments**
   will be filled with values from customer.
7. Can update the **Picking Internal Note** and **Picking Customer
   Comments** you want to.
8. Confirm the Sale Order and go to the created picking.
9. On the "Comments" tab, you will see both the internal note and
   customer comments.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_stock_picking_note%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Tecnativa

## Contributors

- Tecnativa \<<https://www.tecnativa.com>>

  - Carlos Dauden
  - David Vidal
  - João Marques
  - Víctor Martínez

- Sudhir Arya \<<mailto:sudhir@erpharbor.com>>

- Emilio Pascual ([Moduon](https://www.moduon.team/))

- Rafael Blasco ([Moduon](https://www.moduon.team/))

- Gelo Joga ([Moduon](https://www.moduon.team/))

- [Binhex Systems Solutions](https://binhex.cloud/):

  - Deriman Alonso \<<mailto:d.alonso@binhex.cloud>>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

Current [maintainers](https://odoo-community.org/page/maintainer-role):

{{ maintainer-carlosdauden }} {{ maintainer-victoralmau }} {{ maintainer-chienandalu }} {{ maintainer-EmilioPascual }}

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_stock_picking_note) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_stock_reference_by_line

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :alt: Production/Stable
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_stock_reference_by_line
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_stock_reference_by_line
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Stock Reference by Line

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:d903147fac23969da3c283b32b90aa5b43bde16b6390e961f2984652ccac173e
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module was written to extend the functionality of stock references
(previously: procurement groups) created from a sale order

On itself, this module does nothing. It is a requirement for modules
that need to create a stock reference for each individual sale order
line.

This module was previously known as "Sale Procurement Group by Line"
(`sale_procurement_group_by_line`)

**Table of contents**

```{contents}
:local: true
```

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_stock_reference_by_line%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Camptocamp
- ForgeFlow
- Serpent Consulting Services Pvt. Ltd.
- SprintIT Ltd.

## Contributors

- Guewen Baconnier \<<mailto:guewen.baconnier@camptocamp.com>>
- Yannick Vaucher \<<mailto:yannick.vaucher@camptocamp.com>>
- Jordi Ballester \<<mailto:jordi.ballester@forgeflow.com>>
- Serpent Consulting Services Pvt. Ltd. \<<mailto:support@serpentcs.com>>
- Carmen Rondon Regalado \<<mailto:crondon@archeti.com>>
- Tatiana Deribina \<<mailto:tatiana.deribina@sprintit.fi>>

## Other credits

The migration of this module from 18.0 to 19.0 was financially supported
by SprintIT Ltd.

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_stock_reference_by_line) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.

---

### sale_substate

---
substitutions:
  badge1: |-
    ```{image} https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
    :target: https://odoo-community.org/page/development-status
    ```
  badge2: |-
    ```{image} https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: 'License: AGPL-3'
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    ```
  badge3: |-
    ```{image} https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :alt: OCA/sale-workflow
    :target: https://github.com/OCA/sale-workflow/tree/19.0/sale_substate
    ```
  badge4: |-
    ```{image} https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate
    :target: https://translation.odoo-community.org/projects/sale-workflow-19-0/sale-workflow-19-0-sale_substate
    ```
  badge5: |-
    ```{image} https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :alt: Try me on Runboat
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=19.0
    ```
---

# Sale Sub State

% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! This file is generated by oca-gen-addon-readme !!
% !! changes will be overwritten.                   !!
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% !! source digest: sha256:48a9440709aa258e19a4c780eecedf9d2a50337795c289eec261afb3caf55bbc
% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

{{ badge1 }} {{ badge2 }} {{ badge3 }} {{ badge4 }} {{ badge5 }}

This module allows to add a substate to sale order. For each sale order
state you can define a substate. With this module substates can be
defined allowing to extend the sales workflow. For example, you can add
substate "waiting for legal documents" if the order cannot be validated
without this document (sell a car for example).

**Table of contents**

```{contents}
:local: true
```

# Usage

1. Go to \*\* Settings > Technical > Sub State Configuration \*\* and
   Add "Base Substate".
   If necessary you can add "Target State values" (ex define a
   substate for "cancel" state). Substate sequence is very important.
2. Create a sale order and check if the substate are displayed on the
   header of form view. Check if you can't set substate defined for sale
   if sate is a quotation.

# Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/sale-workflow/issues).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_substate%0Aversion:%2019.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

# Credits

## Authors

- Akretion

## Contributors

- Mourad EL HADJ MIMOUNE \<<mailto:mourad.elhadj.mimoune@akretion.com>>

- Alexei Rivera \<<mailto:arivera@archeti.com>> (migration to 15.0)

- OERP Canada <https://www.oerp.ca/>:

  - Nishi Patel <mailto:np@oerp.ca>

## Maintainers

This module is maintained by the OCA.

```{image} https://odoo-community.org/logo.png
:alt: Odoo Community Association
:target: https://odoo-community.org
```

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the [OCA/sale-workflow](https://github.com/OCA/sale-workflow/tree/19.0/sale_substate) project on GitHub.

You are welcome to contribute. To learn how please visit <https://odoo-community.org/page/Contribute>.