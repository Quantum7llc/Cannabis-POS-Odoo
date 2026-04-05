# Purchase — RFQs, Purchase Orders & Vendor Bills

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

Purchase orders, RFQs, vendor bills, and purchase agreements. Covers approval workflows, landed costs, and vendor management. Use when configuring procurement or supplier integration.

---

# Purchase

**Odoo Purchase** helps keep track of purchase agreements, quotations, and purchase orders. Learn
how to monitor purchase tender, automate replenishment, and follow up on your orders.

> **Note:**
>
> - [Odoo Tutorials: Purchase](https://www.odoo.com/slides/purchase-23)

---

# Products

---

# Import vendor pricelist

Set vendor prices to auto-populate requests for quotations (RFQs) or purchase orders (POs) with the
unit price, once the product is added, which reduces errors and saves time.

In Odoo, vendor pricelists can be [added individually] on the
product form, or [imported in bulk], via an XLSX or CSV
file.

> **Warning:**
>
> Please review this [import guide](../../../essentials/export_import_data.html) before uploading
> vendor pricelists.

## On product form

To manually add the vendor price on the product form, go to the Purchase app ‣
Products ‣ Products, and click the desired product.

> **Note:**
>
> Product forms are accessible from multiple apps, such as **Sales**, **Inventory**, and
> **Manufacturing**.

In the Purchase tab of the product form, input the vendor and their price, to have this
information auto-populate on a request for quotation each time the product is listed.

> **Note:**
>
> [Vendor pricelist on product form](../manage_deals/rfq.html#purchase-manage-deals-vendor-pricelist)

![Vendor pricelist on product form.](../../../../_images/product-form-pricelist.png)

## Import vendor pricelist

To import vendor pricelists, ensure the XLSX or CSV file is accurately completed. The best way to
obtain a correctly formatted template, including product names, references, and vendor details, is
to first [export a pricelist] from the database.

Modify the exported file, as needed, then import it back into the Odoo database.

### Export pricelist

To export a pricelist, go to Purchase app ‣ Configuration ‣ Vendor Pricelists.

On the page, tick the checkbox(es) for the desired vendor pricelists.

Then, click the  Actions button that appears, and choose
Export from the drop-down menu.

![Show selected exported fields, with the Export button visible.](../../../../_images/export.png)

In the resulting pop-up window, fields listed under the Fields to export section are
included in the exported file. To add more fields, find the desired field in the
Available fields section, and click the  (plus) icon to the
right of the field.

> **Note:**
>
> To update to existing records, tick the I want to update data (import-compatible
> export) checkbox, and refer to the section on the [External ID] field.
>
> For details on commonly-used fields for importing vendor pricelists, see the [Common fields] section.

Select the desired Export Format: XLSX or CSV.

To save the selected fields as a template, click the Template field, and select
New template from the drop-down menu. Type the name of the new template, and click the
 (save) icon. After that, the template is a selectable option when
clicking the Template field.

Finally, click Export.

> **Note:**
>
> With [developer mode](../../../general/developer_mode.html#developer-mode) turned on, the column names of the exported file
> display the *field name* with the *technical name* in parenthesis.

> **Tip:**
>
> ![Exporting vendor pricelist.](../../../../_images/export-data.png)
>
>
> Export vendor pricelist in XLSX format. It includes Product Template and other
> fields in the Fields to export section.

#### External ID

*External ID* is a unique identifier used to update existing vendor pricelists. Without it, imported
records create new entries, instead of updating existing ones. Including this field in the XLSX or
CSV, indicates the line replaces an existing vendor pricelist in the Odoo database.

> **Tip:**
>
> ![Show 'Ready Mat' appear twice.](../../../../_images/duplicate-values.png)
>
>
> `Ready Mat` appears twice because the external ID was omitted during the price update from
> `$790` to `$780`.

To look-up the External ID for a vendor pricelist, tick the I want to update
data (import-compatible export) checkbox at the top of the Export Data pop-up window.

> **Note:**
>
> Selecting External ID from the Available fields section with the
> I want to update data (import-compatible export) checkbox ticked results in an export
> file with two columns containing the external ID.

#### Common fields

Below is a list of commonly-used fields when importing vendor pricelists:

Field name definitions

| Field name | Used for | Field in Odoo database | Technical name of field |
| --- | --- | --- | --- |
| Vendor | The only required field for creating a vendor pricelist record. This field specifies the vendor associated with the product. | Vendor field in the [vendor pricelist of the product form]. | `partner_id` |
| Product Template | The Odoo product the vendor pricelist entry is related to. | Product field in the vendor pricelist. | `product_tmpl_id` |
| Quantity | The minimum quantity required to receive the product at the specified price. | Quantity field in the vendor pricelist. (If not visible, enable it by clicking the  (adjust) icon, and tick the Quantity checkbox) | `min_qty` |
| Unit Price | The purchase price for the product from the vendor. | Price field in the vendor pricelist. | `price` |
| Lead Time | [Number of days](../../inventory/warehouses_storage/replenishment/lead_times.html#inventory-warehouses-storage-purchase-vendor-lt) before receiving the product after confirming a purchase order. | Lead Time field on the vendor pricelist. | `delay` |
| Sequence | Defines the order of vendors in the pricelist when multiple vendors are available. For example, if `Azure Interior` is listed first and Wood Corner second, their sequences would be `1` and `2`. | N/A | `sequence` |
| Company | Name of company the product belongs to. | Company field in the vendor pricelist. | `company_id` |
| [External ID] | Unique ID of a record used to update existing vendor pricelists. | N/A | `id` |

### Import records

With a template downloaded, fill out the XLSX or CSV file with the necessary information. After
inputting everything, import the file back into the Odoo database, by going to
Purchase app ‣ Configuration ‣ Vendor Pricelists.

On the page, click the  (gear) icon in the top-left corner. In the
drop-down menu that appears, click Import records.

Then, click Upload File in the upper-left corner, and after selecting the XLSX or CSV
file, confirm the correct fields, and click Import.

> **Note:**
>
> - [Export and import data](../../../essentials/export_import_data.html)
> - [Common fields]

![Upload file screen.](../../../../_images/supplier-pricelist-example.png)

#### Formatting import file

To understand how to format import files for vendor pricelists, consider the following example.

- `Storage Box` (Reference: `E-COM08`) is sold by `Wood Corner` for `$10`.
- `Large Desk` (Reference: `E-COM09`) has no records in the vendor pricelist.

An import file is created to do the following:

- Update the price for `Wood Corner` from `$10` to `$13`.
- Add pricelist for `Storage Box`: the vendor, `Ready Mat` intends to sell the product for `$14`.
- Add pricelist for `Large Desk`: vendor is `Wood Corner`, price is `$1299`.
- Add pricelist for `Large Desk`: vendor is `Azure Interior`, price is `$1399`.

Vendor pricelist data

| id | company\_id | delay | price | product\_tmpl\_id | sequence | partner\_id |
| --- | --- | --- | --- | --- | --- | --- |
| product.product\_supplierinfo\_3 | My Company (San Francisco) | 3 | 13.00 | [E-COM08] Storage Box | 4 | Wood Corner |
|  | My Company (San Francisco) | 3 | 14.00 | [E-COM08] Storage Box | 5 | Ready Mat |
|  | My Company (San Francisco) | 2 | 1299.00 | [E-COM09] Large Desk | 6 | Wood Corner |
|  | My Company (San Francisco) | 4 | 1399.00 | [E-COM09] Large Desk | 7 | Azure Interior |

> **Note:**
>
> The *technical field name* was used to create this information.

> **Note:**
>
> Download the sample files for reference:
>
> - [`Sample XLSX import file`](../../../../_downloads/54322bb572bfefb8d336adac3919288c/pricelist-example.xlsx)
> - [`Sample CSV import file`](../../../../_downloads/d233051feebacc1f52f8f43e2ac51f99/pricelist-example.csv)

---

# Configure reordering rules

For certain products, it is necessary to ensure that there is always a minimum amount available on
hand at any given time. Maintaining a minimum stock level ensures that businesses can meet customer
demand without delays, and keep operations running smoothly. It also helps buffer against supply
chain disruptions and unexpected spikes in demand. Inefficiencies may arise from inaccurate demand
forecasting, supply chain delays, and warehouse mismanagement, all of which can lead to increased
operational costs and wasted resources.

Keep highly demanded products in-stock at all times using reordering rules, that trigger a RFQ
(Request for Quotation) each time the forecasted stock quantities fall below the minimum.
RFQs generated from reordering rules have the vendor, price,
quantity needed to reorder, which makes things faster and more convenient.

> **Warning:**
>
> The **Inventory** app must be installed to use reordering rules, as it keeps track of stock
> quantity.

## Configure products for reordering

Products must be configured in a specific way before a reordering rule can be added to them.

Starting from the Inventory, Manufacturing,
Purchase, or Sales app, navigate to Products ‣
Products and then click New to make a new product. Alternatively, find a product that
already exists in the database and click into it’s product form.

Next, on the product form, enable reordering by ticking the Purchase checkbox
underneath the Product name field. Then, under the General Information tab,
set the Product Type to Goods. Finally, tick the checkbox labeled
Track Inventory, and select an [option](../../inventory/product_management/product_tracking.html) from the drop-down.

![Configure a product for reordering in Odoo.](../../../../_images/product-configured-for-reordering.png)

## Add a reordering rule to a product

After properly configuring a product, a reordering rule can be added to it by selecting the now
visible  Reordering Rules smart button at the top of that product’s
form, then clicking Create on the Reordering Rules dashboard.

> **Note:**
>
> If the  Reordering Rules smart button is not visible, click
> More.

Once created, the reordering rule can be configured to generate purchase orders automatically by
defining the following fields:

- Location specifies where the ordered quantities should be stored once they are
  received and entered into stock.
- Min Quantity sets the lower threshold for the reordering rule while Max
  Quantity sets the upper threshold. If the stock on hand falls below the minimum quantity, a new
  purchase order is then created to replenish it up to the maximum quantity.

  > > **Tip:**
  > >
  > > If Min Quantity is set to `5` and Max Quantity is set to `25` and the
  > > stock on hand falls to four, a purchase order is then created for 21 units of the product.
- Multiple Quantity can be configured so that products are only ordered in batches of a
  certain quantity. Depending on the number entered, this can result in the creation of a purchase
  order that would put the resulting stock on hand above what is specified in the Max
  Quantity field.

  > > **Tip:**
  > >
  > > If Max Quantity is set to `100` but Multiple Quantity is set to order
  > > the product in batches of `200`, a purchase order is then created for 200 units of the
  > > product.
- Unit specifies the unit of measurement by which the quantity is to be ordered. For
  discrete products, this should be set to `Units`. However, it can also be set to units of
  measurement like `Volume` or `Weight` for non-discrete products like water or bricks.

![Configure the reordering rule in Odoo.](../../../../_images/reordering-rule-configuration.png)
> **Note:**
>
> [Reordering rules](../../inventory/warehouses_storage/replenishment/reordering_rules.html)

## Manually trigger reordering rules using the scheduler

Reordering rules are automatically triggered by the scheduler, which runs once a day by default. To
trigger reordering rules manually, turn on developer mode, navigate to Inventory app
‣ Operations ‣ Procurement: Run Scheduler. On the pop-up window, confirm the manual action by
clicking Run Scheduler.

> **Note:**
>
> Manually triggering reordering rules will also trigger any other scheduled actions.

## Manage reordering rules

To manage the reordering rules for a single product, navigate to that product page’s form and select
the Reordering Rules smart button at the top of the form.

To manage all reordering rules for every product, go to Inventory app ‣ Operations
‣ Replenishment. From this dashboard, typical bulk actions in Odoo can be performed such as
exporting data or archiving rules that are no longer needed. As well, the Filters,
Group By or triple-dotted menu on the form are available to search for and/or organize
the reordering rules as desired.

---

# Temporary reordering rules

Some businesses require certain products to always have a minimum quantity of stock on-hand at any
given time. To avoid stock falling below a certain threshold, companies can create *reordering
rules* in Odoo to automate purchase orders for specific products.

Reordering rules keep the forecasted stock levels above a certain threshold, without exceeding a
specified upper limit, or maximum amount. When a product with a reordering rule falls below a
specified quantity, Odoo generates an order using the specified *route* (e.g. *Buy* or
*Manufacture*) to replenish the stock.

In certain cases, businesses might opt for *temporary reordering rules* when they do not want
specific products to be replenished automatically.

In Odoo, a “temporary” reordering rule is created in the replenishment dashboard when a product:

1. is configured with a *Buy* route
2. has no reordering rule configured
3. has `0` quantity in stock
4. is included in a sales order (SO).

This rule is deleted upon confirmation of the purchase order (PO) generated for the product.

> **Note:**
>
> - [Reordering rules](../../inventory/warehouses_storage/replenishment/reordering_rules.html)
> - [Configure reordering rules](reordering.html)

## Configuration

To configure a product that triggers temporary reordering rules when its stock reaches `0`, begin by
going to Inventory app ‣ Products ‣ Products, and click New.

> **Note:**
>
> The same configurations can also be made on an existing product, by going to
> Inventory app ‣ Products ‣ Products, and selecting an existing product.

On the product form, enter the product name, and ensure the Can be Sold and
Can be Purchased options are enabled, located beneath the Product Name
field.

Then, set the Product Type to `Storable Product`, under the General
Information tab.

Next, click the Purchase tab, and under Vendor, click Add a line
to select a vendor from the drop-down menu. Then, set a purchase price under Price.

> **Warning:**
>
> A vendor **must** be set for temporary reordering rules to work. While a PO can still be created automatically, attempting to replenish the product from the
> Replenishment dashboard in the *Inventory* app triggers a warning to add a vendor on
> the product form.
>
> ![Warning pop-up upon clicking to replenish product with no set vendor.](../../../../_images/temporary-reordering-warning-popup.png)

Before creating a SO for the product, ensure the On Hand smart
button on the product form reads `0.00 Units`. Then, ensure that the Reordering Rules
smart button reads `0`, indicating there are no rules applied to this product.

![Product form smart button row displaying reordering rules and on hand buttons.](../../../../_images/temporary-reordering-smart-buttons.png)

## Trigger temporary reordering rule

To trigger a temporary reordering rule, create a new sales order for a product by navigating to
Sales app ‣ New.

Then, add a customer in the Customer field, and click Add a product under
the Product column in the Order Lines tab. Next, select the desired product
from the drop-down menu. Lastly, Confirm the SO.

![Sales order for product with no set reordering rules.](../../../../_images/temporary-reordering-sales-order.png)

## Check replenishment report

To see the temporary reordering rule created for the out-of-stock product included in the sales
order, navigate to Inventory app ‣ Operations ‣ Replenishment. Doing so opens
the Replenishment dashboard.

On this dashboard, locate the product for which the temporary reordering rule was created. On its
product line, its On Hand quantity, negative Forecast quantity, *Buy*
Route, and To Order quantity to replenish can be seen.

Additionally, two replenishment options are located to the far-right of the row: Order
Once and Automate.

![Replenishment report displaying temporary reordering rule and options.](../../../../_images/temporary-reordering-replenishment-dashboard.png)

To use the one-time, temporary reordering rule, click Order Once. This action triggers a
confirmation pop-up window in the top-right corner, reading The following replenishment
order has been generated, along with a new purchase order number.

> **Note:**
>
> Once the purchase order has been generated after clicking Order Once, refresh the
> page. The temporary reordering rule for the product no longer appears in the
> Replenishment dashboard.

## Complete purchase order

To view the purchase order created from the Replenishment dashboard, navigate to the
Purchase app, and select the generated PO from the
Requests for Quotation overview.

From here, click Confirm Order, then click Receive Products. Finally, click
Validate to complete the purchase order.

![Purchase order for product ordered with temporary reordering rule.](../../../../_images/temporary-reordering-purchase-order.png)

Now, the original sales order can be delivered and invoiced.

> **Note:**
>
> Once the SO is delivered and invoiced, ensure there are no reordering rules
> on the product form.
>
> Go to Inventory app ‣ Products ‣ Products, select the product, and confirm
> that the Reordering Rules smart button displays `0`.

---

# Manage deals

---

# Requests for quotation

Odoo’s requests for quotation (RFQs) feature in the **Purchase** app standardizes ordering products
from multiple vendors with varying prices and delivery times.

RFQs are documents companies send to vendors requesting product pricing. In Odoo, once the vendor
approves the RFQ, the purchase order (PO) is confirmed to align on lead times and pricing.

## Configuration

### Product

To auto-populate product information and prices on an RFQ, configure products by going to
Purchase app ‣ Products ‣ Products. Select an existing product, or create a new
one by selecting New. Doing so opens the product form, where sales and purchasing data
can be configured.

To configure purchasable products, tick the Purchase checkbox, under the product name.
Next, go to the Inventory tab, and enable the Buy route.

> **Warning:**
>
> The Inventory tab and routes are only visible if using the [Inventory app](../../inventory.html).

> **Note:**
>
> [Configure product types and track quantities](../../inventory/product_management/configure.html)

![Required configuration for purchasable products.](../../../../_images/product-vendor-pricelist-config.png)

### Vendor pricelist

In the Purchase tab of the product form, click Add a line to input the
vendor and their price, to have this information auto-populate on an RFQ each time the product is
listed.

> **Note:**
>
> [Import vendor pricelist](../products/pricelist.html)

Default columns include Quantity, Unit Price, and Delivery Lead
Time, but other columns like, Vendor Product Code or Discount (%), can also
be enabled.

To enable or disable columns, click the  (additional options)
icon on the right side of the header row to reveal a drop-down menu of additional columns that can
be added (or removed) from the Purchase tab.

> **Note:**
>
> Alternatively, prices and delivery lead times for existing products can be added by going to
> Purchase app ‣ Configuration ‣ Vendor Pricelists. Click New in
> the top-left corner. In the Vendor section of the pricelist form that appears, add
> the product information as it pertains to the vendor.

## Order products

With products and prices configured, follow these steps to create and send RFQs to make purchases
for the company.

### RFQ dashboard

To get started, navigate to Purchase app ‣ Orders ‣ Requests for Quotation.

The Requests for Quotation dashboard displays an overview of the company’s RFQs,
POs, and their status. The top of the screen breaks down all RFQs in the company, as well as
individual ones (where the user is the buyer) with a summary of their status.

The top-right corner also provides a report of the company’s recent purchases by total value, lead
times, and number of RFQs sent.

Additionally, the dashboard includes buttons for:

- To Send: orders in the RFQ stage that have not been sent to the vendor.
- Waiting: RFQs that have been sent by email, and are waiting on vendor confirmation.
- Late: RFQs or POs where the Order Deadline has passed.

![RFQ dashboard with orders and order statuses.](../../../../_images/rfq-dashboard.png)

In addition to view options, the Requests for Quotation dashboard provides
Filters and Group By options, accessible via the search bar drop-down menu.

> **Note:**
>
> [Search, filter, and group records](../../../essentials/search.html)

### Create a new RFQ

To create a new RFQ, click the New button on the top-left corner of the
Requests for Quotation dashboard to reveal a new PO form.

Start by assigning a Vendor.

The Vendor Reference field points to the sales and delivery order numbers sent by the
vendor. This comes in handy once products are received, and the PO needs to be matched to the
delivery order.

With the [Purchase Agreements feature](blanket_orders.html) activated, the Blanket
Order field appears, referring to long-term purchase agreements on recurring orders with set
pricing. To view and configure blanket orders, head to Purchase app ‣ Orders ‣
Purchase agreements.

> **Warning:**
>
> The Purchase agreements view only appears if the Blanket Order setting is
> enabled. To do so, navigate to Purchase app ‣ Configuration ‣ Settings, then
> tick the Blanket Orders checkbox.

Next, configure an Order Deadline, which is the date by which the vendor must confirm
their agreement to supply the products.

> **Note:**
>
> After the Order Deadline is exceeded, the RFQ is marked as late, but the products
> can still be ordered.

Expected Arrival is automatically calculated based on the Order Deadline and
vendor lead time. Tick the checkbox for Ask confirmation to ask the vendor to confirm
the shipping date by email.

With the [Storage Locations feature](../../inventory/warehouses_storage/inventory_management/use_locations.html) activated, the
Deliver to field appears, which specifies which warehouse operation (set in the
**Inventory** app) is used to receive the shipment.

Select the receiving warehouse address here, or select Dropship to indicate that this
order is to be shipped directly to the end customer. When Dropship is selected, the
Dropship address field is enabled. Contact names auto-populate here from the
**Contacts** app.

> **Warning:**
>
> The Dropship options only appear if the Dropshipping setting is enabled
> in the **Inventory** app. To do so, navigate to Inventory app ‣ Configuration
> ‣ Settings, then tick the Dropshipping checkbox.

> **Note:**
>
> To create RFQs using different currencies, each currency needs to be enabled in the
> **Invoicing** app settings. See [Foreign currencies](../../../sales/sales/products_prices/prices/currencies.html) to
> learn more.

#### Products tab

In the Products tab, add the products to be ordered. Click Add a product,
and type in the product name, or select the item from the drop-down menu.

To create a new product and add it, type the new product name in the Product column,
select Create [product name] from the resulting drop-down menu and manually add the unit
price. Alternatively, select Create and edit… to be taken to the product form for that
new item.

Catalog can also be selected to navigate to a product menu from the chosen vendor. From
here, products can be added to the cart.

> **Note:**
>
> To make adjustments to products and prices, access the product form by clicking the
>  (right arrow) icon that becomes available upon hovering over
> the Product name.

### Send the RFQ

Clicking Send by Email reveals a Compose Email pop-up window, with a
Purchase: Request for Quotation template loaded, ready to send to the vendor’s email
address (configured in the **Contacts** app).

After crafting the desired message, click Send. Once sent, the RFQ moves to the
RFQ Sent stage.

Clicking Print RFQ downloads a PDF of the RFQ.

> **Note:**
>
> [Contacts](../../../essentials/contacts.html)

### Confirm order

Clicking Confirm Order directly transforms the RFQ into an active PO.

> **Note:**
>
> Odoo tracks communications on each order through the chatter of the PO form. This shows the
> emails sent between the user and the contact, as well as any internal notes and activities.
> Messages, notes, and activities can also be logged on the chatter.

Once an RFQ is confirmed, it creates a PO.

On the new PO, the Order Deadline field changes to Confirmation Date,
which displays the date and time the user confirmed the order.

Depending on the user’s chosen configuration in the **Purchase** app settings, a *vendor bill* is
created once products have been ordered or received. For more information, refer to the
documentation on [managing vendor bills](manage.html).

> **Note:**
>
> After an order is placed, clicking Receive Products records the reception of new
> products into the database.

> **Note:**
>
> With the **Inventory** app installed, confirming a PO automatically creates a receipt document,
> with the product information and expected arrival dates automatically populated.

> **Note:**
>
> [Manage vendor bills](manage.html)

---

# Blanket orders

Blanket orders are long-term purchase agreements between a company and a vendor to deliver products
on a recurring basis with predetermined pricing.

Blanket orders are helpful when products are consistently purchased from the same vendor, but in
different quantities, and at different times.

By simplifying the ordering process, blanket orders not only save time, they also save money, since
they can be advantageous when negotiating bulk pricing with vendors.

## Create a new blanket order

To create blanket orders, enable the *Purchase Agreements* feature from the *Purchase* app settings.
Navigate to Purchase app ‣ Configuration ‣ Settings, and under the
Orders section, click the checkbox for Purchase Agreements. Then click
Save to implement the changes.

> **Note:**
>
> In addition to creating blanket orders, the *Purchase Agreements* setting also allows users to
> create alternative requests for quotation (RfQs).

![Purchase Agreements enabled in the Purchase app settings.](../../../../_images/blanket-orders-enabled-setting.png)

To create a blanket order, go to Purchase app ‣ Orders ‣ Purchase Agreements,
and click New. This opens a new purchase agreement form.

Configure the following fields in the new purchase agreement form to establish predetermined rules
for the recurring long-term agreement:

- Vendor: the supplier to whom this agreement is tied, either once or on a recurring
  basis. The vendor can be selected directly from the drop-down menu next to this field.
- Buyer: the user assigned to this specific blanket order. By default, this is the user
  who created the agreement; the user can be changed directly from the drop-down menu next to this
  field.
- Agreement Type: the type of purchase agreement this blanket order is classified as.
  Use the drop-down menu to choose Blanket Order if not already selected.
- Currency: the agreed-upon currency to be used for this exchange. If multiple
  currencies have been activated in the database, the currency can be changed from the drop-down
  menu next to this field.
- Agreement Validity: the date range this agreement should be valid for. If this blanket
  order should not expire, leave this field blank.
- Reference: the source purchase order (PO) that this blanket order is tied to. If this
  blanket order should not be tied to any existing PO, leave this field blank.
- Operation Type: the operation type that should be applied to this order once it is
  delivered.
- Company: the company assigned to this specific blanket order. By default, this is the
  company that the user creating the blanket order is listed under. If the database is not a
  multi-company database, this field **cannot** be changed, and defaults to the only company listed
  in the database.

![New blanket order purchase agreement with added products.](../../../../_images/blanket-orders-new-agreement.png)

Once all relevant fields have been filled out, click Add a line to add products under
the Product column. Then, in the Quantity column, change the quantity of
each product, and set a price in the Unit Price column.

> **Warning:**
>
> When adding products to a new blanket order, the pre-existing prices of products are not
> automatically added to the product lines. Instead, the prices **must** be manually assigned, by
> changing the value in the Unit Price column to an agreed-upon price with the listed
> vendor. Otherwise, the price will remain `0`.

Click Confirm to save this new purchase agreement.

Once confirmed, the blanket order’s stage changes from Draft to Confirmed,
meaning this agreement can be selected and used when creating new RfQs.

> **Note:**
>
> After creating and confirming a blanket order, products, quantities, and prices can still be
> edited, added, and removed from the purchase agreement.

## Create a new RfQ from the blanket order

After confirming a blanket order, new quotations can be created directly from the blanket order
form. RfQs using this form are pre-populated with information based on the rules set in the form.
The total quantities of products ordered through linked RfQs are automatically updated in the
Ordered field on the agreement.

Additionally, new quotations are automatically linked to this blanket order form, via the
RFQs/Orders smart button at the top-right of the form.

To create a new quotation from the blanket order form, click the New Quotation button.
This opens a new RfQ, that is pre-populated with the correct information, depending on the
settings configured on the blanket order form.

From the new RfQ form, click Send by Email to compose and send an email to the listed
vendor. Click Print RFQ to generate a printable PDF of the quotation; or, once ready,
click Confirm Order to confirm the PO.

![New quotation with copied products and rules from blanket order.](../../../../_images/blanket-orders-new-quotation.png)

Once the PO has been confirmed, click back to the blanket order form (via the breadcrumbs, at the
top of the page). From the blanket order form, there is now one RfQ listed in the
RFQs/Orders smart button at the top-right of the form. Click the RFQs/Orders
smart button to see the PO that was just created.

![RFQs and Orders smart button from blanket order form.](../../../../_images/blanket-orders-rfq-smart-button.png)

## Replenishment

Once a blanket order is confirmed, a new vendor line is added under the Purchase tab of
the products included in the order.

This makes blanket orders useful with [automated replenishment](../products/reordering.html), because information about the Vendor,
Price, and the Agreement are referenced on the vendor line. This information
dictates when, where, and at what price the product should be replenished.

![Product form with replenishment agreement linked to blanket order.](../../../../_images/blanket-orders-product-form.png)
> **Note:**
>
> [Call for tenders](calls_for_tenders.html)

---

# Call for tenders

Sometimes, companies might want to invite vendors to submit offers for similar goods or services all
at once. This helps companies select the cheapest, fastest vendors for their specific business
needs.

In Odoo, this can be done by creating alternative requests for quotation (RfQs) for different
vendors. Once a response is received from each vendor, the product lines from each RfQ can be
compared, and a decision can be made for which products to purchase from which vendors.

> **Note:**
>
> Sometimes referred to as a *call for tender*, this process is primarily used by organizations in
> the public sector, who are legally bound to use it when making a purchase. However, private
> companies can also use alternative RfQs to spend money efficiently.

## Configuration

To create alternative RfQs, the *Purchase Agreements* feature **must** be enabled in the
*Purchase* app settings. To enable the feature, navigate to Purchase app ‣
Configuration ‣ Settings. Under the Orders section, click the checkbox for
Purchase Agreements.

Then, click Save to apply the change.

![Purchase Agreements enabled in the Purchase app settings.](../../../../_images/calls-for-tenders-enabled-setting.png)

## Create an RfQ

To create a new RfQ, follow the instructions in the [Requests for quotation](rfq.html) documentation.

> **Note:**
>
> [Odoo Tutorial: Purchase Basics and Your First Request for Quotation](https://www.youtube.com/watch?v=o_uI718P1Dc)

## Create alternative RfQs

Once a PO is created and sent to a vendor, alternative RfQs can be created for additional
vendors to compare prices, delivery times, and other factors, to help make a decision for the order.

To create alternative RfQs from the original, click the Alternatives tab. Then, click
Create Alternative. When clicked, a Create alternative pop-up window
appears.

![Calls for tenders pop-up to create alternative quotation.](../../../../_images/calls-for-tenders-create-alternative.png)

From this window, select an alternative vendor from the drop-down menu next to the
Vendor field, to whom the alternative quotation is assigned.

Next to this, there is a Copy Products checkbox that is selected by default. When
selected, the product quantities of the original RfQ are copied over to the alternative. For this
first alternative quotation, leave the checkbox checked. Once finished, click Create
Alternative. This opens a new RfQ form.

Since the Create Alternative checkbox was left checked, the new form is already
pre-populated with the same products, quantities, and other details as the previous, original RfQ.

> **Note:**
>
> When the Copy Products checkbox is selected while creating an alternative quotation,
> additional products do **not** need to be added, unless desired.
>
> However, if a chosen vendor is listed in the Vendor column under a specific product
> form included in the order, the values set on the product form carry over to the RfQ, and
> **must** be changed manually, if necessary.

Once ready, create a second alternative quotation by clicking the Alternatives tab,
followed by Create Alternative.

This opens the Create alternative pop-up window. Once again, choose a different vendor
from the drop-down menu next to Vendor. For this particular RfQ, however, *uncheck*
the Copy Products checkbox. Doing so removes all products on the new alternative RfQ,
leaving it blank. The specific products which should be ordered from this particular vendor can be
added in as needed.

Once ready, click Create Alternative.

> **Note:**
>
> If an alternative quotation should be removed from the Alternatives tab, they can be
> individually removed by clicking on the X (remove) icon at the end of their row.

This creates a third, new RfQ. But, since the product quantities of the original RfQ were
**not** copied over, the product lines are empty, and new products can be added as needed by
clicking Add a product, and selecting the desired products from the drop-down menu.

Once the desired number of specific products are added, click Send by Email.

![Blank alternative quotation with alternatives in breadcrumbs.](../../../../_images/calls-for-tenders-blank-quotation.png)

This opens a Compose Email pop-up window, wherein the message to the vendor can be
customized, and attachments can be added, if necessary. Once ready, click Send.

From this newest form, click the Alternatives tab. Under this tab, all three RfQs can
be seen in the Reference column. Additionally, the vendors are listed under the
Vendor column, and the order Total (and Status) of the orders
are in the rows, as well.

The date in the Expected Arrival column is calculated for each vendor, based on any
pre-configured lead times in the vendor and product forms.

## Link new RfQ to existing quotations

Even if a quotation is not created directly from the Alternatives tab of another RfQ,
it can still be linked to existing RfQs.

To do that, begin by creating a new RfQ. Navigate to Purchase app ‣ New. Fill
out the RfQ, according to the [previous instructions].

Then, once ready, click the Alternatives tab. Since this new RfQ was created
separately, there are no other orders linked yet.

However, to link this RfQ with existing alternatives, click Link to Existing RfQ on
the first line in the Vendor column.

![Pop-up to link new quotation to existing RFQs.](../../../../_images/calls-for-tenders-link-rfq-popup.png)

This opens an Add: Alternative POs pop-up window. Select the desired previously-created
RfQs, and click Select. All of these orders are now copied to this RfQ, and can be
found under the Alternatives tab.

> **Note:**
>
> If a large number of POs are being processed, and the previous POs can’t be located, click
> the  (chevron) icon to the right of the search bar, at the top
> of the pop-up window.
>
> Then, under the Group By section, click Vendor. Vendors are displayed in
> their own nested drop-down lists, and each vendor’s list can be expanded to view open POs for
> that vendor.

## Compare product lines

Alternative RfQs can be compared side-by-side, in order to determine which vendors offer the best
deals on the products included in the orders.

To compare alternative RfQs, navigate to the Purchase app, and select one of the
previously-created RfQs.

Then, click the Alternatives tab to see all linked RfQs. Next, under the
Create Alternative option, click Compare Product Lines. This navigates to
the Compare Order Lines page.

![Compare Product Lines page for alternative RFQs.](../../../../_images/calls-for-tenders-compare-products.png)

The Compare Order Lines page, by default, groups by Product. Each product
included in any of the RfQs is displayed in its own nested drop-down list, and features all of the
PO numbers in the Reference column.

> **Note:**
>
> To remove product lines from the Compare Order Lines page, click Clear at
> the far-right end of that product line’s row.
>
> Doing so removes this specific product as a selectable option from the page, and changes the
> Total price of that product on the page to `0`.
>
> Additionally, on the RfQ form, in which that product was included, its ordered quantity is also
> changed to `0`.

Once the best offers have been identified, individual products can be selected by clicking the
Choose button at the end of each corresponding row.

Once all desired products have been chosen, click Requests for Quotation (in the
breadcrumbs, at the top of the page) to navigate back to an overview of all RfQs.

## Cancel (or keep) alternatives

Once the desired products have been chosen from the Compare Order Lines page, the
remaining RfQs, from which no products were chosen, can be cancelled.

The cost in the Total column for each product that wasn’t chosen is automatically set to
`0`, indicated at the far-right of each corresponding row.

Although they haven’t been cancelled yet, this indicates that each of those orders can be cancelled
without having an effect on the other live orders, once those orders have been confirmed.

![Cancelled quotations in the Purchase app overview.](../../../../_images/calls-for-tenders-zero-total.png)

To confirm an RfQ for which products were selected, click into an RfQ, and click
Confirm Order.

This causes a What about the alternative Requests for Quotations? pop-up window
to appear.

To view a detailed form of one of the RfQs listed, click the line item for that quotation. This
opens an Open: Alternative POs pop-up window, from which all details of that particular
RfQ can be viewed.

Once ready, click Close to close the pop-up window.

In the What about the alternative Requests for Quotations? pop-up window, two options
are presented: Cancel Alternatives and Keep Alternatives.

If this PO should **not** be confirmed, click Discard.

Selecting Cancel Alternatives automatically cancels the alternative RfQs. Selecting
Keep Alternatives keeps the alternative RfQs open, so they can still be accessed, if
any additional product quantities need to be ordered later.

Once all products are ordered, select Cancel Alternatives from whichever PO
is open at that time.

![Keep or cancel pop-up for alternative RFQs.](../../../../_images/calls-for-tenders-keep-or-cancel.png)

Finally, using the breadcrumbs at the top of the page, click Requests for Quotation to
navigate back to an overview of all RfQs.

The cancelled orders can be seen, greyed out and listed with a Cancelled status, under
the Status column at the far-right of their respective rows.

Now that all product quantities have been ordered, the purchase process can be completed, and the
products can be received into the warehouse.

> **Note:**
>
> [Blanket orders](blanket_orders.html)

---

# Purchase templates

*Purchase templates* are an agreement type that allow for the repeated creation of requests for
quotations (RFQs) for recurring purchases. Products can then be added and quantities can be changed,
as needed. Purchase templates can be used for multiple vendors, saving time and simplifying the RFQ process.

Purchase templates differ from *blanket orders* in that a [blanket order](blanket_orders.html) is a large order
split into several deliveries, therefore all RFQs must be for the same vendor. Purchase templates can be
replicated for multiple vendors, and can copy over quantities, which is useful when placing frequent
orders.

## Configuration

First, navigate to Purchase app ‣ Configuration ‣ Settings. Under the
Orders section, tick the Purchase Agreements checkbox. Click
Save to save the changes.

![The Purchase agreements setting in the Purchase app.](../../../../_images/purchase-agreements-setting.png)

## Create a new template

Navigate Purchase app ‣ Orders ‣ Purchase Agreements and click New.

Select a Vendor from the drop-down list.

> **Note:**
>
> To make this template available to use with multiple vendors, leave the Vendor field
> blank.

In the Agreement Type field, select Purchase Template from the drop-down.

Confirm the information in the remaining fields is correct, or update as needed.

On the Products tab, click Add a line, and select the desired product.
Update the Quantity, and set the Unit Price.

> **Warning:**
>
> When adding products to a new blanket order, the pre-existing prices of products are not
> automatically added to the product lines. Instead, the prices **must** be manually assigned, by
> changing the value in the Unit Price column to an agreed-upon price with the listed
> vendor. Otherwise, the price will remain `0`.

After adding all necessary products, click Confirm.

### Create a new RFQ from a purchase template

After confirming a purchase template, new quotations can be created directly from the purchase template form. RFQs using
this form are pre-populated with information based on the rules set in the form. Additionally, new
quotations are automatically linked to this purchase template form, via the
RFQs/Orders smart button at the top of the form.

To [create a new quotation](rfq.html#purchase-manage-deals-create-new-rfq), click New
Quotation. This opens a new RFQ, that is pre-populated with the correct information, depending on
the settings configured on the purchase template form.

If there was no vendor identified on the purchase template, choose a Vendor from the drop-down list.
Products can be added to the RFQ by clicking Add a product in the Products
tab. To remove a product, click the  (trash) icon at the far-right of
the product line.

From the new RFQ form, click Send by Email to compose and send an email to the listed
vendor. Click Print RFQ to generate a printable PDF of the quotation; or, once ready,
click Confirm Order to confirm the purchase order.

After confirming the order, return to the purchase template via the breadcrumbs. The
RFQs/Orders smart button has been updated to list the confirmed order.

![The RFQ smart button on a purchase template.](../../../../_images/rfq-smart-button.png)

---

# Control policies

In Odoo’s **Purchase** app, the *Control Policy* determines the quantities billed by vendors on
every purchase order (PO). For example, choosing *On ordered quantities* means the bill is based on
ordered items, even if they have not been received yet.

The control policy is selected on the *Product* record.

## Configuration

To configure the control policy for a product, navigate to Purchase app ‣ Products
‣ Products, then click on a product record to open it. Click to the Purchase tab.
Scroll to the Vendor Bills section. Under Control Policy, tick the radio
button for either On ordered quantities or On recieved quantities.

- On ordered quantities: Creates a vendor bill as soon as a PO is confirmed. The
  products and quantities in the PO are used to generate a draft bill.
- On received quantities: A bill is created only *after* part of the total order has
  been received. The products and quantities received are used to generate a draft bill. An error
  message appears if creation of a vendor bill is attempted without receiving anything.

The default control policy for a product is determined by the Product Type:

- **Services**: The default control policy is *On ordered quantities*.
- **Goods**: The default control policy is *On delivered quantities*

## Pay vendor bills with 3-way matching

The *3-way matching* feature ensures vendor bills are only paid once some, or all, of the products
included in the PO have been received.

To activate *3-way matching*, navigate to Purchase app ‣ Configuration ‣
Settings, and scroll down to the Invoicing section. Then, tick the checkbox for
3-way matching to enable the feature, and click Save.

![Enabled 3-way matching feature in Purchase app settings.](../../../../_images/control-bills-three-way-matching.png)

When *3-way matching* is enabled, vendor bills display a Should Be Paid field under the
Other Info tab. When a new vendor bill is created, the field is set to Yes,
since a bill **cannot** be created until at least some of the products included in a PO have been
received.

To create a vendor bill from a PO, navigate to Purchase app ‣ Orders ‣
Purchase Orders. From the Purchase Orders page, select the desired PO from the list.
Then, click Create Bill. Doing so opens a new draft Vendor Bill form, in the
Draft stage. Click the Other Info tab, and locate the Should Be
Paid field.

> **Warning:**
>
> The PO selected from the list **must not** be billed yet, or an Invalid Operation
> pop-up window appears.
>
> ![Invalid Operation pop-up window for billed Purchase Order.](../../../../_images/control-bills-invalid-operation.png)

Click the drop-down menu next to Should Be Paid to view the available options:
Yes, No, and Exception.

![Should Be Paid field status on draft vendor bill.](../../../../_images/control-bills-should-be-paid.png)
> **Note:**
>
> If the total quantity of products from a PO has not been received, Odoo only includes the
> products that *have* been received in the draft vendor bill.

Draft vendor bills can be edited to increase the billed quantity, change the price of the products
in the bill, and add additional products to the bill.

If the draft bill’s information is changed, the Should Be Paid field status is set to
Exception. This means that Odoo notices the discrepancy, but does not block the changes
or display an error message, since there might be a valid reason for making changes to the draft
bill.

To process the vendor bill, select a date in the Bill Date field, and click
Confirm, followed by Register Payment.

This opens a Register Payment pop-up window. From this window, accounting information is
pre-populated based on the database’s accounting settings. Click Create Payment to
process the vendor bill.

Once payment has been registered for a vendor bill, and the bill displays the green Paid
banner, the Should Be Paid field status is set to No.

> **Note:**
>
> The Should Be Paid status on bills is automatically set by Odoo. However, the status
> can be manually changed by clicking the field’s drop-down menu inside the Other Info
> tab.

## View a purchase order’s billing status

Once a PO is confirmed, its Billing Status can be viewed under the Other
Information tab on the PO form.

To view the Billing Status of a PO, navigate to Purchase app ‣
Orders ‣ Purchase Orders, and select a PO to view.

Click the Other Information tab, and locate the Billing Status field.

![Billing status field on a purchase order form.](../../../../_images/control-bills-billing-status.png)

The table below details the different values the Billing Status field could read, and
when they are displayed, depending on the *Bill Control* policy used.

| Billing Status | On received quantities | On ordered quantities |
| --- | --- | --- |
| Nothing to Bill | PO confirmed; no products received | *Not applicable* |
| Waiting Bills | All/some products received; bill not created | PO confirmed |
| Fully Billed | All/some products received; draft bill created | Draft bill created |

> **Note:**
>
> [Manage vendor bills](manage.html)

---

# Manage vendor bills

A *vendor bill* is an invoice received for products and/or services purchased by a company from a
vendor. Vendor bills record payables as they arrive from vendors, and can include amounts owed for
the goods and/or services purchased, sales taxes, freight and delivery charges, and more.

In Odoo, a vendor bill can be created at different points in the purchasing process, depending on
the *bill control* policy selected on the product’s settings.

## Bill control policies

To configure a product’s bill control policy, navigate to Purchase app ‣ Products
Products, and click on the desired product to open it. Then, click on the Purchase tab.
Under the *Vendor Bills* section, the *Control Policy* field lists two policy options:

- On ordered quantities: creates a vendor bill as soon as a purchase order is confirmed.
  The products and quantities in the purchase order are used to generate a draft bill.
- On received quantities: a bill is only created **after** all (or part) of the total
  order has been received. The products and quantities received are used to generate a draft bill.

![Bill control policies on a product record.](../../../../_images/manage-configuration-settings.png)

Once a policy is selected, click Save to save the changes.

### 3-way matching

The *3-way matching* policy ensures vendor bills are only paid once all (or some) products in a
purchase order (PO) have been received.

To activate 3-way matching, navigate to Purchase app ‣ Configuration ‣
Settings, and scroll to the Invoicing section.

Tick the checkbox next to 3-way matching, and click Save.

> **Warning:**
>
> The 3-way matching feature is **only** intended to work with the Bill
> Control policy set to Received quantities.

## Manage vendor bills in Accounting

Vendor bills can also be created directly from the *Accounting* app, without having to create a
purchase order first.

Navigate to Accounting app ‣ Vendors ‣ Bills, and click New. Doing
so reveals a blank Vendor Bill form.

Add a vendor in the Vendor field. Then, in the Invoice Lines tab, click
Add a line to add products.

Select a product from the drop-down menu in the Product field, and enter the quantity to
order in the Quantity field.

Select a Bill Date, and configure any other necessary information. Finally, click
Confirm to confirm the bill.

Once confirmed, click the Journal Items tab to view the Account journals.
These journals are populated based on the configuration on the corresponding Vendor and
Product forms.

If necessary, click Credit Note to add a credit note to the bill. Additionally, a
Bill Reference number can be added.

Once ready, click Register Payment, followed by Create Payment, to complete
the Vendor Bill.

> **Note:**
>
> To link a draft bill to an existing purchase order, click the drop-down menu next to
> Auto-Complete *before* clicking Confirm, and select a PO from the menu.
>
> The bill auto-populates with the information from the chosen PO.
>
> ![Auto-complete drop-down list on draft vendor bill.](../../../../_images/manage-auto-complete.png)

## Batch billing

Vendor bills can be processed and managed in batches in the *Accounting* app.

Navigate to Accounting app ‣ Vendors ‣ Bills. Then, click the
checkbox in the top-left corner, beside the Number column, under the
New button.

This selects all existing vendor bills with a Status of Posted or
Draft.

Click the  Print button to print the selected invoices or bills.

Click Register Payment to create and process payments for multiple vendor bills at once.

> **Note:**
>
> Only payments with their Status listed as Posted can be billed in
> batches. Payments in the Draft stage **must** be posted before they can be included
> in a batch billing.

Clicking Register Payment opens a Register Payment pop-up window. From the
pop-up window, select the Journal the bills should post to, choose a Payment
Date, and select a Payment Method.

There is also the option to Group Payments together from this pop-up window, as well. If
this checkbox is ticked, only one payment is created, instead of one per bill. This option only
appears if the *Batch Payments* feature is enabled in the settings of the
Accounting app.

Once ready, click the Create Payment button. This creates a list of journal entries on a
separate page. The journal entries on this list are all tied to their corresponding vendor bills.

![Batch billing register payment pop-up window.](../../../../_images/manage-batch-billing.png)
> **Note:**
>
> [Control policies](control_bills.html)

---

# Advanced

---

# Suggest quantities based on historical demand

For a straightforward push-based replenishment strategy, the *Suggest* feature recommends quantities
to order on requests for quotations (RFQs) based on historical demand.

## Key parameters

- *Replenish for*: future coverage window (days).
- *Based on*: period that defines historical demand: last 7 days, 30 days, 3 months, 12 months, or
  the same month or quarter the previous year.
- *Factor*: growth or decline factor (default 100%). After obtaining the total from the period,
  multiply the historical demand by this percentage to determine how much of the demand should be
  replenished. (e.g., input `120%` if sales are projected to grow 20% more than the previous period)

## Demand calculation

To estimate demand, Odoo sums all [validated deliveries](../../inventory/shipping_receiving/daily_operations/receipts_delivery_one_step.html#inventory-delivery-one-step), [components consumed in manufacturing orders](../../manufacturing/basic_setup/bill_configuration.html#manufacturing-basic-setup-setup-components) (MOs), or used to [resupply subcontractors](../../manufacturing/subcontracting/subcontracting_resupply.html) coming from the warehouse specified
on the RFQ in the *Based on* period. The *average daily demand* is this sum of outgoing moves
divided by the number of days in the *Based on* period, multiplied by *Factor*. The
*estimated demand* is the *average daily demand* multiplied by *Replenish For* days.

\[\begin{split}Average~Daily~Demand = \frac{Delivered~or~Consumed~Items}{Based~on~Days} \times Factor
\\ \\ Estimated~Demand = Average~Daily~Demand \times Replenish~for~Days\end{split}\]

> **Note:**
>
> Only Assigned or Confirmed moves are taken into account in
> the *average daily demand* calculations, sales quotations or manufacturing orders
> in Draft are not taken into account until validated.

> **Note:**
>
> In a multi-warehouse setup, internal deliveries are also counted in demand estimation.
> In the case of a central warehouse dispatching products to individual stores,
> the *average daily demand* of the central warehouse will include internal transfers to
> individual stores.

## Recommended quantity

To find the suggested quantity, Odoo deducts the *estimated demand* from the current stock
available quantity and all incoming shipments.

\[Recommended~Quantity = Estimated~Demand - (Available~Stock + Incoming~Stock)\]

> **Tip:**
>
> In [example 1], Odoo recommends `19` units to
> *Replenish for* `14` days *Based on* the past month’s `40` delivered units.

## Prerequisite setup

1. **Purchase** and **Inventory** apps must be [installed](../../../general/apps_modules.html#general-install).
2. [Validate at least one delivery order](../../inventory/shipping_receiving/daily_operations/receipts_delivery_one_step.html#inventory-delivery-one-step) for each product.

   Ensures there is a past delivery record so the system can calculate average daily demand.
3. [Add a vendor to the vendor pricelist](../manage_deals/rfq.html#purchase-manage-deals-vendor-pricelist) with a
   purchase price for each product.

   The *Suggest* feature is vendor-specific, so each product needs a matching vendor for accurate
   purchase quantity and price calculations.
4. Set the *Product Type* to *Goods* and ensure the product is [Tracked by quantity](../../inventory/product_management/configure/type.html#inventory-product-management-manufacture).

   Ensures the system can manage stock levels and calculate recommended replenishment quantities for
   tangible items.

## Suggest quantities to order

To suggest quantities based on past sales, navigate to the Purchase app. Create a
New RFQ or select an existing one.

In the RFQ, set the Vendor field to the chosen supplier.

In the Products tab, click the Catalog button to view that vendor’s items.

> **Warning:**
>
> Verify that each product in the catalog is configured with the chosen vendor
> and that the Purchase Order is in the RFQ stage

> **Note:**
>
> By default, products listed in the product catalog are filtered by vendor.
>
> Remove the filter in the search bar to view all items or use the built-in
> Group By for Product Category.

Inside the Catalog, toggle Suggest in the left sidebar to activate
the feature. Complete its fields as follows:

- Replenish for: Number of days intended to stock products.
- Based on: There are two inputs:

  > 1. Period: select the time frame that represents historical demand (e.g., Last 30
  >    Days, April 2024).
  > 2. Growth factor %: scale the demand up or down (e.g., 120% for 20% growth, 30% for 70% drop).
- The total in the bottom shows the order value. Odoo multiplies the vendor’s *Unit
  Price* by the suggested quantity.

Once the parameters are confirmed, click Add All to add all suggestions to the
order. Adjust amounts if needed, then click Back to Quotation to confirm the final
numbers on the RFQ.

## Example Workflow

### Recommend at 100% growth

A company needs to replenish orchids for 14 days, referencing the last 30 days of historical data,
assuming the revenue growth is the same this month, at 100%.

Delivered/consumed within the period:

- 20 units delivered 15 days ago in a `WH/OUT` operation.
- 20 units delivered 1 day ago
- Total: 40 units in the last 30 days

#### Variables

- Replenish for: 14 days
- Based on: 30 days

  - total delivered/consumed in the period: 40 units
- Factor: 100%

\[Average~Daily~Demand = \frac{40}{30} \approx 1.33 \text{ units/day}\]

#### Suggested quantity

\[Suggested~Quantity = 1.33 \times 14 \approx 18.67 \text{ (rounded to 19 units)}\]

![Suggestion to purchase 19 units.](../../../../_images/result-14.png)

Suggestion to purchase 19 orchids. Since the *Unit Price* is $3, \($3 \times 19 = $57\),
which is the total amount displayed.

### Planning for Mother’s Day

To better plan for the upcoming Mother’s day week, the company changes *Based on* to the
same month last year (May 2024). As the business has grown since then, they also decide to add
a 120% growth factor.

#### Variables

- Replenish for 7 days
- Based on: May 2024,

  - total delivered/consumed in the entire May 2024 month: 361 units
- Factor: 120%

\[Average~Daily~Demand = \frac{361}{30} \times 1.20 \approx 14.44 \text{ units/day}\]

#### Suggested quantity

\[Suggested~Quantity = 14.44 \times 7 \approx 101.08 \text{ (rounded up to 102 units)}\]

![Suggestion to purchase 102 orchids.](../../../../_images/result-30.png)

Suggestion to purchase 102 orchids. Each orchid costs $3 with the chosen vendor, so
\($3 \times 102 = $306\).

## Best practices

1. Validate historical data

   Forecasts are based on validated delivery orders, manufacturing orders, and other inventory
   actions that consume quantities. For delivery orders, the *Effective Date* field is considered
   the date the quantities were consumed.

   ![Example of effective date field.](../../../../_images/effective-date.png)
2. Maintain accurate vendor pricelists

   Review and update vendor pricelists to reflect the latest pricing and supplier information to
   ensure correct suggestions.
3. Test sales projections based on seasonality

   Reference prior months or quarters to capture seasonal fluctuations and experiment with growth
   and decline factors to project sales.
4. Review suggestions critically

   Although the tool provides a baseline recommendation, always apply business judgment. Market
   changes, promotions, and upcoming events can affect actual demand.

---

# Purchase Analysis report

The *Purchase Analysis* report provides statistics about products purchased using Odoo’s
**Purchase** app. This data is useful for gaining a deeper understanding of key metrics related to
purchase orders (POs), including the quantity of products ordered and received, the amount of time
it takes to receive purchased products, and more.

To open the Purchase Analysis report, navigate to Purchase app ‣ Reporting ‣
Purchase.

> **Warning:**
>
> The Purchase Analysis report is one of many reports available across the Odoo app
> suite. This documentation only covers the measures specific to the Purchase Analysis
> report, along with a few use case examples.
>
> For a full overview of the basic features available in most Odoo reports, see the documentation
> on [reporting essentials](../../../essentials/reporting.html).

## Measures

*Measures* refer to the various datasets that can be displayed on the Purchase Analysis
report, with each dataset representing a key statistic about POs or products. To choose a measure,
click the Measures  button, and select one of the options from the
drop-down menu:

- # of Lines: The number of PO order lines, across all POs.
- Average Cost: The average cost of POs.
- Days to Confirm: The number of days it takes to confirm a PO.
- Days to Receive: The number of days it takes to receive the products in a PO.
- Gross Weight: The total weight of purchased products.
- Qty Billed: The quantity of a product (or products) for which the vendor has already
  been billed.
- Qty Ordered: The quantity of a product (or products) ordered.
- Qty Received: The quantity of an ordered product (or products) received.
- Qty to be Billed: The quantity of an ordered product (or products) for which the
  vendor has yet to be billed.
- Total: The total amount spent, including tax.
- Untaxed Total: The total amount spent, excluding tax. This measure is selected by
  default.
- Volume: The total volume of ordered products, for products which are measured by
  volume.
- Count: The total count of POs.

> **Note:**
>
> Only one measure can be selected at a time when one of the
> (graph view) options is enabled. However, multiple measures, and varying group-by
> criteria (on the x and y axes), can be selected when using the
> (pivot table).

## Use case: determine days to receive products from each vendor

One possible use case for the Purchase Analysis report is determining how long each
vendor takes to deliver purchased items. This allows companies to make better informed decisions
about which vendors they want to purchase from.

> **Tip:**
>
> A local bike shop, *Bike Haus*, sells high-quality unicycles, bicycles, tricycles, and all the
> accessories needed to ride and maintain them. They purchase their inventory from a few different
> vendors, and then sell those products on to customers through their storefront.
>
> Recently, Bike Haus has decided to have their purchasing manager, David, look into how long it
> has taken each of their vendors to deliver the items they’ve purchased during the current year,
> 2024.
>
> David starts by navigating to Purchase app ‣ Reporting ‣ Purchase, and
> selecting the  (bar chart) graph type at the top of the report.
>
> Next, he clicks the  (toggle) button on the right of the search
> bar to open its drop-down menu. In the Confirmation Date filter section, he makes
> sure that **only** the 2024 filter is enabled. Then, he selects the
> Vendor option in the Group By section, before clicking away from the
> drop-down menu to close it.
>
> Finally, David clicks on the Measures  drop-down menu, and
> selects the Days to Receive option.
>
> With all of these options enabled, the Purchase Analysis report shows a bar chart,
> with one bar for each vendor, representing the average number of days it takes to receive
> products purchased from the vendor.
>
> Using this data, David can see that it takes Bike Friends over 4.5 days, on average, to deliver
> purchased products. This is more than four times the amount of time it takes any other vendor.
>
> Based on these findings, David makes the decision to reduce the quantity of products purchased
> from Bike Friends.
>
> ![The Purchase report, showing the average days to receive products from vendors.](../../../../_images/dtr.png)

## Use case: compare vendor POs for two time periods

Another use for the Purchase Analysis report is to compare key statistics about POs
for two different time periods, for a specific vendor. By doing so, it is easy to understand how
purchases from the vendor have increased or decreased.

> **Tip:**
>
> Following the [previous example], it has been one month
> since Bike Haus decided to reduce the quantity of products purchased from Bike Friends, one of
> their retailers. Bike Haus’ purchasing manager, David, wants to understand the impact this
> decision has had on the amount of money they have spent on Bike Friends products.
>
> David starts by navigating to Purchase app ‣ Reporting ‣ Purchase. Then, he
> selects the  (pivot table) option at the top of the screen.
>
> In the search bar, he types `Bike Friends`, and clicks Enter, so the report only
> shows data for purchases from Bike Friends.
>
> Then, David clicks the  (toggle) button on the right of the
> search bar to open its drop-down menu. In the Confirmation Date field, he leaves the
> June and 2024 filters enabled. He also selects Confirmation
> Date: Previous Period in the Comparison section, before clicking away from the
> drop-down menu to close it.
>
> Next, David clicks on the Measures  drop-down menu. He leaves
> the Total and Untaxed Total datasets enabled, and disables the
> Order and Count datasets.
>
> Finally, David clicks the  Total button above the rows on
> the pivot table, and selects the Product option.
>
> With all of these options configured, the Purchase Analysis report shows a pivot
> table comparing purchase data for the current month, June, with the previous month, May.
>
> The pivot table is broken down into two main columns: one for the untaxed total spent, and one
> for the taxed total spent. These columns are further broken down into three smaller columns: the
> amount spent in May, the amount spent in June, and the variation between the two months,
> represented as a percentage.
>
> On the left side of the pivot table, one row is shown for each product purchased from Bike
> Friends during June. Using this report, David is able to see that Bike Haus has spent much less
> money on products purchased from Bike Friends, compared to the previous month.
>
> ![The Purchase report, comparing the amount spent at a vendor.](../../../../_images/comparison2.png)

---

# Vendor costs report

With the *Purchase* application, users can track the fluctuation of vendor costs over time. This
allows users to identify the most expensive vendors, and track seasonal changes.

## Create vendor costs reports

To create a vendor costs report, first navigate to Purchase app ‣ Reporting ‣
Purchase to open the Purchase Analysis dashboard. By default, the dashboard displays a
line chart overview of the Untaxed Total of POs (Purchase Orders) with a
Confirmation Date for the current month, or of RFQs (Requests for Quotation) with a
status of *Draft*, *Sent, or \*Cancelled*.

### Add filters and groups

On the top-right, click the  (pivot) icon to switch to pivot view.

Remove any default filters from the Search… bar. Then, click the  (down) icon to open the
drop-down menu that contains the Filters, Group By, and
Favorites columns.

> **Note:**
>
> Unless otherwise specified, the report displays data from both RfQs and POs. This can be
> changed by selecting either Requests for Quotation or Purchase Orders
> under the Filters column.

Under the Filters column, select a date range to use for comparison. The report can be
filtered by either Order Date or Confirmation Date. Choose one from the
list, and click the  (down) icon to specify the date range, either by month, quarter, or year.

Next, under the Group by column, select Vendor. Then, select
Product, which is also located in the Group By column.

> **Note:**
>
> Selecting Product is **not** required for this report. However, it is recommended, as
> it provides additional insight into the performance of individual vendors. Additional selections
> can be made under the Group by heading as well, including Product
> Category, Status, and Purchase Representative.
>
> To ensure the report is generated correctly, make sure that Vendor is the **first**
> selection made under the Group By column.

Next, make a selection under the Comparison heading. These options are only available
after the date range is selected under the Filters column, and vary based on that range.
Previous Period adds a comparison to the previous period, such as the last month or
quarter. Previous Year compares the same time period from the previous year.

> **Note:**
>
> While multiple time-based filters can be added at once, only one comparison can be selected at a
> time.

![The drop-down menu of filters, group by and comparison options for the vendor costs report.](../../../../_images/filters-groups1.png)

### Add measures

After selecting the Filters, Group by, and Comparison settings,
click out of the drop-down menu.

By default, the report displays with the following measures: Order, Total,
Untaxed Total, and Count. Click Measures at the top-left to open
the drop-down list of available measures. Click Average Cost to add it to the report.
Select any additional measures to add to the report, or click on any of the already selected
measures to remove them, if desired.

> **Note:**
>
> It is recommended to run the report with at least Average Cost, Total, or
> Untaxed Total selected from the Measures list. Additional measures, such
> as Days to Receive, can be added to provide additional insights.

## View results

After all of the [filters and measures have been selected], the report generates in the pivot view. Click
Insert in Spreadsheet to add the pivot view into an editable spreadsheet format within
the *Documents* app.

> **Warning:**
>
> The Insert in Spreadsheet option is only available if the *Documents Spreadsheet*
> module is installed.

![A sample of a vendor costs report with the measures set as total and average costs.](../../../../_images/sample-vendor-report.png)
> **Note:**
>
> The vendor costs report is also available in *graph* view. Click the
> (area chart) icon to change to graph view. Click the corresponding icon at the top of
> the report to switch to a  (bar chart),
> (line chart), or  (pie chart).

> **Note:**
>
> To save this report as a *favorite*, see [Favorites](../../../essentials/search.html#search-favorites).

---

# Procurement expenses report

With the *Purchase* application, users can monitor procurement expenses over time. This report helps
companies track and analyze spending, identify cost-saving opportunities, and ensure efficient
budget management.

## Create procurement expenses report

To create a procurement expenses report, first navigate to Purchase app ‣ Reporting ‣ Purchase to
open the Purchase Analysis dashboard.

By default, the dashboard displays a line chart overview of the Untaxed Total of
Purchase Orders (POs) with a Confirmation Date for the current month, or of
Requests for Quotation (RFQs) with a status of *Draft*, *Sent*, or *Cancelled*.

### Add filters and groups

On the top-right, click the  (pivot) icon to switch to pivot view.

> **Note:**
>
> While the procurement expenses report can also be [viewed] as a
> (bar chart),  (line chart), or
> (pie chart), the pivot view provides the most detailed view of the data, and is the
> recommended starting point.

Remove any default filters from the Search… bar. Then, click the  (down) icon to open the
drop-down menu that contains the Filters, Group By, and
Favorites columns.

> **Note:**
>
> Unless otherwise specified, the report displays data from both RfQs and POs. This can be
> changed by selecting either Requests for Quotation or Purchase Orders
> under the Filters column.

Under the Filters column, select a time frame to use for comparison. The report can be
filtered by either Order Date or Confirmation Date. Choose one from the
list, and click the  (down) icon to specify the date range, either by month, quarter, or year.

Next, under the Group by column, select Vendor. Then, select
Product Category, which is also located in the Group By column.

> **Note:**
>
> The selections under the Group By heading can be altered, depending on the needs of
> the individual company. For example, selecting Product, instead of Product
> Category, provides a more in depth look at the performance of specific items, in place of an
> entire category.

Next, make a selection under the Comparison heading that appears. These options are only
available after the date range is selected under the Filters column, and vary based on
that range. Previous Period adds a comparison to the previous period, such as the last
month or quarter. Previous Year compares the same time period from the previous year.

> **Note:**
>
> While multiple time-based filters can be added at once, only one comparison can be selected at a
> time.

![The drop-down menu of filters, group by and comparison options for the procurement expenses report.](../../../../_images/filters-groups.png)

The filter for Q2, comparison for **Previous Period**, and group-by for **Vendor** and **Product
Category** were selected.

### Add measures

After selecting the Filters, Group by, and Comparison settings,
click out of the drop-down menu.

By default, the report displays data with the following measures: Order,
Total, Untaxed Total, and Count. Click Measures at
the top-left to open the drop-down list of available measures.

Click the following specific measures to include additional columns for the procurement expenses
report:

- Total and Untaxed Total: can include one or both measures. These are
  included for overall spending analysis.
- Average Cost: included to evaluate cost efficiency.
- Days to Confirm and Days to Receive: used to assess supplier performance.
- Qty Ordered and Qty Received: used to understand order efficiency.
- Qty Billed and Qty to be Billed: used to track order accuracy.

> **Note:**
>
> Additional measures can be included in the report, if desired, to provide additional insights.
> For example, Gross Weight and Volume may be included for further
> logistics and management analysis.

After selecting all necessary measures, click out of the drop-down menu.

## View results

After all of the filters and measures have been selected, the report generates in the selected view.

![A sample version of the procurement expenses report.](../../../../_images/sample-per-report.png)

Click Insert in Spreadsheet to add the pivot view into an editable spreadsheet format
within the *Documents* app.

> **Warning:**
>
> The Insert in Spreadsheet option is **only** available if the *Documents Spreadsheet*
> module is installed.

> **Note:**
>
> The procurement expenses report is also available in graph view. Click the  (area
> chart) icon to change to graph view. Click the corresponding icon at the top of the report to
> switch to a  (bar chart),  (line
> chart), or  (pie chart).

> **Note:**
>
> To save this report as a *favorite*, see [Favorites](../../../essentials/search.html#search-favorites).

---

# EDI purchase-to-sales order import

Electronic data interchange (EDI) enables companies using different software systems to exchange
information in a standardized, structured format.

In Odoo, a *purchase order* (PO) can be exported as an XML file and imported as a *sales order* (SO)
into another Odoo database, removing the need for manual entry of products, quantities, prices, and
other key information.

The workflow in this document describes how buyers and sellers exchange data directly between their
Odoo databases. As an alternative, sellers can receive a PDF version of the request for quotation
(RFQ) by email and [upload it directly in their Sales dashboard]. **This method is simpler** but does not use the XML-based exchange
described in the document.

> **Note:**
>
> Exported XMLs follow the [UBL schema](https://docs.peppol.eu/poacc/upgrade-3/syntax/Order/tree/). When exchanging data between two
> Odoo databases, this schema remains compatible.
>
> However, implementing custom developments for software that does not support the UBL schema may
> introduce additional complexity.

## Roles and configuration

To facilitate the EDI workflow, two companies are involved: the buyer (the company placing the
order) and the seller (the company fulfilling the order). Each company has specific roles and
configurations.

### Buyer database

The buyer database is responsible for creating and confirming purchase orders. Prerequisites
include:

1. (required) [installing](../../../general/apps_modules.html#general-install) the **Purchase** app
2. (optional) adding vendors (the sellers in this workflow) as [portal users](../../../general/users/user_portals.html).

### Seller database

The seller database is responsible for receiving and processing sales orders. The only prerequisite
is [installing](../../../general/apps_modules.html#general-install) the **Sales** app.

## Workflow

### Buyer’s process

To begin, the buyer (in their database) navigates to the Purchase app to create a
RFQ.

Set the Vendor to the portal user representing the seller, and Confirm the
RFQ. Doing so converts it into a [purchase order](../manage_deals/rfq.html).

> **Tip:**
>
> PO from the buyer’s database. The Vendor is the seller’s portal user account, Joel.
>
> ![Example PO. The Vendor is the seller's portal user account, Joel.](../../../../_images/po-database-view.png)

### Seller’s process

Once the PO is confirmed, it appears on the seller’s portal dashboard. The seller downloads the
XML file and uploads it to their database.

#### Download file

As the seller, log in to the buyer’s database as the portal user. On the dashboard, scroll down and
click the Our Orders button. Doing so reveals a list of purchase orders the buyer’s
database has addressed to the portal user.

Select the desired purchase order, and the click Connect with your software! button.

In the pop-up window, copy the provided URL, and paste it into a new browser tab to download the XML
file.

> **Tip:**
>
> Joel’s portal view of the PO. The first image displays the Connect with your
> software! button, and the second image displays a pop-up window with the Copy
> button.

![Portal view of the PO, with "Connect your software!" button.](../../../../_images/po-portal-view.png)
![Pop-up to copy link.](../../../../_images/pop-up2.png)
> **Tip:**
>
> [`XML file`](../../../../_downloads/393c486cef31f33453cb187b71fbac3a/P00017.xml) for PO00017

#### Upload file

Next, the seller logs in to their own Odoo database and opens Sales app. Click
Upload and select the downloaded XML file. Alternatively, users can drag and drop the
file into the Quotations dashboard.

Doing so automatically generates a sales order with the customer populated as the buyer and all
product lines, quantities, and prices pre-filled. This process ensures efficient and accurate data
exchange between the two databases.

![Uploaded SO in the seller's database.](../../../../_images/so.png)

Uploaded SO in the seller’s database.

> **Note:**
>
> [Create quotations](../../../sales/sales/sales_quotations/create_quotations.html)

---

# Purchase & Vendor analysis dashboard

The *Purchase & Vendor analysis* dashboard, available in the [Odoo Dashboards](../../../productivity/dashboards.html) app, offers various metrics to evaluate purchasing performance
and vendor reliability.

The dashboard tracks financial data like total and average purchase amounts and the number of
purchase orders. It also provides KPIs for supplier performance, such as the average time to receive
products and the percentage of quantities received on time. This makes it possible to rank vendors
and optimize procurement strategy accordingly.

To access the *Purchase & Vendor analysis* dashboard, go to the **Dashboards** app, then, in
the left panel, navigate to the Logistics section and click the name of the dashboard.
The dashboard opens in the main view.

![Purchase & Vendor analysis dashboard.](../../../../_images/purchase-vendor-analysis.png)
> **Note:**
>
> - [Using Odoo dashboards](../../../productivity/dashboards.html#dashboards-use-dashboards)
> - [Customizing Odoo dashboards](../../../productivity/dashboards/build_and_customize_dashboards.html#build-and-customize-dashboards-customize)

> **Note:**
>
> The [access rights](../../../productivity/dashboards.html#dashboards-access-and-sharing) for Odoo dashboards are based on user
> groups, and are managed within the Dashboards app. By default, the Purchase & Vendor
> analysis dashboard is only visible to, and can only be accessed by, users with admin access to
> the **Inventory** app.

## Navigate the dashboard

> **Note:**
>
> - By default, this dashboard shows data for All time. To show data for a specific
>   period, click  All time above the dashboard and select or define
>   the appropriate period.
> - For a more precise analysis, filter the dashboard by vendor via the search bar.

Eight cards at the top of the dashboard show the following information:

- Purchased value: indicates the total value of purchases during the selected period.
- Average order value: indicates the average purchase amount per order during the
  selected period.
- Number of orders: indicates the number of purchase orders during the selected period.
- Quantity ordered: indicates the quantity of products ordered during the selected
  period.
- Days to receive: indicates the average number of days between the order and receipt of
  purchased products (i.e., between the order deadline of the purchase order and the expected
  arrival of the purchase order line).

  > **Note:**
  >
  > The expected arrival date is not impacted by a change to the scheduled date on the receipt.
- Days to Confirm: indicates the average number of days before a purchase order is
  confirmed (i.e., between the creation date of the RFQ and the confirmation date of the purchase
  order).
- Supplier service level: indicates the quantity received versus the quantity purchased,
  as a percentage.

  > **Note:**
  >
  > This KPI is impacted by purchases with future expected receipts.
- On time deliveries: indicates the percentage of products received on time (based on
  the expected arrival date on purchase order lines)

The following charts are available:

- Purchase Value by confirmation date: shows the total value of confirmed purchases by
  date.
- % On time deliveries by vendor: shows the percentage of products received on time, by
  vendor (based on expected arrival on purchase order lines.)
- Top vendors by amount: shows the ranking of vendors by total value of purchase orders
  and number of purchase orders.
- Top vendors by lead time in days: shows the average number of days required to receive
  purchased products, by vendor (Order deadline purchase order - Expected
  arrival purchase order line).

  > **Note:**
  >
  > The expected arrival date is not impacted by a change to the scheduled date on the receipt.
- Average product purchased cost by confirmation week: shows the average unit cost of
  products purchased, by week in which the purchase order is confirmed.
- Top purchase orders by value: lists the ten purchase orders with the highest total
  value, in descending order.
- Top 10 late receipts: lists the ten receipts with the longest delay after the expected
  receipt date.
- Top purchased products: lists the ten products with the highest total purchase amount,
  in descending order.
- Purchase Orders by Buyer: shows the percentage of purchases by buyer.