# Sales — Quotations, Orders & Pricelists

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

Sales orders, quotations, pricelists, customer portal, and order confirmation flows. Use when configuring the sales module or building custom sales workflows.

---

# Sales

The **Sales** application is used to run the sales process (from quotation to sales order) and
deliver and invoice what has been sold. Any product with the *Sales* checkbox ticked on its product
form can be sold with the **Sales** app.

> **Note:**
>
> - [Odoo Tutorials: Sales](https://www.odoo.com/slides/sales-17)

---

# Sales quotations

A *sales quotation* or quote is a document sent to a customer that outlines the estimated costs and
terms for goods and services. Once accepted, a quotation can be converted into a sales order, which
serves as the final agreement before delivery and invoicing.

## Sales flow overview

Quotations fit into a broader sales flow that connects different stages of customer interactions
from initial interest to payment.

The typical flow follows these steps:

1. *Quotation*: A proposal sent to the customer with product details and pricing.
2. *Sales order*: Created automatically when the customer accepts the quotation, confirming the
   sale.
3. *Delivery* (if applicable): Products are shipped or services are delivered.
4. *Invoice*: The final bill is issued based on the sales order or delivered products/services.
5. *Payment*: The customer settles the invoice, completing the sales cycle.

This flow helps businesses track the entire lifecycle of a sale while keeping information consistent
across apps.

In Odoo, quotations are configured in the **Sales** app. They can also be generated from other apps
as part of the sales workflow:

- **CRM**: [Convert opportunities](../crm/acquire_leads/send_quotes.html) into quotes to follow up
  on potential deals.
- **Helpdesk**: [Generate quotes from tickets](../../services/helpdesk/advanced/after_sales.html)
  when offering paid services or products.
- **Subscriptions**: [Offer recurring services](../subscriptions.html) before
  starting an automatic billing cycle.

[#### Create quotations

Create, configure, and send quotations to customers.](sales_quotations/create_quotations.html)[#### Quotation templates

Configure and use quotation templates to send tailor-fit quotations at a quicker pace.](sales_quotations/quote_template.html)[#### Optional products

Offer useful and related products to customers to increase sales.](sales_quotations/optional_products.html)[#### Online signatures for order confirmations

Customers have the ability to confirm orders via online signatures, directly on sales orders.](sales_quotations/get_signature_to_validate.html)[#### Online payment order confirmation

Customers have the ability to confirm orders via online payment, directly on sales orders.](sales_quotations/get_paid_to_validate.html)[#### Quotation Deadlines

Set deadlines on quotations to encourage customers to act in a timely manner when
closing business deals.](sales_quotations/deadline.html)[#### Deliver orders and invoices to different addresses

Specify separate customer delivery and invoicing addresses on quotations.](sales_quotations/different_addresses.html)[#### Product variants on quotations and sales orders

Add product variants to sales orders to provide additional options for single products.](sales_quotations/orders_and_variants.html)[#### PDF quote builder

Add custom PDF files to quotations to elevate the document’s headers and designs.](sales_quotations/pdf_quote_builder.html)

## Sales quotations in business deals

Sales quotations serve as a key step in the sales process, bridging the gap between a customer’s
initial inquiry about goods and services and the final contractual agreement for payment and
delivery. The quotation also provides transparency in pricing, helping both parties negotiate and
finalize the terms before making a commitment.

Sales quotations play a crucial role in business transactions by defining the scope and cost of what
is being sold to the end-customer; setting clear expectations on pricing, delivery, tax, and
payment terms; and providing a documented stage where the business deal can be negotiated before
agreed upon.

## Key components of a sales quotation

A well-structured sales quotation comprises the following:

- Quotation number and date: A unique identifier for tracking and reference, as well as the
  [dates of issue and expiration](sales_quotations/deadline.html). In Odoo **Sales** app, the
  quotation number is assigned under a standard naming convention once it is confirmed.
- Customer information: Customer name and contact information, as well as
  [invoicing and delivery address](sales_quotations/different_addresses.html).
- Products and services: Itemized listing of items to be purchased, including quantity,
  specifications (as needed), and unit price.
- Payment terms and [pricelists](products_prices/prices/pricing.html): Configured agreements and
  rules for the pricing and payment of this particular sales quotation.
- Special pricing: Optional [discounts and promotional pricing](products_prices/prices/pricing.html) to update and/or modify individual product lines.
- Total cost and currency: Summary totals of product or service and shipping prices, including
  relevant taxes.

In Odoo’s **Sales** app, quotations can include additional details and configurations that add
more detail and information, such as [quotation templates](sales_quotations/quote_template.html),
[subscription plans](../subscriptions.html), and [sales team referrer name](sales_quotations/create_quotations.html).

![Unconfirmed sales quotation in Odoo **Sales** app.](../../../_images/sales-quotation.png)

---

# Create quotations

In Odoo **Sales**, quotations can be created and sent to customers. Once a quotation has been
confirmed, it officially turns into a *sales order*, which can then be invoiced and paid for.

## Quotation settings

To access these setting options, navigate to Sales app ‣ Configuration ‣
Settings, and scroll to the Quotations & Orders section.

![The Quotations and Orders section on the Odoo Sales app Settings page.](../../../../_images/quotations-orders-section.png)

- Quotation Templates: Enable this option to create quotation templates featuring
  standard product offers, which are then selectable on quotation forms. When this checkbox is
  ticked, an additional field, Default Template, appears, along with a link to the
  Quotation Templates page.
- Online Signature: Request an online signature to confirm orders.
- Online Payment: Request an online prepayment from customers to confirm orders. Request
  a full or partial payment (via down payment). When this checkbox is ticked, an additional field,
  Prepayment amount (%), appears. There is also a link to the Payment
  Providers page.
- Default Quotation Validity: Determine a set amount (in days) that
  quotations can remain valid for.
- Default Recurrence: Select a default period from the drop-down menu to use as a
  recurrence period for a new quotation.
- Sale Warnings: Get warning messages about orders that include specific products or
  customers.
- PDF Quote builder: Customize the look of quotations with header pages, product
  descriptions, footer pages, and more.
- Lock Confirmed Sales: Ensure no further edits can be made to confirmed orders.
- Pro-Forma Invoice: Send pro-forma invoices to customers.

To activate any of these settings, tick the checkbox beside the desired option(s). Then, click
Save.

## Quotations dashboard

The *Quotations* dashboard is the page that appears when the Sales app is opened.

By default, the Quotations dashboard displays all quotations in the database related to
the current user, as indicated by the default My Quotations filter present in the search
bar.

![The Quotations dashboard present in the Odoo Sales application.](../../../../_images/quotations-dashboard.png)
> **Note:**
>
> To view *all* quotations in the database, remove the My Quotations filter from the
> search bar.

Quotations on this page appear in a default list view, but can also be viewed in a
 Kanban view,  Calendar,
 Pivot table,  Graph, or
 Activity view.

To view and/or modify any listed quotation from the Quotations dashboard, click on the
desired quotation line from the list, and Odoo reveals the specific form for that selected
quotation.

## Create quotation

To create a quotation, open the Sales app, and click the New button,
located in the upper-left corner of the main Quotations dashboard.

> **Warning:**
>
> The New button is **only** present if the Quotations dashboard is in list
> or Kanban view.

Clicking the New button reveals a blank quotation form, with various fields and tabs to
configure.

![A typical quotation form in the Odoo Sales application.](../../../../_images/quotation-form.png)

Begin by entering the customer’s name in the Customer field at the top of the form. This
is a **required** field.

If the customer’s information is already in the database, the Invoice Address and
Delivery Address fields auto-populate with the saved information for those respective
fields, based on the data from that customer’s contact record (found in the **Contacts**
application).

If the customer was referred by another customer or contact, enter their name in the
Referrer field.

If a Referrer is selected, a new field, Commission Plan appears, in which a
commission can be selected from the drop-down menu. This commission is rewarded to the contact
selected in the Referrer field.

Next, if they have not already been auto-populated with the customer’s information, enter the
appropriate addresses in the Invoice Address and Delivery Address fields.
Both of these fields are **required**.

Then, if desired, choose a Quotation Template from the drop-down field to apply to this
quotation. It should be noted that some additional fields may appear, depending on the template
selected.

The default date that appears in the Expiration field is based on the number configured
in the [Default Quotation Validity setting] (in
Sales app ‣ Configuration ‣ Settings).

> **Note:**
>
> When using a quotation template, the date in the Expiration field is based off the
> Quotation Validity figure on the template form.

If the quotation is for a recurring product or subscription, select the desired Recurring
Plan from that specific drop-down menu.

If desired, select a specific Pricelist to be applied to this quotation.

Lastly, select any specific Payment Terms to be used for this quotation.

### Order Lines tab

The first tab on the quotation form is the Order Lines tab.

In this tab, select products, and quantities of those products, to add them to the quotation.

There are two ways to add products to the quotation from this tab.

Click Add a product, select the desired item from the Product drop-down
field, and proceed to adjust the quantity of that selected product, if necessary.

Or, click Catalog to reveal a separate page, showcasing every item (and every potential
product variant) in an organized catalog display, with items organizable by Product
Category and Attributes.

![A product catalog accessible via a quotation in the Odoo Sales application.](../../../../_images/product-catalog.png)

From here, simply locate the desired items, click the  Add
button on the product card, and adjust the quantity, if needed. When complete, click the
Back to Quotation button in the upper-left corner to return to the quotation, where the
newly-selected catalog items can be found in the Order Lines tab.

If multiple items should be presented in a more organized way on the quotation, click Add
a section, enter a name for the section, and drag-and-drop that section heading in the desired
location amongst the items in the Order Lines tab. The section heading appears in bold
and a sub-total for all products in a section is displayed.

If needed, click Add a note beneath a certain product line to add a custom note about
that specific product. The note appears in italics. Then, if needed, proceed to drag-and-drop the
note beneath the desired product line.

Beneath the product lines, there are buttons that can be clicked to apply any of the following:
Coupon Code, Promotions, Discount, and/or Add
shipping.

> **Note:**
>
> - [Use eWallets and gift cards](../products_prices/ewallets_giftcards.html)
> - [Discount and loyalty programs](../products_prices/loyalty_discount.html)
> - [Pricelists](../products_prices/prices/pricing.html)

### Optional Products tab

Open the Optional Products tab to select related products that can be presented to the
customer, which may result in an increased sale.

For example, if the customer wants to buy a car, an optional product that could be offered is a
*Trailer Hitch*.

> **Note:**
>
> [Optional products](optional_products.html)

### Other Info tab

In the Other Info tab, there are various quotation-related configurations separated into
four different sections: Sales, Delivery, Invoicing, and
Tracking.

> **Note:**
>
> Some fields **only** appear if specific settings and options have been configured.

#### Sales section

In the Sales section of the Other Info tab, there are sales specific fields
that can be configured.

![The Sales section of the Other Info tab of a quotation form in Odoo Sales.](../../../../_images/other-info-sales.png)

- Salesperson: Assign a salesperson from the drop-down menu to be associated with this
  quotation. The user who originally created the quotation is selected in this field, by default.
- Sales Team: Assign a specific sales team to this quotation. If the selected
  Salesperson is a member of a sales team, that team is auto-populated in the field.
- Company: Select a company from the drop-down menu this quotation should be associated
  with. This field only appears when working in a multi-company environment.
- Online signature: Tick this checkbox to request an online signature from the customer
  to confirm the order. This field only appears if the *Online Signature* setting has been enabled.
- Online payment: Tick this checkbox, and enter a desired percentage in the adjacent
  field, to request an online payment from the customer (for that designated percentage of the total
  amount) to confirm the order. This field only appears if the *Online Payment* setting has been
  enabled.
- Customer Reference: Enter a custom reference ID for this customer. The entered
  reference ID can contain letters, numbers, or a mix of both.
- Tags: Add specific tags to the quotation for added organization and enhanced
  searchability in the Odoo **Sales** application. Multiple tags can be added, if necessary.

#### Delivery section

In the Delivery section of the Other Info tab, there are delivery-specific
fields that can be configured.

![The Delivery section of the Other Info tab of a quotation form in Odoo Sales.](../../../../_images/other-info-delivery.png)

- Shipping Weight: Displays the weight of the items being shipped. This field is not
  modifiable. Product weight is configured on individual product forms.
- Incoterm: Select an Incoterm (International Commerical Term) to use as predefined
  commerical terms for international transactions.
- Incoterm Location: If an Incoterm is being used, enter the international location in
  this field.
- Shipping Policy: Select a desired shipping policy from the drop-down menu. If all
  products are delivered at once, the delivery order is scheduled, based on the greatest product
  lead time. Otherwise, it is based on the shortest lead time. The available options are:
  As soon as possible or When all products are ready.
- Delivery Date: Click into the empty field to reveal a calendar popover, from which a
  customer delivery date can be selected. If no custom date is required, refer to the
  Expected date listed to the right of that field.

#### Invoicing section

In the Invoicing section of the Other Info tab, there are invoicing specific
fields that can be configured.

![The Invoicing section of the Other Info tab of a quotation form in Odoo Sales.](../../../../_images/other-info-invoicing.png)

- Fiscal Position: Select a fiscal position to be used to adapt taxes and accounts for
  particular customers or sales orders/invoices. The default value comes from the customer. If a
  selection is made in this field, an  Update Taxes clickable link and
  icon appear. When clicked, the taxes for this partiuclar customer and quotation are updated. A
  confirmation window appears, as well.
- Analytic Account: Select an analytic account to apply to this customer/quotation.

#### Tracking section

In the Tracking section of the Other Info tab, there are tracking specific
fields that can be configured.

![The Tracking section of the Other Info tab of a quotation form in Odoo Sales.](../../../../_images/other-info-tracking.png)

- Source Document: Enter the reference of the document that generated the
  quotation/sales order, if applicable.
- Opportunity: Select the specific opportunity (from the **CRM** app) related to this
  quotation, if applicable.
- Campaign: Select the marketing campaign related to this quotation, if applicable.
- Medium: Select the method by which this quotation originated (e.g. *Email*), if
  applicable.
- Source: Select the source of the link used to generate this quotation (e.g.
  *Facebook*), if applicable.

> **Note:**
>
> [Link tracker](../../../websites/website/reporting/link_tracker.html)

### Notes tab

In the Notes tab of the quotation form, enter any specific internal notes about the
quotation and/or customer, if desired.

## Sending and confirming quotations

Once all the necessary fields and tabs have been configured, it is time to send the quotation to the
customer for confirmation. Upon confirmation, the quotation turns into an official sales order.

At the top of the form, there is a series of buttons:

- Send by Email: When clicked, a pop-up window appears with the customer’s name and
  email address in the Recipients field, the quotation (and reference ID) in the
  Subject field, and a brief default message in the body of the email, which can be
  modified, if needed.

  Below that, a PDF copy of the quotation is attached. When ready, click Send to send
  the quotation, via email, to the customer, so they can review and confirm it.
- Send PRO-FORMA Invoice: This button **only** appears if the *Pro-Forma Invoice*
  setting has been enabled. When clicked, a pop-up window appears with the customer’s name and email
  address in the Recipients field, the *Proforma* invoice (and reference ID) in the
  Subject field, and a brief default message in the body of the email, which can be
  modified, if needed.

  Below that, a PDF copy of the quotation is attached. When ready, click Send to send
  the quotation, via email, to the customer, so they can review and confirm it.
- Confirm: When clicked, the quotation is confirmed, and the status changes to
  Sales Order.
- Preview: When clicked, Odoo reveals a preview of the quotation the customer sees when
  they log into their customer portal. Click the  Back to edit
  mode link at the top of the preview page, in the blue banner, to return to the quotation form.
- Cancel: When clicked, the quotation is canceled.

> **Note:**
>
> If the *Lock Confirmed Sales* setting is enabled, the sales order becomes Locked, and
> is indicated as such on the sales order form.

At this point, the quotation has been confirmed, turned into a sales order, and is now ready to be
invoiced and paid for.

For more information about invoicing, refer to the [Invoice based on delivered or ordered
quantities](../invoicing/invoicing_policy.html)

> **Note:**
>
> - [Quotation templates](quote_template.html)
> - [Quotation deadlines](deadline.html)
> - [Online signatures for order confirmations](get_signature_to_validate.html)
> - [Online payment order confirmation](get_paid_to_validate.html)
> - [PDF quote builder](pdf_quote_builder.html)
> - [Pro-forma invoices](../invoicing/proforma.html)

---

# Quotation templates

Reusable quotation templates can be made in Odoo’s **Sales** app for common products or services.

By using these templates, quotations can be tailored and sent to customers at a quicker pace,
without having to create new quotations from scratch every time a sales negotiation occurs.

## Configuration

To use quotation templates, begin by activating the setting in Sales app ‣
Configuration ‣ Settings, and scroll to the Quotations \_Orders heading.

Under the heading, tick the Quotation Templates checkbox. Doing so reveals a new
Default Template field, in which a default quotation template can be chosen from the
drop-down menu.

![How to enable quotation templates on Odoo Sales.](../../../../_images/quotations-templates-setting.png)

Upon activating the Quotation Template feature, an internal
Quotation Templates link appears beneath the Default Template field.

Clicking this link reveals the Quotation Templates page, from which templates can be
created, viewed, and edited.

Before leaving the Settings page, do not forget to click the Save button to
save all changes made during the session.

## Create quotation templates

To create a quotation template, click the Quotation Templates link on the
Settings page once Quotation templates are enabled, or navigate to
Sales app ‣ Configuration ‣ Quotation Templates. Both options reveal the
Quotation Templates page, where quotation templates can be created, viewed, and edited.

![Quotation templates page in the Odoo Sales application.](../../../../_images/quotation-templates-page.png)

To create a new quotation template, click the New button, located in the upper-left
corner. Doing so reveals a blank quotation template form that can be customized.

![Create a new quotation template on Odoo Sales.](../../../../_images/blank-quotation-form.png)

Start by entering a name for the template in the Quotation Template field.

Then, in the Quotation Validity field, designate how many days the quotation template
will remain valid for, or leave the field on the default `0` to keep the template valid
indefinitely.

Next, in the Confirmation Mail field, click the blank drop-down menu to select a
preconfigured email template to be sent to customers upon confirmation of an order.

> **Note:**
>
> To create a new email template directly from the Confirmation Mail field, start
> typing the name of the new email template in the field, and select either: Create or
> Create and edit… from the drop-down menu that appears.
>
> Selecting Create creates the email template, which can be edited later.
>
> Selecting Create and edit… creates the email template, and a Create
> Confirmation Mail pop-up window appears, in which the email template can be customized and
> configured immediately.
>
> ![Create confirmation mail pop-up window from the quotation template form in Odoo Sales.](../../../../_images/create-confirmation-mail-popup.png)
>
> When all modifications are complete, click Save & Close to save the email template
> and return to the quotation form.

If working in a multi-company environment, use the Company field to designate to which
company this quotation template applies.

If a journal is set in the Invoicing Journal field, all sales orders with this template
will invoice in that specified journal. If no journal is set in this field, the sales journal with
the lowest sequence is used.

If the Online Signature and/or Online Payment features are activated in the
Settings (Sales app ‣ Configuration ‣ Settings), those options are
available on quotation template forms.

Check the box beside Online Signature to request an online signature from the customer
to confirm an order.

Check the box beside Online Payment to request an online payment from the customer to
confirm an order. When Online Payment is checked, a new percentage field appears, in
which a specific percentage of payment can be entered.

Both options, Online Signature and Online Payment can be enabled
simultaneously, in which case the customer must provide **both** a signature **and** a payment to
confirm an order.

### Lines tab

In the Lines tab, products can be added to the quotation template by clicking
Add a product, organized by clicking Add a section (and dragging/dropping
section headers), and further explained with discretionary information (such as warranty details,
terms, etc.) by clicking Add a note.

To add a product to a quotation template, click Add a product in the Lines
tab of a quotation template form. Doing so reveals a blank field in the Product column.

When clicked, a drop-down menu with existing products in the database appears. Select the desired
product from the drop-down menu to add it to the quotation template.

If the desired product is not readily visible, type the name of the desired product in the
Product field, and the option appears in the drop-down menu. Products can also be found
by clicking Search More… from the drop-down menu.

> **Note:**
>
> It is possible to add event-related products (booths and registrations) to quotation templates.
> To do so, click the Product field, type in `Event`, and select the desired
> event-related product from the resulting drop-down menu.

> **Note:**
>
> When a product is added to a quotation template, the default Quantity is `1`, but
> that can be edited at any time.

Then, drag and drop the product to the desired position, via the six squares icon,
located to the left of each line item.

To add a *section*, which serves as a header to organize the lines of a sales order, click
Add a section in the Lines tab. When clicked, a blank field appears, in
which the desired name of the section can be typed. When the name has been entered, click away to
secure the section name.

Then, drag and drop the section name to the desired position, via the
(six squares) icon, located to the left of each line item.

To add a note, which appears as a piece of text for the customer on the quotation, click
Add a note in the Lines tab. When clicked, a blank field appears, in which
the desired note can be typed. When the note has been entered, click away to secure the note.

Then, drag and drop the note to the desired position, via the
(six squares) icon.

To delete any line item from the Lines tab (product, section, and/or note), click the
 (remove record) icon on the far-right side of the line.

### Optional Products tab

Using *optional products* is a marketing strategy that involves the cross-selling of products along
with a core product. The aim is to offer useful and related products to customers, which may result
in an increased sale.

> **Tip:**
>
> If a customer wants to buy a car, they have the choice to order massaging seats as
> an additional product that compliments the car, or ignore the offer and buy the car alone.

Optional products appear as a section on the bottom of sales orders and eCommerce pages. Customers
can immediately add them to their online sales orders themselves, if desired.

![Optional products appearing on a typical sales order with Odoo Sales.](../../../../_images/optional-products-on-sales-order.png)

In the Optional Products tab, Add a line for each cross-selling product
related to the original items in the Lines tab, if applicable.

Clicking Add a line reveals a blank field in the Product column.

When clicked, a drop-down menu with products from the database appear. Select the desired product
from the drop-down menu to add it as an optional product to the quotation template.

To delete any line item from the Optional Products tab, click the
(remove record) icon.

> **Note:**
>
> Optional products are **not** required to create a quotation template.

### Terms & Conditions tab

The Terms & Conditions tab provides the opportunity to add terms and conditions to the
quotation template. To add terms and conditions, type the desired terms and conditions in this tab.

> **Note:**
>
> [Default terms and conditions (T&C)](../../../finance/accounting/customer_invoices/terms_conditions.html)

> **Note:**
>
> Terms and conditions are **not** required to create a quotation template.

## Use quotation templates

When creating a quotation (Sales app ‣ New), choose a preconfigured template in
the Quotation Template field.

> **Note:**
>
> The order of the templates in the Quotation Template field is determined by the order
> of the templates in the Quotation Templates form. The order of the quotations in the Quotation
> Templates form does **not** affect anything else.

To view what the customer will see, click the Preview button at the top of the page to
see how the quotation template appears on the front-end of the website through Odoo’s customer
portal.

![Customer preview of a quotation template in Odoo Sales.](../../../../_images/quotations-templates-preview.png)

When all blocks and customizations are complete, click the Save button to save the
configuration.

The blue banner located at the top of the quotation template preview can be used to quickly return
 Back to edit mode. When clicked, Odoo returns to the quotation
form in the back-end of the *Sales* application.

## Mass cancel quotations/sales orders

Cancel multiple quotations (or sales orders) by navigating to the Sales app ‣
Orders ‣ Quotations dashboard, landing, by default, in the list view. Then, on the left side of
the table, tick the checkboxes for the quotations to be canceled.

> **Note:**
>
> Select all records in the table by selecting the checkbox column header at the top-left of the
> table; the total number of selected items are displayed at the top of the page.

Then, with the desired quotations (or sales orders) selected from the list view on the
Quotations page, click the  Actions button to reveal a
drop-down menu.

From this drop-down menu, select Cancel quotations.

![The Cancel quotations option on the Actions drop-down menu in the Odoo Sales application.](../../../../_images/cancel-quotations.png)
> **Note:**
>
> This action can be performed for quotations in *any* stage, even if it is confirmed as a sales
> order.

Upon selecting the Cancel quotations option, a Cancel quotations
confirmation pop-up window appears. To complete the cancellation, click the Cancel
quotations button.

> **Note:**
>
> An error pop-up message appears when attempting to cancel an order for an ongoing subscription
> that has an invoice.

> **Note:**
>
> - [Online signatures for order confirmations](get_signature_to_validate.html)
> - [Online payment order confirmation](get_paid_to_validate.html)

---

# Margins

The sales margin is the profit gained from the sale of a product or service after all the costs
related to it have been accounted for.

In the Odoo **Sales** application, it is possible to show sales margins on quotations and sales
orders. Salespeople can use the feature for better management and monitoring of profitability.

## Configuration

To activate the *Margins* feature, go to the Sales app ‣ Configuration ‣
Settings. In the Pricing section, tick the Margins checkbox. Then click
Save.

![Margins checkbox.](../../../../_images/margins-checkbox.png)

### Configure price and cost

To automatically calculate the sales margin for each quotation or sales order line item, go to
Sales app ‣ Products ‣ Products. Fill out the Sales Price and
Cost fields in the General Information tab for every product.

Odoo calculates the margin by:

\[Sales~Margin = Sales~Price - Cost\]

The margin percentage is calculated by:

\[\frac{Sales~Price - Cost~Price}{Sales~Price} \times 100\]

![Cable Management box product page.](../../../../_images/product-view.png)

## Compute margins on sales orders

Go to Sales app ‣ Orders ‣ Quotations and click the New button to
begin a new quotation. Fill out the quotation with the necessary information. While adding products
to the quotation, a new field, Margin, automatically appears at the bottom of the
document. This field displays the order’s total margin in the configured currency as well as the
percentage.

![Sales order with Margin field on the bottom.](../../../../_images/so-with-margin-field.png)

To display a product’s margin and the margin percentage per line item, click the
 (settings adjust) icon in the Order Lines tab.

Then, tick the checkboxes for Margin and Margin(%). The Margin
column shows the profit to earn from the sale after accounting for all associated costs. It displays
in the configured currency value. The Margin(%) shows the margin value as a percentage.
The margin for one unit is multiplied by the quantity to determine the margin for the entire line.

The Margin and Margin(%) columns are not displayed by default, but once
enabled, the columns appear on all new and existing quotations and SOs.

![Sales order with Margin and Margin(%) columns displayed.](../../../../_images/so-with-margins-checkboxes.png)
> **Note:**
>
> The Margin and Margin (%) columns are not editable since they are
> automatic calculations. To change the calculation, refer to [Configure price and cost] section for more information.

## Margin calculation with a pricelist

To calculate the margin with an applied pricelist, begin with configuring a pricelist for the
product. Follow these steps:

1. Go to Sales app ‣ Products ‣ Pricelists and click the New
   button.
2. Enter the name of the pricelist and click Add a line to create a new pricelist rule.
3. Configure the pricelist and click Save & Close button.
4. Go to Sales app ‣ Orders ‣ Quotations and create a quotation.
5. In the Pricelist field, select the newly made pricelist.
6. Click on Update Prices to refresh the product price and margin.

> **Tip:**
>
> To apply a seasonal 5% discount on blue denim jeans that requires a minumim of two pairs of jeans
> in an order and is valid only from October to the end of December, the pricelist rule should look
> like this:
>
> ![Pricelist Rules pop-up window.](../../../../_images/pricelist-configuration.png)
>
> After saving the pricelist, go to the desired SO and select the newly
> created pricelist, and adjust the quantity according to the pricelist’s rule.
>
> ![Sales order with a new pricelist selected.](../../../../_images/so-with-pricelist.png)
>
> After the changes are made, click  Update Prices to update the
> Margin, Margin (%), and Amount. The margin is recalculated
> based on the pricelist-adjusted product’s sales price and cost.
>
> ![Sales order with margins recalculated based on the price-list adjustment.](../../../../_images/so-with-applied-pricelist.png)

> **Note:**
>
> Another way to visualize the impact of margins on sales orders is to go to Sales
> app ‣ Orders ‣ Quotations, select the  (area chart) icon or
>  (pivot) icon, click Measures drop-down button and
> change it to Margin to see margin contributions across the customer base.

---

# Optional products

The use of optional products is a marketing strategy that involves the cross-selling of useful and
related products alongside a desired core product. For instance, when a business configures optional
products in their Odoo database, an eCommerce or Website customer could be suggested a mouse and
keyboard or an extended warranty when they add a laptop to their shopping cart.

Optional products are automatically suggested during the quotation process whenever an associated
core product is added to a quote. They are also suggested in eCommerce interactions when a customer
adds an associated core product to their shopping cart.

> **Note:**
>
> Optional products differ from [accessory and alternative products](../../../websites/ecommerce/configuration/products.html#ecommerce-products-cross-upselling) in terms of where they are displayed during the customer’s
> online shopping journey.

![A screen from the quotation process shows how optional products appear as a pop-up window.](../../../../_images/optional-products-quotation.png)

Optional products as they appear during the quotation process.

## Configuring optional products

With the Odoo **Sales** app, it is possible to add optional products directly to product forms. To
add an optional product to a product form, navigate to Sales ‣ Products ‣
Products and choose a product.

Ensure that the product’s Sales checkbox is checked and click the Sales tab.
Under Upsell & Cross-sell heading, the Optional Products drop-down menu
allows for optional products to be set. Products will be displayed in alphabetical order. If the
desired product isn’t readily visible, type its name in the field to bring it up, then select it to
add it as an optional product.

To delete an optional product from the product form, simply click the
(Delete) icon.

![Where the optional products section appears in product forms in Odoo Sales.](../../../../_images/optional-products-product-form.png)

Additional products can also be added to a core product by clicking Search more…. This
opens the Search: Optional Products form, which displays all products in the catalog and
includes the New button to create a new product. Multiple products may be selected as
optional products at once when using this form by clicking their checkboxes and then clicking
Select.

![The Search: Optional Products form accessed by clicking Search more...](../../../../_images/search-optional-products-form.png)

## Setting optional product sections in quotations

When developing a quotation for customers, entire sections of the quotation can be set as optional
products, even if they haven’t been configured in the product form. To create a section, click the
Add a section link and enter its desired name in the Enter a description
field. Click the  (drop-down menu) and choose
Set Optional.

![The dropdown menu with the "Set Optional" text highlighted.](../../../../_images/set-optional-dropdown.png)

Once a section is set to optional, the font color changes to reflect its status. All products within
that section default to a quantity of `0`, ensuring they are not included in the total cost
automatically. Both portal users (such as customers or vendors) and employees with access to create
quotations and sales orders can update these quantities. Once a quantity is set to `1` or more, the
product is added to the quote total.

Once an optional product section has been created in a quotation, users who have been [granted
portal access](../../../general/users/user_portals/portal_access.html) can interact with the quotation
there. They can view the quotation and decide whether or not to add the optional products to their
final sales order.

![An optional products section with the quanitty and corresponding amount set to 0.](../../../../_images/optional-products-section.png)
> **Note:**
>
> [Quotation templates](quote_template.html)

---

# Online signatures for order confirmations

The Odoo **Sales** application provides customers with the ability to confirm orders, via an online
signature, directly on the sales order. Once the sales order is electronically signed by the
customer, the salesperson attached to the sales order is instantly notified that the order is
confirmed.

## Activate online signatures

In order to have customers confirm orders with an online signature, the *Online Signature* feature
**must** be activated.

To activate the *Online Signature* feature, go to Sales app ‣ Configuration ‣
Settings, scroll to the Quotations & Orders heading, and activate the
Online Signature feature by checking the box beside it.

![The Online Signature feature option in the Settings of the Odoo Sales application.](../../../../_images/signature-setting.png)

Then, click the Save button in the top-left corner.

> **Note:**
>
> When making a quotation template, the online signature feature is the Signature
> option, located in the Online confirmation field of the quotation template form.
>
> ![The Online confirmation signature option found on every quotation template in Odoo.](../../../../_images/signature-feature-quotation-template.png)
>
> On standard quotations, the online signature feature is the Signature option, located
> under the Other Info tab of the quotation form.
>
> ![The online signature feature option in the Other Info tab of a quotation form in Odoo.](../../../../_images/signature-other-info-tab.png)

## Order confirmations with online signatures

When clients access quotations online through their customer portal, there’s a Sign &
Pay button directly on the quotation.

![The Sign and Pay button present on online quotations in Odoo Sales.](../../../../_images/sign-and-pay-button.png)

When clicked, a Validate Order pop-up window appears. In this pop-up window, the
Full Name field is auto-populated, based on the contact information in the database.

![The Validate Order pop-up window for online signatures in Odoo Sales.](../../../../_images/validate-order-popup.png)

Then, customers have the option to enter an online signature with any of the following options:
Auto, Draw, or Load.

Auto lets Odoo automatically generate an online signature based on the information in
the Full Name field. Draw lets the customer use the cursor to create a
custom signature directly on the pop-up window. And Load lets the customer upload a
previously-created signature file from their computer.

After the customer has chosen any of the three previously mentioned signature options
(Auto, Draw, or Load), they will click the Accept &
Sign button.

When Accept & Sign is clicked, the various payment method options become available for
them to choose from (if the *online payment* option applies to this quotation).

Then, when the quotation is paid and confirmed, a delivery order is automatically created (if the
Odoo **Inventory** app is installed).

### View online signatures in Developer Mode

Clients can view the online signature in [developer mode](../../../general/developer_mode.html#developer-mode).

To view a online signature from a paid invoice, go to Sales app ‣ Orders ‣
Orders and select the desired sales order. A new tab, Customer Signature, is available.
Click the tab to view the electronic signature as well as the Signed By and
Signed On information.

![The Customer Signature tab on a sales order when in Developer Mode.](../../../../_images/customer-signature-tab.png)
> **Note:**
>
> - [Quotation templates](quote_template.html)
> - [Online payment order confirmation](get_paid_to_validate.html)

---

# Online payment order confirmation

The Odoo *Sales* application provides customers with the ability to confirm orders, via an online
payment, directly on a sales order. Once the sales order is electronically paid for by the customer,
the salesperson attached to the sales order is instantly notified that the order is confirmed.

## Activate online payments

In order to have customers confirm orders with an online payment, the *Online Payment* setting
**must** be activated.

To activate the *Online Payment* feature, go to Sales app ‣ Configuration ‣
Settings, scroll to the Quotations & Orders heading, check the box next to the
Online Payment feature, and click Save.

![The online payment setting in the Odoo Sales application.](../../../../_images/online-payment-setting.png)

Beneath the Online Payment option on the *Sales* Settings page, there’s a
Default Quotation Validity field. In this field, there’s the option to add a specific
number of days for quotations to remain valid by default.

To enable this feature on a standard quotation, click the checkbox for the Payment
feature option, located in the Online confirmation field, on the Other Info
tab.

![The online payment setting on a standard quotation in Odoo Sales.](../../../../_images/online-payment-option-quotation.png)

To enable this feature on a quotation template, click the checkbox for the Payment
feature option, located in the Online confirmation field of the quotation template form.

![The online payment setting on quotation template forms in Odoo Sales.](../../../../_images/online-payment-option-quotation-template.png)

## Payment providers

After activating the Online Payment feature, a link to configure Payment
Providers appears beneath it.

Clicking that link reveals a separate Payment Providers page, in which a large variety
of payment providers can be enabled, customized, and published.

![Payment providers page in Odoo Sales.](../../../../_images/payment-providers-page.png)
> **Note:**
>
> [Online payments](../../../finance/payment_providers.html)

## Register a payment

After opening quotations in their customer portal, customers can click Accept & Pay to
confirm their order with an online payment.

![The accept and pay button on an online quotation in Odoo Sales.](../../../../_images/accept-and-pay-button.png)

After clicking Accept & Pay, customers are presented with Validate Order
pop-up window containing different options for them to make online payments, in the Pay
with section.

![How to register a payment on a validate order pop-up window in Odoo Sales.](../../../../_images/validate-order-pay-with.png)
> **Note:**
>
> Odoo will **only** offer payment options on the Validate Order pop-up window that
> have been published and configured on the Payment Providers page.

Once the customer selects their desired method of payment, they will click the Pay
button on the pop-up window to confirm the order. Odoo instantly notifies the assigned salesperson
upon order confirmation with an online payment.

![Sample of notification that appears in the chatter when an online payment is made.](../../../../_images/payment-confirmation-notification-chatter.png)
> **Note:**
>
> - [Quotation templates](quote_template.html)
> - [Online signatures for order confirmations](get_signature_to_validate.html)
> - [Online payments](../../../finance/payment_providers.html)

---

# Quotation deadlines

In the Odoo *Sales* application, it is possible to set deadlines on sales quotations. Doing so
encourages customers to act quickly during sales negotiations, for they might fear for missing out
on a good deal. As well, deadlines also can also act as protection for a company in case an order
has to be fulfilled at a price that is no longer profitable for the business.

## Quotation expiration

In Odoo *Sales*, there’s the option to add an expiration date to a quotation.

To add an expiration date to a quotation, navigate to Sales app, and select a
desired quotation, or create a new one by clicking New.

On the quotation form, click the Expiration field to reveal a pop-up calendar. From this
pop-up calendar, select the desired month and date as the expiration date for the quotation.

![The expiration field on a standard quotation form in Odoo Sales.](../../../../_images/quotation-deadlines-expiration-field.png)
> **Note:**
>
> By clicking the Preview button on a quotation, Odoo clearly displays when that
> specific offer expires.
>
> ![How customers will see deadlines on Odoo Sales.](../../../../_images/quotation-deadlines-preview.png)

## Quotation template expiration

The Odoo *Sales* application also makes it possible to add a deadline expiration date to quotation
templates.

To add a deadline expiration date to a quotation template, navigate to Sales app ‣
Configuration ‣ Quotation Templates, and either select the desired quotation template to which a
deadline should be added, or click New to build a new quotation template from scratch.

On the quotation template form, add a specific number of days to the Quotation expires
after field, located beneath the quotation template name. The number of days represents how long
the quotation will be valid for, before it expires.

![The quotation expires after field on a quotation template form in Odoo Sales.](../../../../_images/quotation-deadlines-expires-after.png)

Then, whenever that specific quotation template is used in a quote, an expiration date is
automatically calculated, based on the number of days designated above. However, this date can be
overwritten before sending the quotation to the customer.

> **Note:**
>
> [Quotation templates](quote_template.html)

---

# Deliveries and invoices to different addresses

People and businesses often use separate addresses for billing (invoicing) and shipping (delivery)
purposes. With the Odoo **Sales** app, contacts can have different specified addresses for delivery
and invoicing.

## Settings

To properly utilize multiple addresses in Odoo, go to the Accounting app ‣
Configuration ‣ Settings, and scroll down to the Customer Invoices heading. Then,
tick the Customer Addresses checkbox.

![Activate the Customer Addresses setting.](../../../../_images/customer-addresses-setting.png)

## Contact form configuration

To add multiple addresses to a contact, go to the Sales app ‣ Orders ‣
Customers, and clear any default filters from the search bar. Then, click on the desired customer
to open their contact form.

> **Note:**
>
> Contact forms can be accessed in the **Contacts** application, as well.

From the contact form, click the Add Contact button, which is located under the
Contacts tab. This brings up the Create Contact pop-up form, in which
additional addresses can be configured.

![Add a contact/address to the contact form.](../../../../_images/contact-form-add-address1.png)

On the Create Contact pop-up form, select any of the following options:

- Contact: Adds another contact, such as an employee at a company, to the contact form.
- Invoice: Adds a default invoice address to the contact form.
- Delivery: Adds a default delivery address to the contact form.
- Other Address: Adds an alternate address to the contact form.

![Create a new contact/address on a contact form.](../../../../_images/create-contact-window1.png)

Once the corresponding information has been entered, click Save & Close to save the
address and close the Create Contact window. To save the address and input additional
contact information, click Save & New instead.

## Quotations and autopopulated addresses

When a customer with invoice and delivery addresses in their contact form is added to a quotation,
the Invoice Address and Delivery Address fields autopopulate with the
corresponding addresses.

![Invoice and Delivery Addresses autopopulate on a quotation.](../../../../_images/quotation-address-autopopulate.png)

The Invoice Address and Delivery Address can also be edited directly from
the quotation by mousing over the address and clicking the
(Internal Link) icon.

---

# Product variants on quotations and sales orders

Before getting into detail about how to use product variants on quotations and sales orders, it’s
recommended to learn about [Product variants](../products_prices/products/variants.html) in Odoo.

Once familiarized with the basics surrounding product variants, the following covers how product
variants can be added to quotations and sales orders using the *product configurator* or *order grid
entry*.

> **Note:**
>
> It should be noted that the setting is titled, *Variant Grid Entry* on the *Sales* app settings
> page, and titled, *Order Grid Entry* on product forms. So, be sure to keep that in mind.

## Settings

When working with product variants, Odoo uses the product configurator, by default. To add the
variant grid entry option, that feature **must** be enabled in the Odoo *Sales* application. The
variant grid entry option provides a pop-up window on the quotation/sales order to simplify the
variant selection process.

To enable that setting, go to Sales app ‣ Configuration ‣ Settings, and scroll
to the Product Catalog section. Then, check the box next to the Variant Grid
Entry option, and click Save.

![The variant grid entry setting in the Odoo Sales application.](../../../../_images/order-grid-entry-setting.png)
> **Note:**
>
> Of course, the Variants feature **must** also be activated, in order to use product
> variants on quotations and sales orders.

## Product configuration

Once the Variant Grid Entry setting is enabled, both options (*Product Configurator* and
*Order Grid Entry*) become available on every product form.

To configure a product form to use either a product configurator or variant grid entry, start by
navigating to Sales app ‣ Products ‣ Products to view all the products in the
database.

Then, select the desired product to configure, or click New, to create a new product
from scratch. Once on the product form, click into the Attributes & Variants tab, where
product variants can be viewed, modified, and added.

At the bottom of the Attributes & Variants tab, there is a Sales Variant
Selection section with two options: Product Configurator and Order Grid
Entry.

> **Note:**
>
> It should be noted that these options **only** appear if at least two values of an attribute have
> been added to the record.

![Sales variant selection options on the attributes and variants tab on product form.](../../../../_images/attributes-variants-tab-selection-options.png)

These options determine which method is used when adding product variants to quotations or sales
orders.

The Product Configurator provides a pop-up window that neatly displays all the available
product variants for that particular product when it’s added to a quotation. However, only one
variant can be selected/added at a time.

The Order Grid Entry provides the same information as the Product
Configurator in a table layout, allowing the user to select larger numbers of unique product
variants, and add them to a quotation/sales order, in a single view.

## Product configurator

The product configurator feature appears as a Configure pop-up window, as soon as a
product with (at least two) variants is added to a quotation or sales order, but **only** if the
Product Configurator option is selected on its product form.

![The product configurator pop-up window that appears on a quotation or sales order.](../../../../_images/product-configurator-window.png)
> **Note:**
>
> This Configure pop-up window also appears if the Order Grid Entry setting
> is **not** activated, as it is the default option Odoo uses when dealing with product variants on
> quotations and/or sales orders.

The Product Configurator option lets salespeople choose exactly which product variant to
add to the quotation or sales order using a format similar to online shopping.

## Order grid entry

The order grid entry feature appears as a Choose Product Variants pop-up window, as soon
as a product with (at least two) variants is added to a quotation or sales order, but **only** if
the Order Grid Entry option is selected on its product form.

![The choose product variants pop-up window that appears on a quotation in Odoo.](../../../../_images/choose-product-variants-popup.png)

The Choose Product Variants pop-up window features all the variant options for that
particular product. From this pop-up window, the salesperson can designate how many of each variant
they’d like to add to the quotation/sales order at once.

When all the desired quantities and variants have been selected, the salesperson simply clicks
Confirm, and those orders are instantly added to the quotation/sales order in the
Order Lines tab.

![Populated order lines tab after order grid entry has been chosen to select products.](../../../../_images/order-grid-entry-order-lines-tab.png)
> **Note:**
>
> [Product variants](../products_prices/products/variants.html)

---

# PDF quote builder

The *PDF Quote Builder* in Odoo **Sales** app provides the opportunity to send customers a fully
customized PDF file for quotes, showcasing the company and products, with various information and
design elements, instead of showing the price and total.

The PDF Quote Builder groups header pages, product descriptions, prices, and footer pages to create
a detailed quote. It can also inject dynamic texts or custom notes in the PDF to personalize the
offer for the customer.

Having a customized PDF in quotes provides a heightened conclusion to the shopping experience for
customers, and adds an elegant level of professionalism to a company.

> **Note:**
>
> [Odoo Quick Tips - Create a PDF quote [video]](https://www.youtube.com/watch?v=tQNydBZt-VI)

> **Note:**
>
> It is recommended to edit PDF forms with Adobe software. The form fields on the header and footer
> PDF templates are necessary to get dynamic values with Odoo.

[#### Add dynamic text to PDFs

Add dynamic text fields to PDFs.](pdf_quote_builder/dynamic_text.html)[#### Add PDFs to quotes

Add a PDF header or footer to a quote.](pdf_quote_builder/add_pdf_quotes.html)[#### Add PDFs to products

Set up the headers and footers for products. These will appear on sales quotes and online
store pages.](pdf_quote_builder/add_pdf_products.html)

## Configuration

In order to add custom PDF files for quotes, the PDF Quote builder feature *must* be
configured.

To do that, navigate to Sales app ‣ Configuration ‣ Settings and scroll to the
Quotations & Orders section. Tick the PDF Quote builder checkbox feature,
then click Save.

Once enabled, a  (right arrow) icon for
Headers/Footers appears beneath it.

## Add PDF as Header/Footer

> **Warning:**
>
> Odoo does **not** allow PDF field names to have a space in them. Only use alphanumerics, hyphens,
> or underscores.

In Odoo **Sales** app allows for the addition a custom PDF, which serves as either as a header or a
footer. Activating the PDF quote builder in a quotation, enables the selection of multiple headers
and footers, which are inserted into the final PDF.

To add a custom PDF as header or footer, start by navigating to Sales app ‣
Configuration. Click the  (right arrow) icon for
Headers/Footers and all available templates appear in a default Kanban view.

Click New or Upload. Clicking Upload instantly provides the
opportunity to upload the desired document.

Then, the document can be further configured on the document card, or by clicking the
 (vertical ellipsis) icon in the top-right corner of the document
card, and then clicking Edit.

Clicking New reveals a blank documents form, in which the desired PDF can be uploaded
via the Upload your file button on the form, located in the File Content
field.

Various information and configurations related to the uploaded document can be modified here.

The first field on the documents form is for the Name of the document, and it is
grayed-out (not clickable) until a document is uploaded. Once a PDF has been uploaded, the
Name field is auto-populated with the name of the PDF, and it can then be edited.

Then, in the Document Type field, click the drop-down menu, and select either:
Header, or Footer to define whether these files are selectable at the
beginning or at the end of the quote.

Under this, in the Quotation Templates section, this PDF can be restricted quotation
templates only.

> **Note:**
>
> Alternatively, you can also navigate to Sales app ‣ Configuration ‣ Quotation
> Templates, select a template and directly Add or Upload a PDF to it in
> the Quote Builder tab.

Lastly, beside the File Content field, you have the possibility to Configure
dynamic fields.

---

# Invoicing Method

---

# Invoicing policies

Depending on business needs, it may be advantageous to choose whether to invoice customers based on
the goods and services that they order or when those goods and services are delivered to them. To
allow businesses maximum flexibility to best meet their needs, Odoo offers two invoicing policies
that can be enabled in the **Sales** app: [Invoice what is ordered] and
[Invoice what is delivered].

- The *Invoice what is ordered* rule is used as the default mode in Odoo **Sales**, which means
  customers are invoiced once the sales order is confirmed.
- The *Invoice what is delivered* rule invoices customers once the delivery is done. This rule is
  often used for businesses that sell materials, liquids, or food in large quantities. In these
  cases, the ordered quantity may differ slightly from the delivered quantity, making it preferable
  to invoice the quantity actually delivered. When the delivery order is validated, Odoo will
  automatically decrease the on-hand quantity in the inventory.

To configure an invoicing policy, go to Sales app ‣ Configuration ‣ Settings,
and under the Invoicing heading, select an Invoicing Policy option:
Invoice what is ordered or Invoice what is delivered.

Activating an invoicing policy option automatically applies the chosen option to all newly created
products. Existing products **must** have their invoicing policy manually updated on their product
forms.

![Choosing an invoicing policy in the Sales app.](../../../../_images/invoicing-policy-setting.png)
> **Warning:**
>
> If the Invoice what is delivered option is chosen, it is **not** possible to activate
> the Automatic Invoice feature, which automatically generates invoices when an online
> payment is confirmed. Regular draft invoices can only be created once the delivery order has been
> processed and validated.

## Changing the invoicing policy for existing products

After the invoicing policy has been configured in *Settings*, navigate to a product’s form through
Sales app ‣ Products ‣ Products and choosing a product. Locate the
Invoicing Policy option located under the General Information tab. Use the
drop-down menu to change the policy.

![How to change invoicing policy on a product form in the **Sales** app.](../../../../_images/invoicing-policy-general-info-tab.png)

### Invoicing what is ordered

The *Invoice what is ordered* option is used as the default mode in the **Sales** app, which means
customers are invoiced once a quotation has been sent to the customer and confirmed. The creation of
a quotation in turn leads to the creation and confirmation of a sales order. An invoice can then be
created as soon as the sales order is confirmed.

This invoicing policy has no impact on the basic Odoo sales flow.

## Invoice ordered quantity workflow

Confirm that the product’s invoicing policy is set to Ordered quantities in the product
form. [Create a quotation and sales order](../sales_quotations/create_quotations.html#sales-create-quotation) as normal. After the sales
order has been confirmed, create an invoice by clicking the Create Invoice button on the
sales order form. Choose the type of invoice to be sent, click Create Draft Invoice,
confirm the invoice when ready, and proceed with the payment flow as normal.

> **Tip:**
>
> A independent artisan with a small business sells handmade jewelery nationwide online. Because
> they have direct control over their inventory levels and ship with 3rd party carriers, they
> invoice their customers after a sales order has been confirmed.
>
> The artisan receives an order for a necklace. They send their customer a quotation, confirm it,
> and create a sales order. After the sales order has been confirmed, an invoice can be created and
> sent to the customer for payment without any additional steps be taken. The invoice gets paid,
> the necklace is shipped and delivered, and the transaction is complete.

### Invoicing what is delivered

The *Invoice what is delivered* option invoices customers as different amounts of the ordered goods
are delivered. This option is often used for businesses that sell large quantities of physical goods
in each sales order, but may not always be able to completely fulfill a given order all at once. In
these cases, the ordered quantity may differ slightly from the delivered quantity based on product
availability. Once a quotation is confirmed, and the status changes from Quotation sent
to Sales order, Odoo automatically adds both the delivered and invoiced quantities to
the invoice and sales order. Both partial and complete deliveries are tracked. [Backorders](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/multipack.html#inventory-shipping-backorders) can be created for partial orders that will be completed at a later
time.

This invoicing policy has a minor impact on the sales flow because the delivered quantity of a
product needs to be manually entered on the sales order.

![How to see delivered and invoiced quantities on Odoo Sales.](../../../../_images/invoicing-policy-order-lines.png)

## Invoice delivered quantity workflow

Confirm that the product’s invoicing policy is set to Delivered quantities in the
product form. [Create a quotation and sales order](../sales_quotations/create_quotations.html#sales-create-quotation) as normal. After
the sales order has been confirmed, the product must be delivered before an invoice can be created.

Once the product has been shipped and delivery has been confirmed, click the Delivery
smart button on the sales order screen and click Validate to validate the delivery
order. Once at least a partial delivery has been confirmed, return to the sales order form. The
Create Invoice button is now purple to indicate that an invoice can be created and
confirmed, and that it is possible to proceed with the payment flow as normal.

> **Warning:**
>
> If a user attempts to create an invoice without validating the delivered quantity, the system
> returns an error message alerting them to the issue.
>
> ![If Delivered Quantities invoicing policy is chosen, ensure a quantity has been delivered.](../../../../_images/invoicing-policy-error-message.png)

> **Tip:**
>
> A produce distributor using the invoice what is delivered option sells 50 heads of lettuce to a
> local restaurant. At the time the delivery is made, only 40 heads are available. The distributor
> delivers the available heads of lettuce and creates an invoice for what was delivered. Later,
> when more supply comes in, the distributor delivers the remaning 10 heads of lettuce and creates
> a second invoice to complete the order.

> **Note:**
>
> - [Create quotations](../sales_quotations/create_quotations.html)
> - [Down payments](down_payment.html)
> - [Inventory](../../../inventory_and_mrp/inventory.html)
> - [Multi-package shipments](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/multipack.html)

---

# Down payments

A down payment is an initial up-front payment made during the confirmation of a sales transaction.
With a down payment, the buyer pays a portion of the total amount owed while agreeing to pay the
remaining amount at a later date. In turn, the seller provides goods or services to the buyer upon
or after accepting the down payment, trusting that the remaining amount will be paid later on.

In the Odoo **Sales** app, down payments can be customized to fit the needs of each individual sales
transaction.

## Create invoices

When a sales order is confirmed, the option to create an invoice becomes available via the
Create Invoice button. When clicked, a Create invoice(s) pop-up appears.

![Create invoice(s) pop-up form that appears in Odoo Sales.](../../../../_images/create-invoices-popup-form.png)
> **Note:**
>
> Invoices are automatically created as drafts so they can be reviewed before validation.

On the Create invoice(s) pop-up, there are 3 options to choose from in the
Create Invoice field:

- Regular invoice
- Down payment (percentage)
- Down payment (fixed amount)

## Initial down payment request

On the Create invoice(s) pop-up window, the down payment options are:

- Down payment (percentage)
- Down payment (fixed amount)

Select a down payment option and set the desired payment, either as a percentage or a fixed amount,
in the Down Payment Amount field.

Once all fields are filled in, click the Create Draft button. Upon clicking this button,
Odoo reveals the Customer Invoice Draft.

> **Warning:**
>
> If an Invalid Operation error appears, double-check that the [invoicing policy](invoicing_policy.html) is configured correctly. In some cases, for example, the invoicing policy is
> configured to require delivery before sending an invoice.

In the Invoice Lines tab of the Customer Invoice Draft, the down payment
that was just configured in the Create invoice(s) pop-up form appears under a new
Down Payments section.

## Example: requesting a 50% down payment

> **Note:**
>
> The following example involves a 50% amount down payment on a (Cabinet with Doors)
> with Ordered quantities as the Invoicing Policy.
>
> ![Cabinet with doors product form showcasing various details and fields.](../../../../_images/cabinet-product-details.png)

Navigate to Sales app ‣ New, and add a Customer to the quotation.
Then, click Add a product in the Order Lines tab, and select the
Cabinet with Doors product. When the order is confirmed (via the Confirm
button), the quotation turns into a sales order. Once this occurs, create and view the invoice by
clicking Create Invoice.

![Cabinet with doors sales order that's been confirmed in the Odoo Sales application.](../../../../_images/cabinet-sales-orders-confirmed.png)

Next, on the Create invoice(s) pop-up window that appears, select Down
payment (percentage), and type `50` in the Down Payment field.

> **Note:**
>
> The Income Account attached to the Down payment can be changed. For more
> information, check out the documentation on [income account modification on down payments]. A Down payment Account can also be
> set on a product category. If set, this account is prioritized for future down payments.

Lastly, click Create Draft Invoice to create and view the invoice draft, which includes
the down payment under the Down Payments section of the Invoice Lines tab.
From there, the invoice can be confirmed and posted by clicking Confirm. Confirming the
invoice changes the status from Draft to Posted. It also reveals a new
series of buttons at the top of the page.

![A sample draft invoice with down payment mentioned in Odoo Sales.](../../../../_images/draft-invoice-sample.png)

From those buttons, the payment can be registered by clicking Pay. Doing so reveals a
Pay pop-up form, which is auto-populated with the necessary information. Confirm the
information provided is correct, and make any necessary adjustments. When ready, click the
Create Payment button.

![Showcase of the Pay pop-up window with create payment button.](../../../../_images/register-payment-pop-up-window.png)

After clicking Create Payment, Odoo reveals the customer invoice, now with a green
In Payment or Paid banner in the upper-right corner, depending on how the
database has configured and if manual confirmation of payments is required.

![Customer Invoice with a green Paid banner located in the upper-right corner.](../../../../_images/customer-invoice-green-payment-banner.png)

On the sales order, a new Down Payments section is present in the Order
Lines tab, along with the down payment that was just invoiced and posted. When the customer wants
to pay the remaining amount of the order, another invoice must be created.

![The down payments section in the order lines tab of a sales order.](../../../../_images/down-payments-section-order-lines.png)

Next, click the Create Invoice button. On the Create invoice(s) pop-up
window that appears, there is a new field: Already invoiced and Amount to
invoice.

![The deduct down payment option on the Create invoice(s) pop up in Odoo Sales.](../../../../_images/create-invoices-pop-up-already-invoiced.png)

If the remaining amount is ready to be paid, select the Regular Invoice option. Odoo
will create an invoice for the exact amount needed to complete the total payment, as indicated in
the Amount to invoice field.

Once ready, click Create Draft Invoice. Doing so reveals another Customer
Invoice Draft page, listing all the invoices for that specific sales order in the
Invoice Lines tab. Each invoice line item displays all the necessary information related
to each invoice.

To complete the flow, click Confirm to change the status of the invoice from
Draft to Posted. Then, click Pay. The Pay form
appears, with all fields auto-populated with the necessary information, including the remaining
amount left to be paid on the order.

![The second Pay pop-up form in Odoo sales.](../../../../_images/second-register-payment-popup.png)

After confirming that information, click Create Payment. Doing so reveals the final
Customer Invoice with a green In Payment or Paid banner in the
upper-right corner, depending on how the database has configured and if manual confirmation of
payments is required. Upon returning to the sales order, both down payments are present in the
Order Lines tab.

![The second down payment invoice with Paid banner in Odoo Sales.](../../../../_images/final-sales-order.png)

At this point, the flow is now complete. This flow is also possible with the Fixed
amount down payment option.

> **Warning:**
>
> If a down payment is used with a product that has a Delivered quantities invoicing
> policy, and the cost of the product exceeds the 50% down payment, a regular invoice is created.
> However, for products that cost less than the 50% down payment, the down payments will not be
> able to be deducted when it comes time to invoice the customer. This is because the product(s)
> would have to be delivered *before* creating the final invoice due to Odoo not allowing negative
> totals for invoices. If nothing has been delivered, a Credit Note is created, which
> cancels the draft invoice that was created after the down payment.
>
> To utilize the Credit Note option, the **Inventory** application must be installed in
> order to confirm the delivery. Otherwise, the delivered quantity can be entered manually directly
> on the sales order.

## Example: requesting a 100% down payment

Requesting a 100% down payment is similar to requesting a [50% down payment], but with fewer steps.

> **Note:**
>
> A 100% down payment is not the same as a full payment of the sales order. A sales order paid
> through the regular invoice process will not allow any additional invoices to be generated and
> will not display the Create Invoice button on the Sales Order. Instead, following
> this example will cause the Create Invoice button to be displayed on the Sales Order.
> This is because the system expects another invoice to be created after the down payment to
> complete payment of the sales order.

The *Solar Panel Installation* product is being used in this example.

To configure a 100% down payment, navigate to Sales app ‣ New and add a
Customer to the quote. Next, click Add a product in the Order
Lines tab, and select the `Solar Panel Installation` product. Upon clicking the Confirm
button, the quotation turns into a sales order. At that point, an invoice can now be created by
clicking Create Invoice in the top-left corner. On the Create invoice(s)
pop-up window that appears, select Down payment (percentage), and type `100` in the
Down Payment field.

![The Down payment (percentage) option selected with 100% set as the Down Payment.](../../../../_images/100p-down-payment-percentage.png)

Next, click Create Draft Invoice to create an invoice draft. This will also bring the
draft invoice into view, which includes the Down payment under the Down
Payments section of the Invoice Lines tab. The invoice can now be confirmed and posted
by clicking Confirm. Confirming the invoice changes the status from Draft to
Posted. It also reveals a new series of buttons at the top of the page.

The payment can be registered by clicking the Pay button. This brings up the
Pay pop-up form, which is auto-populated with the necessary information. When ready,
click the Create Payment button.

After clicking Create Payment, Odoo reveals the customer invoice, now with a green
In Payment or Paid banner in the upper-right corner, depending on how the
database has configured and if manual confirmation of payments is required. The process is now
complete, and the 100% down payment has been successfully applied.

## Income account modification on down payments

> **Warning:**
>
> To change or adjust the income account attached to down payments, the **Accounting** app must be
> installed. With the **Accounting** app installed, the Accounting column becomes
> available on the draft invoice.

Navigate to the invoice to be modified by going to Sales app ‣ Orders ‣ Orders.
Open an order, then click the Invoices smart button. Open an invoice, click the
drop-down arrow on the entry in the Account column and click Search more…
to bring up the Search: Account form. In this form, a different account can be chosen
from the list of pre-existing accounts. A new account can also be created by clicking the
New button.

![The Search:Account form with existing accounts displayed and a button to create a new account.](../../../../_images/income-account.png)
> **Note:**
>
> [Invoicing policies](invoicing_policy.html)

---

# Pro-forma invoices

A *pro-forma invoice* is an abridged or estimated invoice sent in advance of a delivery of goods. It
notes the kind and quantity of goods, their value, and other important information, such as weight
and transportation charges.

Pro-forma invoices are commonly used as preliminary invoices with a quotation. They are also used
during importation for customs purposes. They differ from a normal invoice, in that they are *not* a
demand (or request) for payment.

## Configuration

In order to utilize pro-forma invoices, the *Pro-Forma Invoice* feature **must** be activated.

To enable this feature, navigate to Sales app ‣ Configuration ‣ Settings, and
in the Quotations & Orders section, click the checkbox next to Pro-Forma
Invoice. Then, click Save to save all changes.

![The Pro-Forma Invoice feature setting in the Odoo Sales application.](../../../../_images/pro-forma-setting.png)

## Send pro-forma invoice

With the Pro-Forma Invoice feature activated, the option to send a pro-forma invoice is
now available on any quotation or sales order, via the Send Pro-Forma Invoice button.

![The Send Pro-Forma Invoice button on a typical sales order in Odoo Sales.](../../../../_images/send-pro-forma-invoice-button.png)
> **Note:**
>
> Pro-forma invoices can **not** be sent for a sales order or quotation if an invoice for a down
> payment has already been sent, or for a recurring subscription.
>
> In either case, the Send Pro-Froma Invoice button does **not** appear.
>
> However, pro-forma invoices **can** be sent for services, event registrations, courses, and/or
> new subscriptions. Pro-forma invoices are not limited to physical, consumable, or storable goods.

When the Send Pro-Forma Invoice button is clicked, a pop-up window appears, from which
an email can be sent.

In the pop-up window, the Recipients field is auto-populated with the customer from the
sales order or quotation. The Subject field and the body of the email can be modified,
if necessary.

The pro-forma invoice is automatically added as an attachment to the email.

When ready, click Send, and Odoo instantly sends the email, with the attached pro-forma
invoice, to the customer.

![The email pop-up window that appears with pro-forma invoice attached in Odoo Sales.](../../../../_images/pro-forma-email-message-pop-up.png)
> **Note:**
>
> To preview what the pro-forma invoice looks like, click on the PDF at the bottom of the email
> pop-up window *before* clicking Send. When clicked, the pro-forma invoice is
> downloaded instantly. Open that PDF to view (and review) the pro-forma invoice.
>
> ![Sample pro-forma invoice PDF from Odoo Sales.](../../../../_images/pro-forma-pdf.png)

> **Note:**
>
> [Invoicing policies](invoicing_policy.html)

---

# Invoicing based on time and materials

Invoicing based on time and/or materials is typically used when accurately estimating the size of a
project isn’t possible, or when the requirements of a project may change.

This is different from a fixed-price contract, when a customer agrees to pay a specified total for
the fulfillment of the contract—no matter what needs to be paid to the employees, sub-contractors,
vendors, suppliers, and so on.

The Odoo *Sales* app can invoice for time and various other expenses (e.g. transport, lodging), as
well as purchases needed to fulfill an order.

## App and settings configuration

First, in order to accurately keep track of the progress of a project, the Odoo *Project* and
*Accounting* apps **must** be installed.

To install the *Project* app, navigate to Odoo main dashboard ‣ Apps. Then, on
the Apps page, locate the Project app block, and click Activate.
The page automatically refreshes and returns to the main Odoo dashboard, where the *Project* app is
now available to access.

Repeat the same process to install the *Accounting* application.

After installation, click the Accounting app icon from the main Odoo dashboard, and
navigate to Configuration ‣ Settings. On the Settings page, scroll
down to the Analytics section, and ensure the box next to Analytic
Accounting is checked.

![How it looks to activate the Analytic Accounting setting in Odoo Accounting Setting page.](../../../../_images/analytic-accounting-setting.png)

Then, click Save to save all changes.

Then, navigate to Odoo main dashboard ‣ Project app ‣ Configuration ‣
Settings. On the Settings page, in the Time Management section, ensure the
box beside the Timesheets feature is checked.

Then, click Save to save all changes.

![What the Timesheets feature looks like on the Odoo Project settings page.](../../../../_images/timesheets-feature.png)

## Service product configuration

With the *Timesheets* feature activated in the *Project* app, it is now possible to invoice for time
spent on a project, but **only** when the following product configurations have been made.

> **Warning:**
>
> Invoicing for time spent on a project is **only** possible with products that have *Service* set
> as the *Product Type* on their product form.

To configure a service product, first navigate to Sales app ‣ Products ‣
Products. On the Products page, select the desired service product to be configured, or
click New to create a new product.

From the product form, in the General Information tab, set the Product Type
to Service. Then, open the drop-down menu in the Invoicing Policy field, and
select Based on Timesheets.

Next, from the Create on Order drop-down menu, select Project & Task. That
setting indicates that, when a sales order is created with this specific service product, a new
project and task is created in the *Project* app.

![The correct settings for Invoicing Policy and Create on Order fields for service product.](../../../../_images/service-product-general-settings.png)
> **Note:**
>
> The option Task can be chosen instead from the Create on Order drop-down
> menu. If Task is chosen, select an existing project that the task will appear in from
> Project field, which only appears if Task is chosen in the
> Create on Order field.

## Add time spent to sales order

After properly configuring a service product with the correct *Invoicing Policy* and *Create on
Order* options, it is possible to add time spent to a sales order.

To see that in action, navigate to Sales app ‣ New to open a blank quotation
form. Then, proceed to add a Customer, and in the Order Lines tab, click
Add a product, and select the properly [configured service product] from the drop-down menu.

Next, click Confirm to confirm the order.

After confirming the sales order, two smart buttons appear at the top of the order form:
Projects and Tasks.

![How the Projects and Tasks smart buttons look on a Sales Order in Odoo Sales.](../../../../_images/projects-tasks-smart-buttons.png)

If the Projects smart button is clicked, it reveals the specific project related to this
sales order. If the Tasks smart button is clicked, it reveals the specific project task
related to this sales order. Both are also accessible in the *Project* app.

In order to add time spent on a sales order, click the Tasks smart button.

On the task form, select the Timesheets tab. From the Timesheets tab,
employees can be assigned to work on the project, and the time they spend working on the task can be
added by the employees or by the person who created the sales order.

To add an employee, and the time spent working on the task, click Add a line in the
Timesheets tab. Then, select the appropriate Date and Employee.
There is also the option to add a brief description of the work done during this time in the
Description column, but it’s not required.

Lastly, enter the amount of time worked on the task in the Hours Spent column, and click
away to complete that line in the Timesheets tab.

> **Note:**
>
> The time entered in the Hours Spent column is immediately reflected in the
> Allocated Time field (located near the top of the task form) as a percentage, which
> reflects how much of the total allocated work hours have been done so far.
>
> That same information is found as numerical hours in the Hours Spent and
> Remaining Hours fields, located at the bottom of the Timesheets tab.
>
> ![How the Timesheets tab appears on a task form in Odoo Sales and Odoo Project.](../../../../_images/timesheets-tab-on-task.png)

Repeat this process for however many employees and hours have been worked on the project.

## Invoice time spent

Once all the necessary employees and time spent have been added to the project task, return to the
sales order to invoice the customer for those hours. To do that, either click the Sales
Order smart button at the top of the task form, or return to the sales order via the breadcrumb
links, located in the upper-left of the screen.

Back on the sales order form, the time that was added to the task is reflected in the
Order Lines tab (in the Delivered column) and in the new Recorded
Hours smart button at the top of the sales order.

To invoice the customer for time spent on the project, click Create Invoice, and select
Regular invoice from the Create invoices pop-up window. Then, click
Create Draft Invoice.

Doing so reveals a Customer Invoice Draft, clearly showing all the work that’s been done
in the Invoice Lines tab.

> **Note:**
>
> Pay attention to the Analytic Distribution column in the Customer
> Invoice, as that information is necessary to ensure other time/material invoicing tasks are
> completed properly and accurately.
>
> ![Invoice draft showing time spent on sales order in Odoo Sales.](../../../../_images/invoice-lines-time.png)

Click Confirm to confirm the invoice and continue with the invoicing process.

> **Note:**
>
> [Invoicing policies](invoicing_policy.html)

## Expenses configuration

In order to track and invoice expenses related to a sales order, the Odoo *Expenses* app **must** be
installed.

To install the *Expenses* app, navigate to Odoo main dashboard ‣ Apps. Then, on
the Apps page, locate the Expenses app block, and click
Activate.

The page automatically refreshes and returns to the main Odoo dashboard, where the
Expenses app is now available to access.

## Add expenses to sales order

To add an expense to a sales order, first navigate to the Expenses app. Then, from
the main *Expenses* dashboard, click New, which reveals a blank expense form.

On the expense form, add a Description of the expense (e.g. `Hotel Stay`, `Plane
Ticket`). Next, in the Category field, select the appropriate option from the drop-down
menu (e.g. Meals, Miles, Travel & Accommodation).

> **Note:**
>
> Expense categories can be added and modified by navigating to Expenses app ‣
> Configuration ‣ Expense Categories.

Then, enter the total amount of the expense in the Total field, as well as any
Included Taxes that may apply. Next, ensure that the correct Employee is
selected, and designate who paid for the expense in the Paid By field: the
Employee (to reimburse) or the Company.

Next, in the Customer to Reinvoice field, select the appropriate sales order from the
drop-down menu. Then, select that same sales order information from the Analytic
Distribution field, as well.

> **Note:**
>
> The Analytic Distribution field will **only** have the corresponding sales order as
> an option if the sales order contains a service product that is billed based on *Timesheets*,
> *Milestones*, or *Delivered Quantities*.

![How to properly fill out an expense form that's attached to a sales order in Odoo.](../../../../_images/expense-detail-form.png)

If there are any receipts that should be uploaded and attached to the expense, click the
Attach Receipt button, and upload the necessary documents to the expense. This is
**not** required, but it may affect whether or not an expense is approved.

When all the information has been entered, click Create Report to create an expense
report detailing all the expense information that was just entered.

![How an Expense Report Summary looks in Odoo Expenses.](../../../../_images/expense-report-summary.png)

Then, there’s the option to Submit to Manager for approval. Once approved, the
Report in Next Payslip appears.

To showcase a complete flow in this example, select Submit to Manager. Then, the manager
would click Approve to approve this expense, and click Post Journal Entries
to post this expense to the accounting journal.

## Invoice expenses

To invoice a customer for an [expense on a sales order], navigate to the related sales order, either from the
Sales app or from the expense report in the Expenses app. From the
expense report, click the Sales Orders smart button at the top of the page.

If the expense report was linked to the sales order, the newly-configured expense now has its own
line in the Order Lines tab, and can be invoiced to the customer.

![An expense appearing on Order Lines tab of a Sales Order in Odoo Sales application.](../../../../_images/invoice-expense-from-sales-order.png)

To invoice the customer for the expense on the sales order, click Create Invoice, select
Regular Invoice from the Create invoices pop-up window, then click
Create Draft Invoice.

Doing so reveals a Customer Invoice Draft for the expense. Then, the invoicing process
can be completed as usual.

![Sample customer invoice for an expense generated from a sales order in Odoo Sales.](../../../../_images/customer-invoice-for-expense.png)

## Purchase configuration

In order to invoice a customer for purchases made on a sales order, the *Purchase* application
**must** be installed.

To install the *Purchase* application, navigate to Odoo main dashboard ‣ Apps.
Then, on the Apps page, locate the Purchase app block, and click
Activate. The page automatically refreshes and returns to the main Odoo dashboard, where
the Purchase app is now available to access.

## Add purchase to sales order

To add a purchase to a sales order, a purchase order must first be created. To create a purchase
order, navigate to Purchase app ‣ New to reveal a blank purchase order form.

First, add a Vendor to the purchase order. Then, under the Products tab,
click the extra column options drop-down menu, represented by two horizontal lines with
dots on them, located to the far-right of the column headers. From that drop-down menu, select
Analytic Distribution.

![How to add analytic distribution column on purchase order form in Odoo Purchase.](../../../../_images/extra-column-analytic-distribution-option.png)

After adding the Analytic Distribution column to the headers on the Products
tab of the purchase order form, proceed to add the product(s) to the purchase order. To do that,
click Add a product, and select the desired product from the drop-down menu. Repeat for
all the products to add.

> **Warning:**
>
> In order for a purchase to be properly invoiced on a sales order, the product on the purchase
> order **must** be marked as Can be Expensed, have an Invoicing Policy set
> to Delivered quantities, and have the At cost option selected in the
> Re-Invoice Expenses field on its product form.
>
> ![Product settings for a purchase order to be invoiced on a sales order in Odoo.](../../../../_images/product-form-settings-invoice-purchase.png)

Then, select the appropriate Analytic Distribution associated with the sales order to
which this purchase order is related. To do that, click the empty Analytic Distribution
field to reveal an Analytic pop-up window.

Then, from the Departments drop-down menu, select the analytic distribution associated
with the desired sales order to be invoiced for the purchase.

![How to select the Analytic Distribution department from a purchase order in Odoo.](../../../../_images/analytic-drop-down-distribution.png)

Once all the information is entered in the Products tab of the purchase order, confirm
the order by clicking Confirm Order. Then, click Receive Products when the
products have been received. This creates a receipt form.

> **Note:**
>
> If any serial/lot numbers must be entered before validating the receipt of products, then on the
> receipt form, click the details icon represented by four horizontal lines located to
> the far-right of the product line.
>
> This reveals a Detailed Operations tab, in which the necessary Lot/Serial
> Number(s) and Done quantity can be added. When ready, click Confirm to
> confirm the data.

Then, click Validate to validate the purchase order.

Next, return to the purchase order, via the breadcrumb links at the top of the page, and click
Create Bill to create a vendor bill that can be invoiced to the customer on the attached
sales order.

![Vendor bill draft for a purchase order to be invoiced to a customer in Odoo.](../../../../_images/vendor-bill-draft.png)
> **Note:**
>
> Make sure to enter a Bill Date on the Vendor Bill Draft before
> confirming. If a Bill Date is *not* entered, an error window appears, requesting that
> information to be entered before confirmation can occur.

Then, click Confirm to confirm the vendor bill, which is then automatically added to the
sales order, where it can be invoiced directly to the customer attached to it.

## Invoice purchase

To invoice a customer for a purchase on a sales order, first [add the purchase to the sales
order], then navigate to the desired sales order in
the Sales app.

On the sales order that was attached to the purchase order, the purchased product now has its own
product line under the Order Lines tab, and it is ready to be invoiced.

![Purchase order product on sales order to be invoiced to customer via Odoo Sales.](../../../../_images/purchase-order-on-sales-order.png)

To invoice the customer for the purchase, simply click Create Invoice, select
Regular Invoice from the Create invoices pop-up window, then click
Create Draft Invoice.

Doing so reveals a Customer Invoice Draft with the newly-added purchase order product in
the Invoice Lines tab.

![Customer invoice draft with purchase product attached to sales order in Odoo.](../../../../_images/draft-invoice-with-purchase-product.png)

To complete the invoicing process, click Confirm to confirm the invoice, and then click
Register Payment in the Register Payment pop-up form.

---

# Invoice project milestones

Milestone-based invoicing is designed for companies that deliver work in clearly defined phases.
Instead of invoicing an entire service upfront or at the very end, businesses can bill customers
progressively as each stage of work is completed. This approach provides customers clearer
visibility into progress and value delivered over time.

In Odoo, milestone invoicing is configured at the product level in the **Sales** app, with milestone
progress and completion managed in the **Projects** app. When a milestone is marked as reached, the
delivered quantity on the sales order (SO) is updated and can be invoiced.

## How milestone invoicing works

Milestone invoicing follows a clear workflow involving multiple applications in Odoo:

- A product is created in the **Sales** application, configured to be invoiced based on milestones.
- A SO is created with the product.
- A project in the **Projects** app is created with multiple milestones included.
- A milestone is reached, and marked complete, causing the *Delivered* quantity on the SO line to
  update.
- An invoice is created for the completed milestone, which can be sent to the customer.

> **Warning:**
>
> This document covers the **Sales** app configuration and invoicing flow for invoicing based on
> project milestones. For more information on creating, managing, and marking milestones as
> complete, and how to link them to tasks, see [Project milestones](../../../services/project/project_management/project_milestones.html).

## Create milestone products

To begin, a service product must be configured specifically for milestone-based invoicing. Navigate
to Sales app ‣ Products ‣ Products and click New. Enter the
necessary information, including the product title and Sales Price.

For the Product Type, select Service. Doing so reveals the Create
on Order field. Select either Project, Project and Task, or
Task, depending on how the product is to be tracked in the **Project** app.

> **Note:**
>
> A Project Template can also be selected for the product. See [Project templates](../../../services/project/project_management/project_templates.html) for more information. Project
> templates can have milestones defined, however, the *Quantity (%)* field must be manually updated
> on each newly created project.

For the Invoicing Policy, select Based on Milestones. This option ensures
that the product’s delivered quantities update automatically once a milestone is completed.

> **Warning:**
>
> *Based on Milestones* is only available if there is at least one project with *Milestones*
> enabled.

### Defining milestones

> **Note:**
>
> This document focuses on the process of selling and invoicing a milestone product in the
> **Sales** app. For more information on creating milestones in the **Project** app, see
> [Project milestones](../../../services/project/project_management/project_milestones.html).

After the milestone product has been sold, a *Milestones* smart button is added to the SO. Click
the smart button to view, edit, or create new milestones.

From here, the Delivered % can be altered. This amount equates to the total cost of the
SO that is billed when the milestone is reached.

> **Tip:**
>
> A company that provides pool installation services bills based on predefined milestones as the
> work is completed. Each milestone equates to 25% of the total services:
>
> > - Site Preparation & Excavation
> > - Structural Installation
> > - Plumbing & Equipment Installation
> > - Finishing & Final Inspection
>
> ![The milestones for a sales order line.](../../../../_images/view-milestones.png)
>
> The team uses a project template, called *Pool installation*, with these milestones defined. A
> new project is created whenever a SO with the *Pool installation services* product is
> confirmed.

## Invoicing a completed milestone

Milestones can be tracked through the **Project** app (see [Using milestones](../../../services/project/project_management/project_milestones.html#project-using-milestones)). Additionally, a milestone can be marked complete by navigating to the
SO, and clicking the Milestones smart button. On the *Milestones* page, enable the
checkbox in the Reached column for the milestone.

Then, click View Sales Order or use the breadcrumbs to return to the SO. The
Delivered column will be updated to reflect the *Delivered %* for the milestone reached.

These steps can be repeated as additional milestones are reached until the SO has been fulfilled.

> **Warning:**
>
> Reaching a milestone does *not* automatically create an invoice. Instead, it updates the SO to
> reflect the amount of the total that is ready for invoicing.

Once one or more milestones have been reached, navigate to the SO, and confirm the
Delivered column has updated correctly. Then, click Create Invoice.

Additional milestones can be invoiced as they are completed, until all services are complete.

> **Note:**
>
> - [Invoicing based on time and materials](time_materials.html)
> - [Pro-forma invoices](proforma.html)
> - [Invoicing policies](invoicing_policy.html)

---

# Products & Prices

---

# Manage your products

---

# Manage your pricing

---

# Returns and refunds

The Odoo *Sales* app provides two different ways to process returns. The method used depends on
whether or not an invoice has been sent.

## Before invoicing

Returns are completed using *Reverse Transfers* when a customer decides to return a product
**before** an invoice has been sent or validated.

> **Note:**
>
> In order to use *Reverse Transfers*, the *Inventory* app **must** be installed.

To start a return before invoicing, navigate to the Sales app, select the desired
sales order, and click on the Delivery smart button to open the associated delivery
order.

![A typical sales order with a highlighted delivery smart button in Odoo Sales.](../../../../_images/sales-order-delivery-smart-button.png)

On the validated delivery order, click Return.

![A validated delivery order with a highlighted Return button in Odoo Sales.](../../../../_images/validated-delivery-order-return-button.png)

This opens a Reverse Transfer pop-up window.

By default, the Quantity matches the validated quantities from the delivery order.
Update the quantities, if necessary. Click on the 🗑️ (trash) icon next to a line item
to remove it from the return.

![The "Reverse Transfer" pop-up window, to make a return before invoicing the customer.](../../../../_images/reverse-transfer-popup.png)

Next, click Return to confirm the return. This generates a new warehouse operation for
the incoming returned product(s).

![Warehouse operation after a return has been confirmed in Odoo Sales.](../../../../_images/warehouse-operation-confirmed-return.png)

Upon receiving the return, the warehouse team validates the warehouse operation by clicking
Validate. Then, on the original sales order, the Delivered quantity updates
to reflect the difference between the initial validated quantities and the returned quantities.

![The updated "Delivered" quantity on the sales order after the reverse transfer.](../../../../_images/updated-sales-quantities.png)

When an invoice is created, the customer receives an invoice **only** for the products they are
keeping, if any.

## After invoicing

Sometimes, customers return an item after they receive and/or pay for their invoice. In these
cases, a return using only *Reverse Transfers* is insufficient since validated, or sent, invoices
cannot be changed.

However, *Reverse Transfers* can be used in conjunction with *Credit Notes* to complete the
customer’s return.

To start a return after invoicing, navigate to the relevant sales order in the
Sales app.

If there is a payment registered on the sales order, the payment details appear in the chatter, and
the invoice (accessible through the Invoices smart button) has a green In
Payment banner.

![Sample of a green in payment banner in Odoo Sales.](../../../../_images/green-in-payment-banner.png)

From the sales order, click on the Delivery smart button to view the validated delivery
order. Then, click Return to open the Reverse Transfer pop-up window.

Next, edit the Product and/or Quantity, as needed for the return. Then,
click Return. This generates a new warehouse operation for the incoming returned
product(s), which is validated by the warehouse team once the return is received by clicking
Validate.

Then, on the sales order, the Delivered quantity updates to reflect the difference
between the initial validated quantities and the returned quantities.

To process a refund, navigate to the relevant invoice (from the sales order, click on the
Invoices smart button). Then, click the Credit Note button at the top of the
validated invoice.

![A typical customer invoice with a Credit Note button highlighted in Odoo Sales.](../../../../_images/credit-note-button.png)

Doing so reveals a Credit Note pop-up form.

![Typical credit note pop-up form that appears in Odoo Sales.](../../../../_images/credit-note-pop-up-form.png)

Start by entering a Reason displayed on Credit Note and a specific Journal
to process the credit. Then, select a specific Reversal Date.

After the information is filled in, click Reverse or Reverse and Create
Invoice. Then, edit the draft, if needed.

Lastly, click Confirm to confirm the credit note.

When complete, a blue banner reading: You have outstanding credits for this customer. You
can allocate them to mark this invoice as paid. appears at the top of the page.

> **Note:**
>
> [Credit notes and refunds](../../../finance/accounting/customer_invoices/credit_notes.html)

---

# Use eWallets and gift cards

With Odoo, customers can use **eWallets** and **gift cards** for online and in-store shopping.

To enable eWallets and gift cards for eCommerce and Point of Sale (PoS), first enable
Discounts, Loyalty & Gift Card under Sales app ‣ Configuration ‣
Settings ‣ Pricing section. Once enabled, go to Sales app ‣ Products ‣ Gift
cards & eWallet and Create a new eWallet or gift card program.

## eWallets

eWallets allow customers to save credits on their online account and use these credits as a payment
method when buying items in an online store or a brick-and-mortar store. eWallets can also be used
to centralize multiple [gift cards].

Before creating an eWallet program, it is necessary to create an eWallet **top-up** product. Top-ups
are pre-defined digital credit values added to an eWallet in exchange for its equivalent in real
currency. These credits can then be used as a payment method in the eCommerce shop or PoS. Top-up values can be of different amounts.

> **Tip:**
>
> A $50 top-up can be bought for $50, and adds that same amount of credits to the eWallet.

To create a top-up product, go to Sales app ‣ Products ‣ Products and
Create a new product. On the product template, configure the options as follows:

- Product Name: enter a name for the top-up product (for example, `$50 Top-Up`)
- Can be Sold: enabled
- Product Type: select Service
- Invoicing Policy: select Prepaid/Fixed Price
- Create on Order: select Nothing
- Sales Price: enter the amount of the top-up

> **Note:**
>
> In order to have eWallet top-ups of different amounts, create multiple top-up products and
> modify the Sales Price accordingly.

Once the top-up is created, go to Sales app ‣ Products ‣ Gift cards & eWallet
to Create an eWallet program. The following configuration options are available:

- Program Name: enter a name for the eWallet program
- Program Type: select eWallet
- eWallet Products: select the eWallet top-up created earlier. Repeat the process if
  you created top-ups of different amounts.
- Email template: select the email template used for the email sent to the customer. To
  create a new template, click on the field, select Search More, and then click
  Create.
- Currency: select the currency to use for the eWallet program
- Company: select the company for which the program is valid and available
- Available On: select the applications on which the program is valid and available
- Website: select the website on which the program is valid and available. Leave this
  field empty to include all websites.
- Point of Sale: select the PoS in which the program is valid
  and available. Leave this field empty to include all PoS.

![eWallet program configuration page](../../../../_images/ewallet-configuration.png)

Once the program is configured, click the Generate eWallet button in the upper-left
corner to generate eWallets. eWallets can be generated based on Customers and/or
Customer Tags. The quantity is automatically adapted according to the
Customers and Customer Tags selected. Then, set the eWallet
value. Finally, set the Valid Until period if applicable.

Generated eWallets can be accessed through the eWallets smart button in the upper-right
corner. From there, Send or Share the eWallets via email or a URL link.

![eWallets send and share buttons](../../../../_images/ewallet-share.png)

Click on an eWallet to change the Expiration Date, Partner, or
Balance. The Code of an eWallet *cannot* be changed, deleted, or duplicated.

## Gift cards

Gift cards can be purchased by customers, and in turn used as a payment method upon checkout at an
eCommerce shop or PoS.

Before creating a new gift card program, it is necessary to first create gift cards as products. To
do so, go to Sales app ‣ Products ‣ Products and Create a product.
On the product template, configure the options as follows:

- Product Name: enter a name for the gift card product
- Can be Sold: enabled
- Product Type: select Service
- Invoicing Policy: select Prepaid/Fixed Price
- Create on Order: select Nothing
- Sales Price: enter the amount of the gift card

> **Note:**
>
> In order to have gift cards of different amounts, create multiple gift card products and modify
> the Sales Price accordingly.

Once the gift card product is created, go to Sales app ‣ Products ‣ Gift cards
& eWallet to Create a gift card program. The following configuration options are
available:

- Program Name: enter a name for the gift card program
- Program Type: select Gift Card
- Gift Card Products: select the gift card product created earlier. Repeat the process
  if you created gift card products of different amounts.
- Email template: select the default Gift Card: Gift Card Information
  template, or create a new template by clicking on the field, selecting Search More,
  and then clicking Create.
- Print Report: select Gift Card
- Currency: select the currency to use for the gift card program
- Company: select the company for which the program is valid and available
- Available On: select the applications on which the program is valid and available
- Website: select the website on which the program is valid and available. Leave this
  field empty to include all websites.
- Point of Sale: select the PoS in which the program is valid
  and available. Leave this field empty to include all PoS.

![Gift card program configuration page](../../../../_images/giftcard-configuration.png)

Once the program is configured, click the Generate Gift Cards button in the upper-left
corner to generate gift cards. Gift cards can be generated either for Anonymous
Customers or Selected Customers. Set the Quantity to generate for
Anonymous Customers, or select the Customers and/or Customer
Tags for Selected Customers. Then, set the Gift Card value. Finally, set
the Valid Until period if applicable.

Generated gift cards can be accessed through the Gift Cards smart button in the
upper-right corner. From there, Send or Share the gift cards via email or a
URL link.

![Gift cards send and share buttons](../../../../_images/giftcard-share.png)

Click on a gift card to change the Expiration Date, Partner, or
Balance. The Code of a gift card *cannot* be changed, deleted, or
duplicated.

---

# Discount and loyalty programs

The Odoo **Sales**, **eCommerce**, and **Point of Sale** applications allow users to create discount
and loyalty programs that customers can use for online and in-store shopping. These programs offer
more varied, public, and time-sensitive pricing options than [pricelists](prices/pricing.html).

## Configure the settings

To begin using discount and loyalty programs, navigate to Sales ‣ Configuration
‣ Settings. Under the Pricing heading, activate the Discounts, Loyalty &
Gift Card setting by checking the box next to the feature. Finally, click Save to save
the changes.

## Configure discount and loyalty programs

To create discount and loyalty programs, go to Sales ‣ Products ‣ Discount &
Loyalty.

If no discount or loyalty programs have been created yet, Odoo provides a choice of templates to
help create the first program. Choose one of the template cards, or click New to create
a new program from scratch.

Or, if there are already existing programs, select an existing program to edit it.

![Discount and loyalty program template cards.](../../../../_images/price-discount-loyalty.png)
> **Note:**
>
> Templates **only** appear when no programs have been created, and they disappear once the first
> program is created.

Creating or editing a program opens the program form.

![Program options on the loyalty program form.](../../../../_images/price-programs.png)

The program form contains the following fields:

- Program Name: Enter the name of the program in this field. The program name is **not**
  visible to the customer.
- Program Type: Select the desired [program type] from the drop-down menu.
- Currency: Select the currency used for the program.
- Pricelist: If desired, select a pricelist from the drop-down menu to have this loyalty
  program applied to a specific pricelist (and customers attached to the pricelist). More than one
  pricelist can be selected in this field. When a single loyalty program is linked to several
  pricelists, it makes it viable for different customer segments to have different pricelists, but
  the *same* loyalty programs. If this field is left blank, the program applies to everyone,
  regardless of pricelist.
- Points Unit: Enter the name of the points used for the Loyalty Cards
  program (e.g. `Loyalty Points`). The points unit name *is* visible to the customer. This field is
  **only** available when the Program Type is set to Loyalty Cards.
- Start Date: Select the date on which the program becomes valid. Leave this field blank
  if the program should always be valid and not expire.
- End Date: Select the date on which the program stops being valid. Leave this field
  blank if the program should always be valid and not expire.
- Limit Usage: If desired, tick this checkbox, and enter a number of usages
  to limit the number of times the program can be used during the validity period.
- Company: If working in a multi-company database, choose the one company for which the
  program is available. If left blank, the program is available to all companies in the database.
- Available On: Select the apps on which the program is available.
- Website: Select a website on which the program is available. Leave this field blank to
  make it available on all websites.
- Point of Sale: Select the point(s) of sale at which the program is available. Leave
  this field blank to make it available at all PoS.

> **Note:**
>
> The options available on the program form vary depending on the [Program Type] selected.

All of the existing cards, codes, coupons, etc. that have been generated for the program are
accessible through the smart button located at the top of the form.

![Program items smart button on the loyalty program form.](../../../../_images/price-programs-items.png)
> **Note:**
>
> In Odoo 17 (and later), when a loyalty card or coupon is associated with a contact in the
> database, a Loyalty Cards smart button conditionally appears on the contact form.
>
> ![The Loyalty Card smart button as it appears on a contact form in Odoo 17.](../../../../_images/loyalty-cards-smart-button.png)
>
> This smart button **only** appears if a loyalty card or coupon is associated with the contact.

### Program types

The different Program Types available on the program form are:

- Coupons: Generate and share single-use coupon codes that grant immediate access to
  rewards.
- Loyalty Cards: When making purchases, the customer accumulates points to exchange for
  rewards on current and/or future orders.
- Promotions: Set conditional rules for ordering products, which, when fulfilled, grant
  access to rewards for the customer.
- Discount Code: Set codes which, when entered upon checkout, grant discounts to the
  customer.
- Buy X Get Y: for every (X) item bought, the customer is granted 1 credit. After
  accumulating a specified amount of credits, the customer can trade them in to receive (Y) item.
- Next Order Coupons: Generate and share single-use coupon codes that grant access to
  rewards on the customer’s next order.

### Conditional rules

Next, configure the Conditional rules that determine when the program applies to a
customer’s order.

In the Rules & Rewards tab, click Add next to Conditional rules
to add *conditions* to the program. This reveals a Create Conditional rules pop-up
window.

![Rules & Rewards tab of the loyalty program form.](../../../../_images/price-conditional-rewards.png)
> **Note:**
>
> The options for Conditional rules vary depending on the selected [Program Type].

The following options are available for configuring conditional rules:

- Discount Code: Enter a custom code to be used for the Discount Code
  program, or use the default one generated by Odoo. This field is only available when the
  Program Type is set to Discount Code.
- Minimum Quantity: Enter the minimum number of products that must be purchased in order
  to access the reward. Set the minimum quantity to at least `1` to ensure that the customer must
  make a purchase in order to access the reward.
- Minimum Purchase: Enter the minimum amount (in currency), with tax
  Included or tax Excluded, that must be spent in order to access the reward. If both a
  minimum quantity *and* minimum purchase amount are entered, then the customer’s order must meet
  both conditions.
- Products: Select the specific product(s) for which the program applies. Leave this
  field blank to apply it to all products.
- Categories: Select the category of products for which the program applies. Choose
  All to apply it to all product categories.
- Product Tag: Select a tag to apply the program to products with that specific tag.
- Grant: Enter the number of points the customer earns per order,
  per currency spent, or per unit paid (for the Loyalty Cards
  and Buy X Get Y programs).

![Conditional rules configuration window for a discount or loyalty program.](../../../../_images/price-conditions.png)

Click Save & Close to save the rule and close the pop-up window, or click
Save & New to save the rule and immediately create a new one.

### Rewards

In the Rules & Rewards tab of the program form, click Add next to
Rewards to add *rewards* to the program. This reveals a Create Rewards
pop-up window.

> **Note:**
>
> The options for Rewards vary depending on the selected [Program Type].

The following options are available for configuring rewards:

- Reward Type: Select the reward type among Free Product,
  Discount, and Free Shipping. The other options for reward configuration
  depend on the Reward Type selected.

  - Free Product:

    - Quantity Rewarded: Select the number of free products rewarded to the customer.
    - Product: Select the product given for free as a reward. Only one product can be
      selected.
    - Product Tag: Select a tag to further specify the free product eligible for the
      reward.
  - Discount:

    - Discount: Enter the discounted amount in either percentage,
      currency per point, or currency per order. Then, select whether the
      discount applies to the entire Order, only the Cheapest Product on the
      order, or only Specific Products. If [developer mode](../../../general/developer_mode.html) is active, the reward can be set to apply to the
      Cheapest Product in a specific domain (for example, the cheapest t-shirt when
      there are multiple types of clothing in a sales order).
    - Max Discount: Enter the maximum amount (in currency) that this reward may grant as
      a discount. Leave this field at `0` for no limit.
  - Free Shipping:

    - Max Discount: Enter the maximum amount (in currency) that this reward may grant as
      a discount. Leave this field at `0` for no limit.
- In exchange of: Enter the number of points required to exchange for the reward (for
  the Loyalty Cards and Buy X Get Y programs).
- Description on order: Enter the description of the reward, which is displayed to the
  customer upon checkout.

![Rewards configuration window for a discount or loyalty program.](../../../../_images/price-rewards.png)

---

# Commissions

Commissions are a powerful tool to motivate sales team members. They incentivize performance, boost
productivity, and encourage healthy competition. The *Commissions* feature in Odoo’s **Sales**
application provides a way to reward salespeople or sales teams based on their performance. This
feature supports the creation of flexible, measurable commission structures that align with business
goals, whether that means driving revenue, volume, profit, or recurring contracts.

## Configuration

To enable the *Commissions* feature, navigate to Sales app ‣ Configuration ‣
Settings. Scroll to the Invoicing section, and tick the Commissions
checkbox. Then, click Save. Doing so causes a new Commissions menu to appear
in the menu bar. To create a new commission plan, navigate to Commissions ‣
Comission Plans and click New.

## Commission plan structure

Each commission plan is comprised of several components:

- Based on: Determines whether commissions are awarded based on progress toward
  Targets or Achievements
- per: Indicates whether the plan applies to individual salespeople or an entire sales
  team
- Target Frequency: Sets how often targets reset: **Monthly**, **Quarterly**, or
  **Yearly**.
- Achievements: Determines what is being measured toward commissions.

![A new commission plan detail form.](../../../_images/new-commission-plan.png)

### Target-based commission plans

In a *Target* based commission plan, commissions are awarded based on the percentage of sales
targets reached. Target based plans are ideal for setting clear, measurable goals, such as invoicing
a specific amount in sales per quarter, then rewarding sales people progressively based on how close
they come to reaching or exceeding that goal.

> **Note:**
>
> Target based plans differ from *Achievement* based plans because they are based on reaching a
> fixed, predefined goal. They focus on goal-based incentives and performance milestones.

To configure a new target based commission plan, navigate to the Sales app ‣
Commissions ‣ Commission Plans, then click New. Click in the Based on
drop-down menu and select Targets. Then, select an option in the per field.

In the On Target Commission field, set the payout amount for reaching `100%` of the
target. Update the Effective Period fields to confirm the dates for this plan. Then,
update the Target Frequency field based on how often the targets should be set and
evaluated.

- *Monthly*: short term goals with frequent payouts.
- *Quarterly*: aligns with business cycles and provides mid-range objectives.
- *Yearly*: long term sales goals for strategic planning.

After the Target Frequency field is updated, the Targets tab updates with a
list of the appropriate time frame. For each Period, enter a Target goal.

On the Achievements tab, add one or more [Achievement metric] for this plan by clicking Add a new achievement.

Click the Sales People tab to assign this plan to the appropriate staff. Click either
Add a new Sales Person to add them individually, or Add Multiple
Salespersons to bulk add several at once.

> **Note:**
>
> The Add Multiple Salespersons button is only available if
> [Developer mode (debug mode)](../../general/developer_mode.html) is active.

### Levels

To provide additional incentive, *commission levels* can be added to *Target* based plans. These
tiers allow salespeople to earn varying commission amounts based on their performance levels. Levels
can start at `0%` and increase incrementally. This allows for salespeople to earn commission even if
they do not achieve `100%` of the target, as well as the ability to achieve over `100%` of the
target. Commission levels can be set from the Commissions tab when creating a commission
plan.

If no levels are added above 100%, salespeople are **not** able to earn above the stated commission.

> **Tip:**
>
> In the plan below, the levels start at `0%`, and continue until `300%`. If a salesperson exceeds
> `100%` of the expected target, their expected payout continues to increase up to `300%`.
>
> ![An example of commission levels, with levels above 100 percent.](../../../_images/commission-levels.png)

### Achievement-based commission plans

In a *Achievement* based commission plan, salespeople earn a percentage of their invoice value as
commission. Achievement-based plans are ideal for rewarding sales activity consistently, regardless
of specific goals. For example, offering a `5%` commission on all invoiced amounts, regardless of
how much is sold.

> **Note:**
>
> Achievement based plans differ from *Target* based plans because they are calculated based on
> actual achievements using a flat, consistent rate. They are beneficial for ongoing, non-goal
> based compensation plans.

To configure a new target based commission plan, navigate to the Sales app ‣
Commissions ‣ Commission Plans, then click New. Click in the Based on
drop-down and select Achievements. Then, select an option in the per field.

Update the Effective Period fields to confirm the dates for this plan. Then, update the
Target Frequency field based on how often the targets should be set and evaluated.

On the Achievements tab, add one or more [Achievement metric] for this plan by clicking Add a new achievement.

Click the Sales People tab to assign this plan to the appropriate staff. Click either
Add a new Sales Person to add them individually, or Add Multiple
Salespersons to bulk add several at once.

### Achievements

Performance can be measured in several ways in performance plans. These are configured in the
Achievements tab of each plan. It is possible to track achievements by all products
sold, by specific products sold, by all products sold in a specific category, and more.

- Amount Sold: the total value of sales orders (SOs).
- Amount Invoiced: the total value of confirmed invoices.
- Quantity Sold: the total number of units sold via SOs.
- Quantity Invoiced: the total number of units invoiced.
- Margin: the profit margin (selling price minus cost price).
- MRR: the new *Monthly Recurring Revenue* from subscription sales. this option is
  **only** available if the [Subscriptions](../subscriptions.html) app is installed.

> **Note:**
>
> Regardless of what the plan is Based on, each plan needs both *Achievements* and
> *Targets* configured.

## Plan approval

After confirming the details of the new plan, click Approve. This moves the plan from
the Draft stage into the Approved stage.

> **Warning:**
>
> Commissions plans in the Approved stage **cannot** be edited. To edit an approved
> plan, it must first be Reset to Draft.

After a plan is approved, Odoo automatically tracks performance and calculates commissions based on
the established parameters.

> **Note:**
>
> [Commissions](../../hr/payroll/commissions.html)

---

# Amazon Connector

---

# Amazon Connector features

The *Amazon Connector* synchronizes orders between Amazon and Odoo, which considerably reduces the
amount of time spent manually entering Amazon orders (from the Amazon Seller account) into Odoo. It
also allows users to accurately keep track of Amazon sales in Odoo.

## Supported features

The Amazon Connector is able to:

- Synchronize (Amazon to Odoo) all confirmed orders (both FBA and FBM), and their order items, which
  include:

  - product name, description, and quantity
  - shipping costs for the product
  - gift wrapping charges
- Create any missing partner related to an order in Odoo (contact types supported: contact and
  delivery address).
- Notify Amazon of confirmed shipment in Odoo (FBM) to get paid.
- Synchronize (Odoo to Amazon) all available quantities of your products (FBM).
- Support multiple seller accounts.
- Support multiple marketplaces per seller account.

The following table lists capabilities provided by Odoo when using the Amazon Connector:

|  | Fulfilled By Amazon (FBA) | Fulfilled By Merchant (FBM) |
| --- | --- | --- |
| **Orders** | Synchronize shipped and cancelled orders. | Synchronize unshipped and cancelled orders. |
| **Shipping** | Shipping cost is computed by Amazon, and included in the synchronized order. | Shipping cost is computed by Amazon and included in the synchronized orders. |
| Shipping done by Amazon. | A delivery order is automatically created in Odoo for each new order. Once it has been processed in Odoo, the status is then synchronized in Amazon. |
| **Gift Wrapping** | Handled by Amazon. | Cost is computed by Amazon, and included in the synchronized order. Gift message is added on a line of the order and on the delivery order. Then it is up to the user. |
| **Stock Management** | Managed by Amazon, and synchronized with a virtual location to follow it in Odoo. | Managed in Odoo Inventory app, and synchronized with Amazon. |
| **Delivery Notifications** | Handled by Amazon. | Send by Amazon, based on delivery status synchronized from Odoo. |

> **Note:**
>
> The Amazon Connector is designed to synchronize the data of sales orders. Other actions, such as
> downloading monthly fees reports, handling disputes, or issuing refunds, **must** be managed from
> the *Amazon Seller Central*, as usual.

> **Warning:**
>
> As of February 19, 2024, in North American marketplaces, FBA orders
> created with the *Amazon Connector*, do not get the customer’s name passed onto the
> sales/delivery order in Odoo. This is due to the fact that Amazon now calculates, and remits,
> sales tax on behalf of sellers. In other words, personally identifiable customer information is
> not transmitted to the seller any longer, after a FBA order.

## Supported marketplaces

If a marketplace is not listed in your Amazon marketplaces, it’s possible to [add a new
marketplace](setup.html#amazon-add-new-marketplace).

| **North America region** | |
| --- | --- |
| Canada | Amazon.ca |
| Mexico | Amazon.com.mx |
| US | Amazon.com |

| **Europe region** | |
| --- | --- |
| Germany | Amazon.de |
| Spain | Amazon.es |
| France | Amazon.fr |
| UK | Amazon.co.uk |
| Italy | Amazon.it |
| Netherlands | Amazon.nl |

> **Note:**
>
> - [Amazon Connector configuration](setup.html)
> - [Amazon order management](manage.html)

---

# Amazon Connector configuration

Odoo allows users to register an Amazon seller account in the database, but the user **must** have
a paid Amazon Seller account prior to completing the configuration.

Set up a paid Seller account on Amazon by first logging into the Amazon platform, and navigating to
Account & Lists ‣ Start a Selling Account from the drop-down menu located in
the header section.

Then on the Sell with Amazon page, follow the sign-up process and finally proceed to
follow the instructions below to register and link that Amazon Seller account in Odoo.

> **Note:**
>
> [Sell with Amazon](https://www.amazon.com/b/?node=12766669011)

## Connect Amazon Seller account to Odoo

To connect an Amazon Seller account in Odoo, navigate to Sales app ‣
Configuration ‣ Settings ‣ Connectors section, activate the Amazon Sync feature,
and click Save.

Then, return to Sales app ‣ Configuration ‣ Settings ‣ Connectors section,
and click on the Amazon Accounts link under the Amazon Sync setting.

![The Amazon Accounts link beneath the Amazon Sync settings in Odoo Sales.](../../../../_images/amazon-accounts-link-setting.png)

Doing so reveals a separate Amazon Accounts page. From here, click New to
create and link a new Amazon account.

On the blank Amazon Account form page, start by choosing a name for the account (e.g.
`American Marketplace`). Then, in the Credentials tab, select the marketplace on which
the seller account was initially created from the Home Marketplace drop-down menu.

![A typical Amazon Account form page in the Odoo Sales application.](../../../../_images/amazon-accounts-form-page.png)

After saving, the field in the Credentials tab is replaced by a Link with
Amazon button.

![A typical Amazon Account form page and Link with Amazon button in Odoo Sales.](../../../../_images/amazon-accounts-form-link-button.png)

Clicking that button redirects to either the Amazon login page, or directly to the required consent
page, if the user is already logged in to Amazon.

On the login page, log in to the desired Amazon seller account.

On the consent page, confirm that Amazon is allowed to give Odoo access to the account and related
data.

Upon confirmation, Amazon returns the user to Odoo, and the account has been registered.

With the Amazon account successfully registered, the marketplaces available to this specific account
are synchronized with Odoo and listed under the Marketplaces tab.

If desired, remove items from the list of synchronized marketplaces to disable synchronization.

## Amazon orders in Odoo

When an Amazon order is synchronized, up to three line items are created on the sales order in Odoo.
Each one represents a product sold on Amazon: one for the product that was sold on Amazon
Marketplace, one for the shipping charges (if any), and one for the gift wrapping charges (if any).

The selection of a database product for a sales order item is done by matching its
Internal Reference (a customizable product reference idenifier in Odoo, like `FURN001`)
with the Amazon *SKU* for marketplace items, the Amazon *Shipping Code* for delivery charges, and
the Amazon *Gift Wrapping* code for gift wrapping charges.

For marketplace products, pairings are saved as *Amazon Offers*, which are listed under the
Offers smart button on the account form.

![The Amazon Offers smart button on the account form in Odoo Sales.](../../../../_images/amazon-offers-button.png)

Offers are automatically created when the pairing is established, and they’re used for subsequent
orders to lookup SKUs. If no offer with a matching SKU is found, [the internal reference is
used instead].

> **Note:**
>
> It’s possible to force the pairing of a marketplace item with a specific product, by changing
> either the product or the SKU of an offer to ensure they match. The offer can be manually created
> if it was not automatically done yet.
>
> This is useful if the internal reference is not used as the SKU, or if the product sells under
> different conditions.

If no database product with a matching internal reference is found for a given Amazon SKU or gift
wrapping code, then a default database product, *Amazon Sale*, is used. The same is done with the
default product *Amazon Shipping* if no database product is found for a given Amazon shipping code.

> **Note:**
>
> To modify default products, activate the [developer mode](../../../general/developer_mode.html#developer-mode), and navigate to
> Sales app ‣ Configuration ‣ Settings ‣ Connectors ‣ Amazon Sync ‣
> Default Products.

## Product tax configuration

To allow for tax reporting of Amazon sales with Odoo, the taxes applied to the sales order items are
those set on the product, or determined by the fiscal position.

Make sure to have the correct taxes set on your products in Odoo, or have it done by a fiscal
position, to avoid discrepancies in the subtotals between *Amazon Seller Central* and Odoo.

> **Note:**
>
> As Amazon does not necessarily apply the same taxes as those configured in Odoo, it may happen
> that order totals differ by a few cents between Odoo and *Amazon Seller Central*. Those
> differences can be resolved with a write-off when reconciling the payments in Odoo.

## Add a new marketplace

All marketplaces are supported by the Amazon Connector. To add a new marketplace, proceed as
follows:

1. Activate the [developer mode](../../../general/developer_mode.html#developer-mode).
2. Go to Sales app ‣ Configuration ‣ Settings ‣ Connectors ‣ Amazon Sync ‣
   Amazon Marketplaces.
3. Click New to create a new marketplace record.
4. Enter the Marketplace ID in the API Idenifier field, and select the Amazon
   Region for your marketplace as described in the [Amazon Documentation for marketplace IDs and
   regions](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids), and the
   Seller Central URL as described in the [Amazon Documentation for seller central URLs](https://developer-docs.amazon.com/sp-api/docs/seller-central-urls).
5. Set the Name of the record to `Amazon.<country code>` to easily retrieve it (e.g.
   `Amazon.se`). The API Identifier, the Region and the Seller
   Central URL fields should respectively hold the *Marketplace ID*, the selected Amazon region,
   and the *Seller Central URL* values from the Amazon Documentation.
6. Once the marketplace is saved, update the Amazon Account configuration by going to
   Sales app ‣ Configuration ‣ Settings ‣ Connectors ‣ Amazon Sync ‣
   Amazon Accounts.
7. Select the account on which to use the new marketplace, go to the Marketplaces tab,
   and click on Update available marketplaces. An animation should confirm the success
   of the operation. Newly added marketplaces are automatically added to the list of synchronized
   marketplaces. If the new marketplace is not added to the list, it means that it is either
   incompatible or unavailable for the seller account.

> **Note:**
>
> - [Amazon Connector features](features.html)
> - [Amazon order management](manage.html)

---

# Amazon order management

## Order synchronization

Orders are automatically fetched from Amazon, and synchronized in Odoo, at regular intervals.

The synchronization is based on the Amazon status: only orders whose status has changed since the
last synchronization are fetched from Amazon. This includes changes on either end (Amazon or Odoo).

For *FBA* (Fulfilled by Amazon), only *Shipped* and *Cancelled* orders are fetched.

For *FBM* (Fulfilled by Merchant), the same is done for *Unshipped* and *Cancelled* orders. For each
synchronized order, a sales order and customer are created in Odoo (if the customer is not already
registered in the database).

> **Note:**
>
> When an order is cancelled in Amazon, and was already synchronized in Odoo, the corresponding
> sales order is automatically cancelled in Odoo.

## Force synchronization

In order to force the synchronization of an order, whose status has **not** changed since the
previous synchronization, start by activating the [developer mode](../../../general/developer_mode.html#developer-mode). This
includes changes on either end (Amazon or Odoo).

Then, navigate to the Amazon account in Odoo (Sales app ‣ Configuration ‣
Settings ‣ Connectors ‣ Amazon Sync ‣ Amazon Accounts), and modify the date under
Orders Follow-up ‣ Last Order Sync.

Be sure to pick a date that occurs prior to the last status change of the desired order to
synchronize and save. This will ensure synchronization occurs correctly.

> **Note:**
>
> To immediately synchronize the orders of an Amazon account, switch to [developer mode](../../../general/developer_mode.html#developer-mode), head to the Amazon account in Odoo, and click Sync Orders. The
> same can be done with pickings by clicking Sync Pickings.

## Manage deliveries in FBM

Whenever an FBM (Fulfilled by Merchant) order is synchronized in Odoo, a picking is instantly
created in the *Inventory* app, along with a sales order and customer record. Then, decide to either
ship all the ordered products to the customer at once, or ship products partially using backorders.

When a picking related to the order is confirmed, a notification is then sent to Amazon, who, in
turn, notifies the customer that the order (or a part of it) is on its way.

> **Warning:**
>
> Amazon requires users to provide a tracking reference with each delivery. This is needed to
> assign a carrier.
>
> If the carrier doesn’t automatically provide a tracking reference, one must be set manually. This
> rule applies to all Amazon marketplaces.

> **Note:**
>
> If the chosen carrier isn’t supported by Odoo, a carrier with the same name can still be created
> (e.g. create a carrier named `easyship`). The name used is **not** case sensitive, but be mindful
> to avoid typos. If there are typos, Amazon will **not** recognize them. Next, create a delivery
> carrier named `Self Delivery` to inform Amazon that the user will make the deliveries. Even with
> this route, a tracking reference still **must** be entered. Remember, the customer is notified by
> email about the delivery, and the carrier, along with the tracking reference, are displayed in
> the email to the customer.

> **Note:**
>
> [Third-party shipping carriers](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.html)

### Manage errors when synchronizing deliveries

Sometimes, Amazon can fail to correctly process all the information sent by Odoo. In this case, Odoo
sends an email listing all the shipments that failed and the errors Amazon sent with them. In
addition, these shipments are flagged with a Synchronization with Amazon failed tag.

Usually, the error can be corrected directly in the Amazon backend or in Odoo. If the problem is
corrected in Odoo, synchronize the shipment again using the Retry Amazon Sync button.

> **Note:**
>
> It might happen that Odoo receives a notification from Amazon saying that some delivery
> information was not processed, but without specifying which shipments were affected. In that
> case, all the shipments in an unknown state will be treated as if they failed to synchronize.
> Once Odoo receives a notification from Amazon saying that a shipment was processed, its tag will
> change to Synchronized with Amazon. To speed up this process, on your Amazon account,
> click on Sync Orders to manually synchronize these orders, or click on
> Recover Order and enter the relevant Amazon Order Reference.

## Follow deliveries in FBA

When an FBA (Fulfilled by Amazon) order is synchronized in Odoo, a stock move is recorded in the
*Inventory* app for each sales order item. That way, it’s saved in the system.

Inventory managers can access these stock moves by navigating to Inventory app ‣
Reporting ‣ Moves History.

For FBA orders, the stock move is automatically created in Odoo by the Amazon connector, thanks to
the shipping status of Amazon. When sending new products to Amazon, the user should manually create
a picking (delivery order) to transfer these products from their warehouse to the Amazon location.

> **Note:**
>
> To follow *Amazon (FBA)* stock in Odoo, make an inventory adjustment after replenishing stock. An
> automated replenishment from reordering rules can also be triggered on the Amazon location.

The Amazon location is configurable by accessing the Amazon account managed in Odoo. To access
Amazon accounts in Odoo navigate to Sales app ‣ Configuration ‣ Settings ‣
Connectors ‣ Amazon Sync ‣ Amazon Accounts.

All accounts of the same company use the same Amazon location, by default. However, it is possible
to follow the stock filtered by marketplace.

To do that, first remove the marketplace, where the desired stock to follow separately can be found,
from the list of synchronized marketplaces, which can be found by navigating to
Sales app ‣ Configuration ‣ Settings ‣ Connectors ‣ Amazon Sync ‣ Amazon
Accounts.

Next, create another registration for this account, and remove all marketplaces— **except** the
marketplace this is desired to be isolated from the others.

Lastly, assign another stock location to the second registration of the account.

## Invoice and register payments

### Issue invoices

Due to Amazon’s policy of not sharing customer email addresses, it is **not** possible to send
invoices directly to Amazon customers from Odoo. However, it **is** possible to manually upload the
generated invoices from Odoo to the Amazon back-end.

Additionally, for B2B clients, it is currently required to manually retrieve VAT numbers from the
Amazon back-end **before** creating an invoice in Odoo.

### Register payments

Since customers pay Amazon as an intermediary, creating a dedicated *Bank* journal (e.g. named
`Amazon Payments`), with a dedicated *Bank and Cash* intermediary account is recommended.

Additionally, as Amazon makes a single monthly payment, selecting all the invoices linked to a
single payment is necessary when registering payments.

To do that, use the appropriate Journal dedicated to Amazon payments, and select
Batch Deposit as the Payment Method.

Then, select all the generated payments, and click Actions ‣ Create batch payment
‣ Validate.

> **Note:**
>
> This same action can be performed with vendor bills from Amazon dedicated to commissions.
>
> When the balance is received in the bank account at the end of the month, and the bank statements
> are recorded, credit the Amazon intermediary account by the amount received.

## Follow Amazon sales in sales reporting

On the Amazon account profile in Odoo, a sales team is set under the Order Follow-up
tab.

This gives quick access to important metrics related to sales reporting. By default, the Amazon
account’s sales team is shared between all of the company’s accounts.

If desired, the sales team on the account can be changed for another, in order to perform a separate
reporting for the sales of this account.

> **Note:**
>
> It is also possible to perform reporting on a per-marketplace basis.
>
> First, remove the desired marketplace from the list of synchronized marketplaces.
>
> To access the list of synchronized marketplaces in Odoo, navigate to Sales app
> ‣ Configuration ‣ Settings ‣ Connectors ‣ Amazon Sync ‣ Amazon Accounts.
>
> Then, create another registration for this account, and remove all other marketplaces **except**
> the one to isolate.
>
> Lastly, assign another sales team to one of the two registrations of the account.

> **Note:**
>
> - [Amazon Connector features](features.html)
> - [Amazon Connector configuration](setup.html)

---

# Tracking lot or serial number products with FBA orders

When selling products tracked by lots or unique serial numbers via the Fulfilled By Amazon
FBA feature, Amazon’s API does not send the specific lot or unique
serial number used for the sale. The lack of information triggers a synchronization failure in Odoo.

To successfully set up an Amazon FBA order, configure a [product
kit] in Odoo based on the original Amazon product. When a new
FBA order syncs, Odoo sells the product kit, which prevents the error that occurs with the tracked
product.

When [resupplying the Amazon Fulfillment center](manage.html#amazon-connector-fba-follow-deliveries),
transfer the tracked product to the `WH/Amazon` location. This records the movement in traceability
reports and accounts for inventory consumption at the point of transfer rather than the point of
sale.

> **Note:**
>
> The `WH/Amazon` location is automatically created as a default location when the first Amazon
> account is linked.

Under this system, the quantity of the product kits remains negative indefinitely. Treat this as a
standard byproduct of the bypass, as the actual stock levels are managed through the initial
fulfillment center transfer.

> **Warning:**
>
> This setup does not track the specific lot or unique serial number used for the sale. It only
> ensures that the FBA order can be processed without synchronization failures.

## Settings

The following apps are essential for the product kit workflow:

- **Sales app**: Enables [connecting an Amazon Seller account to Odoo](setup.html#amazon-setup).
- **Inventory app**: Allows for product replenishment by [warehouse location](../../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations.html#use-locations-configuration).
- **Manufacturing app**: Enables [BoM creation](../../../inventory_and_mrp/manufacturing/basic_setup/bill_configuration.html#manufacturing-basic-setup-bom-setup) for
  products and product kits.

## Create a product kit

To enable accurate tracking, create a product kit for the existing Amazon product. When a new FBA
order syncs, Odoo sells the kit, which prevents the error that occurs with the tracked product.

Navigate to Sales app ‣ Products ‣ Products and click New. Then,
[create a kit as a product](../../../inventory_and_mrp/manufacturing/advanced_configuration/kit_shipping.html#manufacturing-advanced-configuration-kits) that represents the
Amazon item.

> **Warning:**
>
> *Never* enable Track Inventory for the product kit.

![Example of a product form configured to be a kit in the Inventory app.](../../../../_images/product-kit-form.png)

### Link the Amazon item SKU to the product kit

Next, go to the Sales app ‣ Configuration ‣ Offers and click New.
Enter the desired [Amazon market](features.html#amazon-supported-marketplaces) in the
Marketplace column, and select the product kit in the Product column. In the
Amazon SKU column, enter the SKU of the existing Amazon product.

> **Note:**
>
> This method removes the link between the Amazon SKU and the tracked product. Breaking this
> connection is necessary because Odoo cannot automatically assign specific tracking numbers during
> the sync process.
>
> Keeping this link active causes a synchronization failure for every FBA order. By
> disconnecting them, the system bypasses the tracking requirement and allows the sync to complete.

![Example of a kit product linked to an Amazon SKU in the Offers page in the Sales app.](../../../../_images/link-amazon-sku.png)

### Create the BoM for the product kit

Navigate to the product kit by clicking the Sales app ‣ Products ‣ Products and
select the product kit. Click the  Bill of Materials smart button and
[create a kit BoM](../../../inventory_and_mrp/manufacturing/advanced_configuration/kit_shipping.html#manufacturing-advanced-configuration-kit-bom).

In the Components tab, click Add a line and type in the name of the Amazon
product that is tracked by lots or a unique serial number.

> **Warning:**
>
> The Amazon product must be **the sole component** of the kit BoM.

![Example of the kit BoM for the kit product to represent the Amazon listing.](../../../../_images/amazon-product-bom-kit.png)

Now the Amazon product can be processed and tracked accurately in the **Sales** app by using the kit
product and its associated BoM.

---

# Shopee Connector

The **Shopee Connector** synchronizes orders between Shopee and Odoo, which considerably reduces the
amount of time spent manually entering Shopee orders (from the Shopee Seller account) into Odoo. It
also allows users to accurately keep track of Shopee sales in Odoo.

## Supported features

The **Shopee Connector** is able to:

- Synchronize (Shopee to Odoo) all confirmed orders, and their order items, which include:

  - Product name
  - SKU reference
  - Quantity
- Synchronize (Odoo to Shopee) all available quantities of your products (FBM).
- Support multiple seller accounts.
- Support multiple Shopee marketplaces (shops) per seller account.

> **Note:**
>
> The **Shopee Connector** is designed to synchronize sales orders data. Other actions, such as
> downloading weekly/monthly income/fees reports, handling disputes, or issuing refunds, **must**
> be managed from the *Shopee Seller Central*, as usual.

## Shopee supported marketplaces

| **APAC region** | |
| --- | --- |
| Indonesia | Shopee.co.id |
| Taiwan | Shopee.tw |
| Vietnam | Shopee.vn |
| Thailand | Shopee.co.th |
| Philippines | Shopee.ph |
| Malaysia | Shopee.com.my |
| Singapore | Shopee.sg |

| **South America region** | |
| --- | --- |
| Brazil | Shopee.com.br |
| Chile | Shopee.cl |
| Colombia | Shopee.com.co |
| Mexico | Shopee.com.mx |

> **Note:**
>
> - [Shopee Connector configuration](shopee_connector/setup.html)
> - [Shopee order management](shopee_connector/manage.html)

---

# Shopee Connector configuration

Odoo allows users to synchronize with Shopee Seller account in the database, but users **must**
have a registered **Shopee Seller account** and a **Shopee Open account** prior to completing the
configuration.

Set up an Open Shopee account by first going to the [Shopee Open Platform](https://open.shopee.com/), and click the Get Access (Now) button located in the
middle of the page.

Use the [Open Shopee Developer Guide](https://open.shopee.com/developer-guide/12), and follow the
registration process. Once all done, proceed to follow the instructions below to register and link
the Open Shopee account in Odoo.

> **Warning:**
>
> Shopee Open Platform access and seller account requirements are **regionally specific**. This
> means the rules, qualifications, and processes differ from country to country. Before proceeding
> with Odoo’s Shopee Connector setup, verify the requirements for *your* specific Shopee region.
>
> **Key Considerations:**
>
> - **Shopee Seller Status & Business Type:** You must have an active Shopee seller account
>   (Individual or Registered Business). Your eligibility depends on your region and business
>   registration.
> - **Order Volume/Seller Tier (If Applicable):** Many regions require a minimum number of orders
>   within a specific time frame or a certain seller tier (e.g., Mall, Preferred, Managed) to
>   access the Open Platform.
>
> **Action Required:**
>
> 1. Identify your Shopee region.
> 2. Locate the official Shopee documentation for your region.
>    [Open Shopee Developer Guide](https://open.shopee.com/developer-guide/12)
> 3. Carefully review the requirements for seller accounts and Open Platform access in your
>    region.
> 4. Ensure your Shopee account meets all the necessary criteria *before* proceeding with the
>    Odoo Shopee Connector configuration.

## Connect Shopee seller account to Odoo

[Install](../../../general/apps_modules.html#general-install) the Shopee Connector (`sale_shoppe`) by going to
Apps.

Then connect your Shopee Open account by navigating to Sales app ‣ Configuration
‣ Shopee ‣ Accounts.

From here, click New to create to link a new Shopee account.

Then, in the Credentials tab, select the appropriate API Endpoint from the
drop-down menu.

> **Note:**
>
> Shopee offers several API endpoints for production and testing. Selecting the correct endpoint
> is crucial for successful integration. Choose the endpoint that corresponds to your marketplace
> location.
>
> - Shopee Production Endpoint (Singapore): This is the primary endpoint for sellers in
>   most APAC countries. Select this option unless you are specifically operating within mainland
>   China or Brazil.
> - Shopee Production Endpoint (China): This endpoint is exclusively for sellers
>   operating within mainland China. It is designed to comply with local regulations and business
>   practices.
> - Shopee Production Endpoint (Brazil): This endpoint is dedicated to sellers
>   operating within Brazil. Select this option if your Shopee store is based in Brazil.
> - Shopee Testing Endpoint: This endpoint is for development and testing purposes
>   only. Use it to simulate interactions with the Shopee API without affecting your live data.
>   **Do not use this endpoint for production.**
> - Shopee Testing Endpoint (China): Similar to the general testing endpoint, this one
>   is specifically for testing integrations related to the China-specific production endpoint.
>   **Do not use this endpoint for production.**

After selecting the correct API Endpoint in the Credentials form, input your Open
Shopee Partner ID and Partner Key in the corresponding fields. Then click
Save And Authorize.

> **Warning:**
>
> You’ll need your Open Shopee Partner ID and Partner Key to complete this
> step. Here’s how to find them in the Shopee Open Platform:
>
> 1. **Log in to the Shopee Open Platform:** [Log in](https://open.shopee.com/) with the
>    credentials you used to register your Open Shopee account.
> 2. **Navigate to App Management:** Go to the App Management section, then select
>    App List.
> 3. **Select your app:** Choose the specific app you want to synchronize with Odoo (either your
>    test app or your production app).
> 4. **Find your credentials:** Within the app details, you’ll find your Partner ID and Partner
>    Key. These are the values you’ll need to copy and paste into the corresponding fields in
>    Odoo.

> **Note:**
>
> - **Copy carefully:** Copy the Partner ID and Partner Key accurately, without any extra spaces
>   or characters. These are case-sensitive.
> - **Keep your key secure:** Your Partner Key is sensitive information. Do not share it with
>   anyone. Treat it like a password.

## Authorization and account registration

After entering connecting the [Shoppe Seller account to Odoo], the authorization
process begins.

### Shopee seller account selection/login

Upon clicking Save and Authorize, Odoo redirects to the Shopee seller account selection
page.

- **Already logged in:** If you are already logged in to a Shopee account, your email address or
  username will be displayed. Click on your account to proceed.
- **Not logged in:** If you are not logged in, you will be prompted to enter the credentials
  (email/username and password) of the Shopee seller account you wish to connect to Odoo.

### Granting access to Odoo

After selecting or logging into your Shopee seller account, you will be directed to the
authorization (or consent) page. Here, confirm that you allow Shopee to grant Odoo access to your
account and related data. This step is essential for the integration to function correctly.

## Account registration and Shopee shop creation

Upon confirming access, Shopee redirects you back to Odoo. An indicator appears, confirming that
your Shopee account has been successfully registered.

### Post-synchronization configuration

After the redirection, you should perform the following steps within Odoo:

1. **Rename the Shopee Account (Optional):** The newly created Shopee account in Odoo will likely
   have a default name. You can rename it to something more descriptive (e.g., the name of your
   Shopee shop) for easier management.
2. **Set the Last Order Synchronization Date:** This setting determines the starting point for
   fetching orders from Shopee. Choose a date from which you want Odoo to retrieve past orders.
3. **Configure Inventory Synchronization:** Decide whether you want to synchronize your product
   inventory between Odoo and Shopee. Enable the Synchronize Inventory option to
   automatically push stock updates from Odoo to Shopee. Disabling this option prevents automatic
   inventory updates.
4. **Assign a Default Sales Team:** Assign a default sales team to your Shopee account in Odoo.
   This helps with reporting and order management.

With the Shopee account successfully registered, the marketplaces available with this specific
account can later be synchronized the exact same way, and listed under the Shops
button.

## Shopee orders in Odoo

When a Shopee order is synchronized, only lines for items are created on the sales order in Odoo.
Each one represents one for the product that was sold on Shopee.

![Shopee synchronized sale order in Odoo.](../../../../_images/shopee-sales-odoo.png)

Any necessary price reconciliation related to shipping or income versus fees can be managed later
using Shopee’s weekly / monthly financial reports, which can then be imported into the Odoo
**Accounting** app.

The selection of a database product for a sales order item is done by matching its
Internal Reference (a customizable product reference identifier in Odoo, like `FURN001`)
with the Shopee *SKU*.

If no database product with a matching internal reference is found for a given
Shopee SKU, then a default database product, *Shopee Item*.

> **Note:**
>
> To modify default products, activate the [developer mode](../../../general/developer_mode.html#developer-mode), and navigate to
> Sales app ‣ Configuration ‣ Settings. In the Connectors section,
> under Shopee Sync, find the Default Products.

## Product tax configuration

To allow for tax reporting of Shopee sales with Odoo, the taxes applied to the sales order items are
those set on the product, or determined by the [fiscal position](../../../finance/fiscal_localizations.html).

Make sure to have the correct taxes set on your products in Odoo, or have it done by a fiscal
position, to avoid discrepancies in the subtotals between *Shopee Seller Central* and Odoo.

> **Note:**
>
> As shopee does not necessarily apply the same taxes as those configured in Odoo, it may happen
> that order totals differ by a few cents between Odoo and *Shopee Seller Central*. Those
> differences can be resolved with a write-off when reconciling the payments in Odoo.

## Add a new marketplace

To add a new marketplace, follow these steps:

1. **Navigate to Shopee Accounts:** Go to Sales ‣ Configuration ‣ Accounts.
2. **Create a New Shopee Account:** Click New to create a new Shopee marketplace
   account.
3. **Select the API Endpoint:** Choose the appropriate API endpoint for your local market.
   (Typically, this will be Shopee Production Endpoint (Singapore) unless you are
   operating in mainland China or Brazil. Refer to the documentation for details on endpoint
   selection).
4. **Enter Credentials:** Your Partner ID and Partner Key are the same as
   those linked to your unique Open Shopee account. Enter these values in the corresponding fields.
5. **Name Your Shop:** Give the new shop a descriptive name (e.g., `Shopee Philippines`) to identify
   it later.
6. **Assign a Sales Team:** Assign a relevant sales team (e.g., `Shopee Sales Philippines`) to
   enable advanced reporting capabilities.
7. **Synchronize Your Account:** If none of your existing marketplaces are listed, click
   Log in with another account to synchronize a new one. This will initiate the Shopee
   authorization process.

### Automatic synchronization

Newly added marketplaces are automatically added to the list of synchronized marketplaces. If a new
marketplace does *not* appear in the list after synchronization, it indicates that the marketplace
is either incompatible with the Shopee Open Platform or unavailable for your specific seller
account. Consult the Shopee Open Platform documentation or contact their support for further
assistance.

> **Warning:**
>
> While Odoo allows creating the same Shopee shop multiple times, only one instance will function
> due to token limitations. To avoid order management issues, synchronize each shop only once. For
> connection updates, manually fetch orders first before re-establishing the connection.

> **Note:**
>
> - [Shopee supported features and marketplaces](../shopee_connector.html)
> - [Shopee order management](manage.html)

---

# Shopee order management

## Product catalog mapping

### New Odoo customers with no existing products

If you are starting a new Odoo database and your products are only on Shopee, you can import your
Shopee product catalog into Odoo.

1. **Export Shopee catalog:** Use the *Mass Function* drop-down to export the product catalog from
   Shopee, ensuring it includes the Shopee SKUs.

   ![Mass Function drop-down in Shopee.](../../../../_images/shopee-seller-centre-product-extract.png)
2. **Import into Odoo:** [Import](../../../essentials/export_import_data.html) the exported catalog
   into Odoo. During the import process, it is *crucial* to map the Shopee SKU to the
   *Internal Reference* field in Odoo. This field will serve as the link between your Shopee and
   Odoo products.

### Existing Odoo customers with products already in Odoo

If you already have products in your Odoo database, you’ll need to map your Shopee listings to your
existing Odoo products.

1. **Export Shopee catalogs:** Use the *Mass Function* drop-down to export the product catalog from Shopee
   (including Shopee SKUs) and [export](../../../essentials/export_import_data.html) your product
   catalog from Odoo (including *Internal References*).
2. **Map in a spreadsheet:** Use a spreadsheet to map the products. Match the Shopee SKU from the
   Shopee export with the corresponding *Internal Reference* from the Odoo export. Create a column
   that links the Shopee SKU with the Odoo *Internal Reference*.
3. **Update Odoo products:** Import the updated spreadsheet back into Odoo. Use the mapping you
   created in the spreadsheet to update the *Internal Reference* field of your existing Odoo
   products with the corresponding Shopee SKU. This establishes the link between your Odoo and
   Shopee products.

> **Warning:**
>
> Product catalog synchronization between Odoo and Shopee is **not automatic**. It is a
> **manual operation** that you must initiate. The process differs depending on whether your
> products already exist in Odoo.

## Order synchronization

Orders are automatically fetched from Shopee, and synchronized in Odoo, at **regular intervals**.

The synchronization is based on the Shopee orders status: only orders whose status has changed
since the last synchronization are fetched from Shopee. This includes changes on Shopee only.

When an order is canceled on Shopee, it will update the order’s status in Odoo. On the other hand,
if an order is canceled on Odoo, the change won’t be reflected on Shopee.

For every synchronized order, Odoo creates a sales order and a customer (contact), as long as the
customer hasn’t been previously imported from Shopee or doesn’t already exist in the database.

> **Note:**
>
> The principal of the synchronization is to *only fetch orders that needs to be shipped*
> (i.e., `SHIPPED`, `CANCEL`, `UNPAID`, `COMPLETED`).

## Force synchronization

In order to force the synchronization of an order, whose status has **not** changed since the
previous synchronization:

Then, navigate to the Shopee account in Odoo Sales app ‣ Configuration ‣ Shopee
‣ Account ‣ Shop. Modify the date for Last Order Sync under Orders
Follow-up.

Be sure to pick a date that occurs prior to the last status change of the desired order to
synchronize and save. This will ensure synchronization occurs correctly.

## Manage deliveries in FBM

Whenever an FBM (Fulfilled by Merchant) order is synchronized in Odoo, a picking is instantly
created in the **Inventory** app, along with a sales order and customer record.

When a picking related to the order is confirmed, you also have to click on Arrange
Shipment in your Shopee Seller Account in order to be able to generate and fetch the
Shipping Label and Tracking Number.

### Shopee delivery statuses

Understanding the different Shopee delivery statuses is crucial for managing your orders
effectively. Here’s a breakdown:

- **Ready to ship:** The seller can now arrange shipment for this order.
- **Shipment arranged:** The seller has arranged shipment online and received a tracking number
  from the third-party logistics (3PL) provider.
- **Shipped:** The parcel has been dropped off at the 3PL location or picked up by the 3PL
  provider.
- **Cancelled:** The order has been canceled.
- **Pickup failed:** The 3PL parcel pickup attempt failed. The seller needs to rearrange shipment,
  and the rest of the order fulfillment content.

![Shopee delivery status in Odoo.](../../../../_images/shopee-delivery-orders-status.png)
> **Warning:**
>
> Unsupported for Non-Shopee Supported Logistics (NSSL)
>
> This feature is not available for NSSL, you have to
> manually create shipping label and tracking number via the logistics provider’s website/app.
> Check your region for list of supported logistics (e.g. [Malaysia](https://seller.shopee.com.my/edu/article/388)).
>
> Shopee requires users to provide a tracking reference with each delivery. This is needed to
> assign a carrier.
>
> If the carrier doesn’t automatically provide a tracking reference, one must be set manually.
> This rule applies to all Shopee marketplaces.

## Follow deliveries in Odoo

For FBM orders, the stock move is automatically created in Odoo by
the Shopee connector, thanks to the shipping status of Shopee.

![Stock move created for Shopee order in Odoo.](../../../../_images/shopee-wh-out.png)

### Order fulfillment process

This section describes the process of fulfilling Shopee orders within Odoo, from order creation to
inventory updates.

1. **New order creation:** When a new order is placed on Shopee, it is automatically created in
   Odoo.
2. **Arrange shipment on Shopee:** Before the order can be shipped, you **must** arrange the
   shipment through the Shopee platform itself. This usually involves selecting a shipping
   provider, generating a shipping label, and scheduling pickup or drop-off. Odoo does *not*
   handle the physical shipping arrangements; this is managed entirely within Shopee.
3. **Fetch Shopee shipping label (delivery note):** Once the shipment is arranged on Shopee,
   Odoo fetches the generated shipping label (which serves as the delivery note). This label
   contains crucial information like the tracking number and is essential for printing and
   attaching to the package. The shipping label is imported into Odoo and associated with the
   corresponding sales order.
4. **Validate stock out in Odoo:** After the shipping label is retrieved, you need to validate the
   stock movement in Odoo. This confirms that the ordered items have left your warehouse or
   inventory. Validating the stock out will decrease the stock levels in Odoo.
5. **Inventory update on Shopee:** Finally, Odoo pushes the updated stock levels back to Shopee.
   This ensures that your Shopee listings reflect the current inventory, preventing overselling and
   keeping your product availability accurate. This synchronization keeps your Shopee storefront
   up-to-date with your Odoo inventory.

## Register payments

Since customers pay Shopee as an intermediary, creating a dedicated *Bank* journal (e.g. named
`Shopee Payments`), with a dedicated *Bank and Cash* intermediary account is recommended.

Additionally, as Shopee makes a single weekly or monthly payment, selecting all the invoices linked
to a single payment is necessary when registering payments.

To do that, use the appropriate Journal dedicated to Shopee payments, and select
Batch Deposit as the Payment Method.

Then, select all the generated payments, and click Actions ‣ Create batch payment
‣ Validate.

> **Note:**
>
> This same action can be performed with vendor bills from Shopee dedicated to fees/commissions.
>
> When the balance is received in the bank account at the end of the week/month, and the bank
> statements are recorded, credit the Shopee intermediary account by the amount received.

## Analyzing Shopee sales with Odoo’s reporting

Odoo’s dashboard consolidates sales data from all your connected sales channels, providing a
comprehensive overview of your business performance. To specifically analyze your Shopee sales, you
will need to configure sales teams for your Shopee shops. This setup enables you to filter and
isolate Shopee sales data within the Odoo dashboard.

### Setting up sales teams for Shopee reporting

By default, the Shopee account’s sales team is shared across all of your company’s accounts. To
generate separate reports for specific Shopee shops or marketplaces, you’ll need to assign dedicated
sales teams.

1. **Assign a sales team to your Shopee shop:** Navigate to the Shopee account configuration
   (typically found under Sales ‣ Configuration ‣ Accounts). Within the
   account details, assign a specific sales team to your Shopee shop.
2. **Filtering Shopee sales on the dashboard:** Once sales teams are assigned, you can use the
   dashboard filters to view sales data specifically for your Shopee shops. Select the appropriate
   sales team to isolate and analyze your Shopee performance.

> **Note:**
>
> - [Shopee supported features and marketplaces](../shopee_connector.html)
> - [Shopee Connector configuration](setup.html)

---

# Lazada Connector

---

# Lazada Connector features

The **Lazada Connector** synchronizes orders, products, and inventory between Lazada and Odoo,
streamlining your operations across Southeast Asia’s marketplaces. It reduces manual data entry
between systems and enhances order management, enabling efficient tracking of Lazada sales within
Odoo.

## Supported features

The **Lazada Connector** is able to:

- Synchronize (Lazada to Odoo) all confirmed orders (FBM) with
  status READY\_TO\_SHIP or PROCESSED, including:

  - Product name
  - SKU reference
  - Quantity
- Synchronize (Odoo to Lazada) all available product quantities (FBM).
- Synchronize the Lazada product catalog into Odoo or map existing Odoo products to Lazada SKUs.

The following table lists capabilities provided by Odoo when using the Lazada Connector:

|  | Fulfilled By Lazada (FBL) | Fulfilled By Merchant (FBM) |
| --- | --- | --- |
| **Orders** | Synchronize completed orders. | Synchronize all confirmed and unshipped orders. |
| **Stock Management** | Managed by Lazada, and synchronized with a virtual location to track it in Odoo. | Managed in Odoo Inventory app, and synchronized with Lazada. |
| **Delivery Notifications** | Handled by Lazada. | Delivery information is fetched from Lazada, and synchronized in Odoo. |

> **Note:**
>
> The **Lazada Connector** is designed to synchronize sales orders and inventory. Other
> actions, such as downloading monthly fee reports, handling disputes, or issuing refunds,
> **must** be managed from the *Lazada Seller Center*, as usual.

## Lazada supported marketplaces

| **Southeast Asia region** | |
| --- | --- |
| Indonesia | Lazada.co.id |
| Malaysia | Lazada.com.my |
| Philippines | Lazada.com.ph |
| Singapore | Lazada.sg |
| Thailand | Lazada.co.th |
| Vietnam | Lazada.vn |

> **Note:**
>
> - [Lazada Connector configuration](setup.html)
> - [Lazada order management](manage.html)

---

# Lazada Connector configuration

This guide explains how to set up the **Lazada Connector** in Odoo to integrate your Lazada Seller
account(s) and manage multiple marketplaces efficiently in Southeast Asia. Follow these steps to
configure your account, synchronize your product catalog, and prepare your shop for go-live.

## Prerequisites

Before configuring the **Lazada Connector**, ensure you have:

- A Lazada Seller account
  (Personal Self-Developed or Enterprise Self-Developed).
- A valid email address and phone number for verification.
- A digital copy of your business license (for Enterprise Self-Developed accounts).
- A brief description of your integration purpose (e.g., “Connecting Odoo ERP to our Lazada store
  for order and inventory synchronization”).

> **Note:**
>
> The *Lazada Open Platform* account for API access is separate from your *Lazada Seller account*.

## Create a Lazada Open Platform account

1. Open [Lazada Open Platform](https://open.lazada.com/) and click Create Account or
   Sign Up.
2. Navigate to the profile and in the Basic information, begin filling in the fields to
   start the registration process.

   Under account information, select one of the following selections for Partner type:

   - Personal Self-Developed: For individuals without a business license.
   - Enterprise Self-Developed: For businesses with a registered license.

> **Warning:**
>
> Do **not** select other service provider types, as they are not applicable for Odoo integration.

3. Continuing on the same page, fill out the following information to complete registration under
   the **Personal information** section:

   - Enter your phone number, email, and address. Complete any verification steps (e.g.,
     OTP via SMS).
   - For Enterprise Self-Developed accounts, upload your business license.
   - Provide a brief introduction (e.g., “Integration for Odoo ERP to sync orders, inventory, and
     fees with Lazada”).
4. After completing the details, click Submit to submit your profile details. Approval
   typically takes a few hours to a couple of business days. Check your registered email for
   confirmation or requests for additional information.
5. If approval status is rejected, review the reason in the notification email or on the
   *Lazada Open Platform Console*. Edit and resubmit as needed.

> **Note:**
>
> Ensure profile details are accurate to avoid delays. Common issues include incorrect account
> type selection or missing business license documents.

## Create an app on Lazada Open Platform

To obtain the App Key and App Secret for Odoo integration:

1. Log in to the [Lazada Open Platform Console](https://open.lazada.com/), navigate to
   App Console, App Management, and click Create App.

   ![../../../../_images/lazada-open-platform-app-console.png](../../../../_images/lazada-open-platform-app-console.png)
   ![../../../../_images/lazada-create-app.png](../../../../_images/lazada-create-app.png)
2. For App Category, select Seller In-house APP.
3. Fill out the rest of the application form:

   - Provide your Odoo database URL and tester account credentials (name and password).
   - For APP IP Address Management, select IP address(es) unavailable
     and enter “The application is cloud-hosted.”
4. Click Submit to process the application. The app creation takes approximately 24
   hours. Once approved, note the App Key and App Secret.

## Connect Lazada Seller account to Odoo

1. To connect a Lazada Seller account in Odoo, navigate to App from your Database,
   search for Lazada, and click Activate.

   ![../../../../_images/lazada-connector-odoo-app.png](../../../../_images/lazada-connector-odoo-app.png)
2. Enable Lazada Sync by navigating to Sales app ‣ Configuration.

   ![../../../../_images/lazada-odoo-sales-menu.png](../../../../_images/lazada-odoo-sales-menu.png)
3. Connect a Lazada Seller account:

   - Go to Sales ‣ Configuration ‣ Lazada ‣ Shops and click
     Create New Shop.
   - Enter a name (e.g., “Lazada Malaysia”), App Key, App Secret, and
     select the marketplace (e.g., Lazada.com.my).![../../../../_images/lazada-connect-new-shop-odoo.png](../../../../_images/lazada-connect-new-shop-odoo.png)
4. Link the account by doing the following:

   - Click Create Shop & Authorize.
   - Click the button to redirect to the Lazada login or consent page. Log in with your Lazada
     Seller account credentials and grant Odoo access.

     ![../../../../_images/lazada-authorize-shop.png](../../../../_images/lazada-authorize-shop.png)
   - Upon successful authorization, Odoo lists available marketplaces under the
     Lazada Shops tab.

     ![../../../../_images/lazada-odoo-shop-list.png](../../../../_images/lazada-odoo-shop-list.png)
5. Manage Marketplaces:

   - Newly added marketplaces are automatically synchronized. To disable synchronization for
     specific marketplaces, remove them from the list.
   - Avoid synchronizing the same shop multiple times to prevent duplicate orders.

> **Warning:**
>
> To maintain data integrity, ensure each shop is synchronized only once. If synchronization
> fails, try manually fetching orders before reconfiguring.

## Configure the shop before go-live

1. Set up warehouses:

   - Navigate to Sales app ‣ Configuration ‣ Settings ‣ Connectors ‣ Lazada
     ‣ Lazada Shops.
   - Select the Lazada shop and configure the FBM Warehouse field to limit stock
     fetching to specific warehouses.
   - By default, all accounts use the same Lazada stock location. To isolate stock for a specific
     marketplace, create a separate account registration and assign a unique stock location.

> **Note:**
>
> To manually trigger re-initialization of the catalog, clear the
> Last Catalog Synchronization before clicking Sync Catalog.

2. Synchronize the product catalog:

   The product catalog is automatically matched during the first synchronization. However, it is
   recommended to synchronize the product catalog in the following scenarios:

   - Use the Sync Catalog button in Odoo to automatically fetch active Lazada products
     daily.
   - For new Odoo databases, export the Lazada catalog from *Lazada Seller Center* (including
     SKUs). Import into Odoo via Inventory app ‣ Products ‣ Import, mapping SKUs
     to the Internal Reference field.
   - For existing Odoo products, export both Lazada and Odoo catalogs, map SKUs to
     Internal References in a spreadsheet, and import the updated mappings back into
     Odoo.

> **Note:**
>
> Test catalog synchronization with a small product set to verify SKU mappings before full import.

> **Note:**
>
> - [Lazada Connector features](features.html)
> - [Lazada order management](manage.html)

---

# Lazada order management

This guide explains how to manage Lazada orders, inventory, deliveries, and sales reporting within
Odoo using the **Lazada Connector**. It covers product catalog mapping, order synchronization,
delivery processes, and sales analysis to streamline your marketplace operations in Southeast Asia.

## Product catalog mapping

### New Odoo customers with no existing products

If you are starting a new Odoo database and your products exist only on Lazada, you can import your
Lazada product catalog into Odoo.

1. In [Lazada Seller Center](https://sellercenter.lazada.com.ph/), use the Bulk Manage
   drop-down to export your product catalog, including Lazada SKUs.

   ![../../../../_images/lazada-bulk-edit.png](../../../../_images/lazada-bulk-edit.png)
2. Import the exported catalog into Odoo via Inventory ‣ Products ‣ Import.
   Map the Lazada SKU to the Internal Reference field in Odoo to link your Lazada and
   Odoo products.

### Existing Odoo customers with products already in Odoo

If you have an existing product catalog in Odoo, map your Lazada listings to these products.

- Use the Sync Product Catalogue button in Odoo to automatically match active Lazada
  products.

  > ![../../../../_images/lazada-sync-product.png](../../../../_images/lazada-sync-product.png)

> **Warning:**
>
> Product catalog synchronization is an automated process initiated by the synchronization.

## Order synchronization

Orders are automatically fetched from Lazada and synchronized in Odoo at regular intervals
(every 60 minutes).

- Only orders with status READY\_TO\_SHIP or PROCESSED are fetched, as these
  require shipping action.
- When an order is canceled on Lazada, its status updates in Odoo. However, cancelling an order in
  Odoo does not reflect on Lazada.
- For each synchronized order, Odoo creates a sales order and a customer (contact) if the customer
  has not been previously imported or does not exist in the database.

> **Note:**
>
> Only orders requiring shipment are synchronized. Orders with statuses SHIPPED,
> CANCEL, UNPAID, or COMPLETED are excluded during
> synchronization.

## Force synchronization

To synchronize an order whose status hasn’t changed since the last synchronization:

1. Navigate to Sales app ‣ Configuration ‣ Lazada ‣ Shops.
2. Select the Lazada Shop and modify the Last Order Sync date under
   Synchronization Information to a date prior to the order’s last status change.
3. Save to trigger synchronization.

> **Note:**
>
> In Debug Mode, access the Lazada shop in Odoo and click Sync Orders to immediately
> synchronize orders or Sync Inventory for inventory updates.

## Manage deliveries in FBM

For FBM orders, the **Lazada Connector** creates a picking in the
Inventory app, along with a sales order and customer record, upon synchronization.

1. Arrange by comfirming the picking in Odoo, then navigate to *Lazada Seller Center* and click
   Pack Lazada Package to generate the tracking number. Odoo retrieves the shipping
   label and attahces it to the corresponding delivery order.
2. Validate the stock movement in Odoo to update inventory levels and confirm the order has left
   the warehouse.

### Lazada package statuses

Understanding Lazada package statuses is crucial for effective order management:

- Package Pending on Lazada: The package is awaiting receipt, tagging, or processing in
  the warehouse system.
- Package Confirmed on Lazada: The package has been packed by the seller or warehouse
  and is confirmed ready for courier pickup or dropoff. Lazada is notified and updates the order
  status.
- Ready to Ship on Lazada: The order is ready for shipment. Lazada is notified and
  updates the order status.
- Delivered on Lazada: The parcel has been dropped off or picked up by the logistics
  provider.
- Canceled on Lazada: The order has been canceled.
- Manual handling required: The package cannot be processed on Odoo and requires manual
  handling on Lazada.

> **Warning:**
>
> Lazada requires a tracking reference for each delivery. If the carrier doesn’t provide one
> automatically, set it manually in *Lazada Seller Center*. Check supported logistics providers
> for your region (e.g., Malaysia).

### Order fulfillment process

1. Lazada orders are automatically created in Odoo as sales orders. Select the desired sales order
   in the **Sales app**.
2. Click Pack Lazada Package to arrange shipment in the delivery transfer if you are
   using supported logistics providers. Odoo imports the shipping label (delivery note) and
   tracking number, associating them with the sales order.
3. Confirm the stock movement in Odoo to reduce inventory levels.

## Invoice and register payments

Due to Lazada’s policy of not sharing customer email addresses, invoices cannot be sent directly
from Odoo. Instead:

1. Generate invoices in Odoo and manually upload them to *Lazada Seller Center*.
2. Register Payments:

   - Create a dedicated Bank Journal (e.g., “Lazada Payments”) with a Bank and Cash
     intermediary account.
   - Since Lazada processes batch payments weekly or monthly, select all invoices linked to a
     payment in Odoo.
   - Use Batch Deposit as the Payment Method, select the invoices, and go to
     Actions ‣ Create Batch Payment ‣ Validate.
3. Reconcile the payments after Lazada deposits the balance. Record it in the bank statement and
   credit the Lazada intermediary account.

> **Note:**
>
> Apply the same process for vendor bills related to Lazada commissions.

## Analyzing Lazada sales with Odoo Reporting

Odoo’s dashboard consolidates sales data from all channels. To analyze Lazada sales specifically:

1. Set Up Sales Teams:

   - Navigate to Sales app ‣ Configuration ‣ Settings ‣ Connectors ‣ Lazada
     ‣ Shops.
   - Assign a dedicated sales team to each Lazada shop for isolated reporting.
2. Use the dashboard filters to view sales data for the assigned Lazada sales team.

> **Note:**
>
> Configure separate sales teams for each Lazada marketplace to generate detailed performance
> reports.

> **Note:**
>
> - [Lazada Connector features](features.html)
> - [Lazada Connector configuration](setup.html)

---

# Gelato

Gelato is a global print-on-demand platform that integrates with Odoo to sync product catalogs and
automate order fulfillment.

Connecting Gelato’s services with Odoo’s **Sales** and **eCommerce** apps enables the following:

- Sync Odoo sales orders with Gelato for automated order fulfillment
- Create and manage Gelato products within Odoo; supports product variant and image sync
- Configure delivery options in Odoo and receive order updates via webhooks.

## Configuration

> **Warning:**
>
> The company information (*Company name* and *Billing address*) in the Gelato account *must* match
> the company information in the Odoo database in order for sales orders to be confirmed and sent
> to Gelato for fulfillment.
>
> ![Company information in Gelato.](../../../_images/gelato-company.png)
> ![Company information in Odoo.](../../../_images/odoo-company.png)

### Configure API keys and webhooks in Gelato

Before configuring the Gelato connector in Odoo, first obtain API credentials and webhooks from the
Gelato account.

API connectors enable Odoo **Sales** to send and receive data from Gelato for order processing,
while webhooks provide real-time updates on order status and shipment tracking.

#### API Key

An API Key is a unique authentication token that allows Odoo to securely communicate with Gelato’s
API, enabling order transmission, status updates, and data synchronization.

After logging into Gelato, click  Developer in the left menu bar. From
here, click on API keys. In the new page, click the Add API Key button to
open a new API key form. Type in a name, then click Create Key.

Copy the generated API key using Copy to Clipboard.

![Newly generated API key in the Gelato platform.](../../../_images/gelato-api-key.png)
> **Warning:**
>
> Copy the API key and store it somewhere safe and secure before leaving this page. Once the page
> is refreshed or exited, the key will not be available to copy.
>
> If the key cannot be copied or is lost, return to the API key page and start over,
> creating a new API key.

#### Webhook

A webhook is an automated notification system that instantly updates Odoo when Gelato processes,
ships, or delivers an order, ensuring real-time tracking and minimal manual intervention.

To create a webhook, go to Developer ‣ Webhooks under the Developer
drop-down menu in the left menu bar. In the new page, click Add Webhook to open a
Create Webhook form.

The webhook form requires several specific configurations:

- URL: This tells Gelato where to send the order updates in Odoo. Copy and paste the
  Odoo database URL with the additional suffix `/gelato/webhook`.

  > **Tip:**
  >
  > `https://stealthywood.odoo.com/gelato/webhook`
- Events: Click into the field and select order\_status\_updated. Selecting
  order\_status\_updated ensures Odoo receives order changes automatically.
- Method: Click into the field and select the HTTP Post option, as this is
  the request method used to send data from Gelato to Odoo.
- Tick the checkbox next to I want to take Authorization to this webhook.
- Header Name: In this field, type in `signature` to match the field in Odoo.
- Click Generate Key to generate a Header Value.
- Click Create to complete this webhook configuration.

![Newly configured webhook in the Gelato platform.](../../../_images/gelato-webhook.png)
> **Note:**
>
> Copy and paste the API key and webhook on a notepad before tabbing out of the Gelato webpage as
> backup.

### Configure Gelato connector in Odoo

In Odoo, navigate to Sales app ‣ Configuration ‣ Settings, then scroll to the
Connectors section. Enable the Gelato connector by ticking the checkbox.
Next, paste the newly generated API keys and webhook secret key into their respective fields. Once
saved, Gelato is available in Odoo **Sales** and **eCommerce** products.

## Synchronizing Gelato products with Odoo Sales

It is recommended to have products already configured in Gelato before configuring them in Odoo. To
get the product ID in Gelato, navigate to the Templates page from the side bar menu.
Select which product to synchronize in Odoo, then hover over the product card to reveal the
 (vertical ellipsis) menu icon. Click the menu icon, then click
Copy Template ID to copy the product template ID to the clipboard.

> **Note:**
>
> [Start selling products with Gelato: Quick & easy setup](https://www.gelato.com/blog/get-started-with-gelato-creating-products)

### Odoo Sales product

To create a product in Odoo that matches the Gelato product, navigate to Sales app
‣ Products ‣ Products, select New to create a new product form. Type in the product
Name, then navigate to the Sales tab. Find the Gelato section,
then click into the Template Reference field and paste the copied template ID from the
Gelato product. Finally, click Synchronize.

Successful synchronization pulls the Gelato product variant options into the newly configured Odoo
product.

In the new Print Images field, click the default marker to set a default
product image. Click the  (edit) icon and select the product image file
to upload, then Save & Close.

> **Warning:**
>
> The Print Images field *must* be configured on all Gelato products and their
> respective product variations before they can be ordered.

### Product variants

To view and edit the newly synchronized product variants, navigate to the Attributes &
Variants tab, which will have the variants pulled from the Gelato product configuration. Click the
Configure button to edit and configure the variant images, delivery methods, additional
pricing, etc.

### Order a Gelato product from Odoo

Once synchronized, Gelato products are available to order in Odoo through [sales quotations](sales_quotations.html) or on the **eCommerce** store. Gelato delivery options are automatically
synchronized upon API and webhook configuration.

To add Gelato delivery, click Add shipping on the sales order. Select
Standard Delivery or Express Delivery in the Shipping Method
field, then click Get rate.

Once the quotation is confirmed, it becomes an active sales order, and the order is sent to Gelato
for fulfillment. Once a sales order is sent from Odoo to Gelato, Gelato processes the order,
produces the product at the nearest fulfillment center, and ships it directly to the end-customer.

> **Note:**
>
> [Create quotations](sales_quotations/create_quotations.html)

> **Warning:**
>
> When creating a sales order for Gelato products in the database, only Gelato products can be
> added to the same sales order. Multivendor orders are not available with the Gelato connector at
> this time.