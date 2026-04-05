# Point of Sale — Configuration, Payments & Customization

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

Odoo Point of Sale: configuration, payment methods, hardware (IoT box, receipt printers, scales), restaurant mode, and self-order kiosk. Use when implementing or customising a retail or hospitality POS.

---

# Point of Sale

Odoo **Point of Sale** is designed for managing shops and restaurants. It is web-browser-based,
allowing it to run on any device, and is built to maintain functionality even during temporary
network outages.

Beyond traditional [store](point_of_sale/shop.html) and [restaurant](point_of_sale/restaurant.html) settings, Odoo POS also supports a
[self-ordering](point_of_sale/extra/self_order.html) feature, enabling customers to place orders
and make payments using a dedicated kiosk or their own mobile device.

Odoo POS integrates with all essential point-of-sale hardware, including:

- [Payment terminals](point_of_sale/payment_methods/terminals.html);
- Cash drawers;
- [Cash machines](point_of_sale/payment_methods/cash_machines.html);
- [Scales](point_of_sale/hardware_network/scale.html);
- [Barcode scanners](../inventory_and_mrp/barcode/setup/hardware.html);
- [Customer displays](point_of_sale/hardware_network/customer_display.html);
- [Preparation displays](point_of_sale/extra/preparation.html);
- [Electronic shelf labels](point_of_sale/hardware_network/electronic_labels.html).

This hardware can be connected directly or through an [IoT system](../general/iot.html).

> **Note:**
>
> [Odoo Tutorials: Point of Sale tutorials](https://www.odoo.com/slides/point-of-sale-28)

---

# Use

## Create a POS

If no point of sale exists yet in the database, a set of POS cards is displayed on the Point of Sale
Dashboard. Each card represents a business type. Click a card to create a POS with
preconfigured settings tailored to that type. These settings can be adjusted later as needed.

To create additional POS or to create one from scratch, go to Point of Sale ‣
Configuration ‣ Point of Sales and click New. Then, configure the [POS settings] to meet your specific business requirements.

> **Note:**
>
> Click Configurations > Settings to access more settings.

> **Warning:**
>
> Assign a dedicated [cash payment method](payment_methods.html) and [cash
> journal](../../finance/accounting/get_started/journals.html#accounting-journals-cash) to each POS. This ensures that accounting entries are
> separated and traceable to specific points of sale.

## Access the POS settings

To access the general POS settings, go to Point of Sale ‣ Configuration ‣
Settings. Then, open the Point of Sale dropdown menu and select the POS to configure.

![Dropdown menu to select the POS in the app settings](../../../_images/select-pos-dropdown.png)
> **Note:**
>
> To configure basic settings, access the POS dashboard, click the
> (vertical ellipsis) icon on the relevant POS card, then select Edit.
> In the popup window, you can:
>
> - [Enable multiple employees to log in.](extra/employee_login.html)
> - [Connect and set up an IoT sytem.](hardware_network/pos_iot.html)
> - [Connect and set up an ePOS printer.](hardware_network/epos_ssc.html)

## Open the POS register

Once the POS is fully [configured](hardware_network.html), access the POS interface by opening the
register. Navigate to Point of Sale ‣ Dashboard and:

1. On the relevant POS card, click Open Register.
2. In the Opening Control popup, ensure the Opening cash amount is correct.
3. Click Open Register.

> **Note:**
>
> - Once the register is open, Open Register is replaced by Continue
>   Selling on the POS card.
> - You can switch between [multiple users](extra/employee_login.html) from an open POS register,
>   provided [multi-employee management is enabled](extra/employee_login.html#pos-employee-login-use).

From the POS interface header:

- Click Register to access the register for daily POS actions such as [sales], [refunds], etc.
- Click Orders to access the POS [orders] overview screen and
  retrieve past or ongoing orders.
- Click the  (plus) icon to put the current order aside and start
  a new one.
- Click the order numbers to switch between ongoing orders.
- Search for products using the search bar.
- Click the  (barcode) icon to use a webcam as a barcode scanner.
- Click the user’s avatar to switch between employees, provided [multi-employee management is
  enabled](extra/employee_login.html#pos-employee-login-use).
- Click the  (hamburger menu) icon to access more advanced options, such
  as [closing the register].

## Sell products

The POS register can be divided into three sections: the cart, a pad to adjust cart items, apply
discounts, set customers, etc., and the list of products. To make sales:

1. Click on products to add them to the cart.

   - To change the **quantity**, click Qty and enter the number of products using the
     keypad.
   - To add a **discount**, click % and enter the discount value using the keypad.
   - To modify the product **price**, click Price and enter the new amount using the
     keypad.
2. Once the order is completed, click Payment to proceed to checkout.
3. Select the [payment method](payment_methods.html).
4. Enter the received amount, then click Validate.
5. Click New Order to move on to the next order.

![POS register](../../../_images/pos-register.png)
> **Note:**
>
> - You can use both `,` and `.` on the keyboard as decimal separators.
> - **Cash** is selected by default if no [payment method](payment_methods.html) is manually
>   selected.

## Set customers

Registering customers is necessary to [collect their loyalty points and grant them rewards](extra/pricing.html#pos-pricing-loyalty), automatically apply an [attributed pricelist](extra/pricing.html#pos-pricing-pricelists), or [generate and print invoices](use/pos_invoices.html#pos-invoices-invoices).

To create customers from [the POS register]:

1. Click Customer.
2. Click Create.
3. Complete the customer form information and save.

To create customers from the backend:

1. Go to Point of Sale ‣ Orders ‣ Customers.
2. Click New.
3. Fill in the customer form information.

To assign a customer to an order, click Customer to access the customer list on the POS
register or the payment screen, and select the desired customer.

> **Note:**
>
> Creating a new customer from the POS register or the payment screen assigns them automatically to
> the current order upon saving.

### Send marketing messages

Customers’ contact details, such as their phone number or email addresses, are stored
automatically when sending [receipts](use/receipts.html) by email, SMS or Whatsapp. They can then
be used, for example, for [marketing](../../marketing.html) purposes.

To send marketing messages manually from the POS application, go to Point of Sale
‣ Orders ‣ Orders, open a POS order form, navigate to the Contact Info category
under the Extra Info tab, then click the  (email) icon or
 (whatsapp) icon.

> **Note:**
>
> - [Email Marketing](../../marketing/email_marketing.html)
> - [SMS Marketing](../../marketing/sms_marketing.html)
> - [WhatsApp](../../productivity/whatsapp.html)

## Orders overview

The Orders overview allows for viewing, searching, and retrieving orders from the POS
interface. To access it, click Orders in the header.

Then, search for orders in the search bar using their:

- Reference
- Receipt Number
- Date
- Customer
- Delivery Channel
- Delivery Order Status

To filter orders based on their status, click the Active dropdown menu and select one of
the following options:

- Active: Orders currently in progress. This includes orders marked as
  Ongoing, as well as those in the Payment or the Receipt stages
  (i.e., orders for which the receipt has been emailed to the customer).
- Paid: Paid orders.

To navigate between pages, click the  or
(caret) icon.

To access an order in the register, click it, then click Load Order.

> **Note:**
>
> Paid orders can be [refunded].

> **Note:**
>
> - To define the number of orders visible on a page, click `1-x / x`. Enter a number lower than
>   the total number of pages, and click Ok.
> - Click the  (trash) icon next to an Active order to
>   delete it.
> - If using [presets](restaurant.html#pos-restaurant-orders-preset), click one to view the related orders.
>   Click it again to return to the main overview.

## Return and refund products

To refund a returned product, follow these steps:

1. [Open or access the register] from the POS dashboard.
2. Click the  (vertical ellipsis) button, then
   Refund.

   > **Note:**
   >
   > Alternatively, you can refund orders from the [orders overview] screen.
   > Access the list of orders and filter them by status to display only Paid orders.
3. Select the relevant order from the order list.
4. Select the items and use the keypad to set the refund quantity, then click Refund.
5. Choose how to handle the refund:

   - To reimburse the customer, select a payment method on the payment screen, then click
     Validate.
   - To issue a [gift card](../sales/products_prices/ewallets_giftcards.html#ewallet-gift-gift-cards) for the refund amount, click
     Back. A new order containing the returned items (with negative quantities) is
     created automatically. Then, add the gift card from the product list to the order; its value
     is set automatically to match the total refund amount. Click Payment, then
     Validate the refund.

> **Note:**
>
> - You cannot add other products to the cart until the refund has been validated.
> - Alternatively, refunds can be processed by:
>
>   > - Selecting the returned product(s) from the POS register and setting a negative quantity
>   >   equal to the number of returned items. To do so, click Qty and +/-,
>   >   and update the quantity accordingly.
>   > - Selecting the returned product(s) from the POS register and a [preset](restaurant.html#pos-restaurant-orders-preset) set up for the return mode.
>   > - Accessing the POS dashboard, navigating to Point of Sale ‣ Orders ‣
>   >   Orders, selecting an order, and clicking Return Products.

Once the return is validated, a corresponding credit note is generated, referencing the original
[receipt](use/receipts.html) or [invoice](use/pos_invoices.html).

> **Note:**
>
> [Credit notes and refunds](../../finance/accounting/customer_invoices/credit_notes.html)

## Notes

Notes allow you to attach extra information to specific products in an order. There are two types of
notes: internal notes and customer notes.

### Internal notes

Internal notes provide information meant for staff (e.g., `no tomato` for the kitchen). These notes
do not appear on the customer’s receipt. To add a note to an order, ensure no item is selected and
click Note. Likewise, to add a note to one specific item, select it from the cart and
click Note. Then, add or modify the note’s content in the popup that opens:

> - Type the note directly into the window, or
> - Use a configured note model to save time if the same content is frequently used. Click on the
>   desired note model to insert its text.

To create or edit note models, navigate to Point of Sale ‣ Configuration ‣
Note Models, click New or the relevant note model, then complete or edit the
Name column.

### Customer notes

Notes for customers appear on [receipts](use/receipts.html) and [invoices](use/pos_invoices.html).
They can be used, for example, to provide warranty details for a high-value item or specific care
instructions, such as `Dry clean only`.

To add a **customer note** from the [POS register] to a specific item,
select a product from the cart and click the  (vertical ellipsis)
button. Click Customer Note, then add the note’s content in the popup window.

> **Note:**
>
> - If no item is selected, the note applies for the whole order.
> - Product notes from an [imported SO](shop.html#pos-shop-so) are displayed identically in
>   the cart.

![Customer note button and notes (SO and POS register) on products in the cart](../../../_images/customer-notes.png)

## Manage the cash register

Odoo POS allows you to determine which coins and bills are accepted. To set up the allowed coins and
bills:

1. Navigate to Point of Sale ‣ Configuration ‣ Coins/Bills.
2. Click New to add a new value.
3. Select the POS where this value is available in the Point of Sale column or leave the
   field empty to make it available for all POS.

To record a cash in or cash out transaction not associated with a sale:

1. Click the  (hamburger menu) icon on the POS interface.
2. Click Cash In/Out.
3. In the popup that opens, select Cash In or Cash Out.
4. Enter the amount.
5. Specify the reason for the addition or removal of cash, and Confirm.

> **Note:**
>
> Only employees with [basic or advanced access rights](extra/employee_login.html#pos-employee-login-configuration)
> are allowed to perform cash in/out actions.

## Close the POS register

To close the POS register, click the  (hamburger menu) icon, then
Close Register.

In the Closing Register pop-up that opens, you can view:

- The number of orders and the total amount made during the session.
- The expected amounts grouped by payment method.

1. Click  (money) to specify the number of each coin and bill.
2. Click Confirm to return to the previous pop-up window. The computed amount is set in
   the Cash Count field, and the Closing Details are specified in the
   Closing Note section.
3. Click Close Register to close the register and post accounting entries.

> **Note:**
>
> Click  (clone) to automatically fill in the field with the expected
> cash amount.

> **Note:**
>
> - When the money counted does **not** match the expected amount, a Payments
>   Difference window automatically pops up. Selecting Proceed Anyway validates the
>   session and automatically posts the discrepancy to the designated cash difference journal.
> - Closing the register of a [restaurant](restaurant.html) POS when orders are still in draft
>   and not scheduled for later is not allowed and opens a pop-up window on which you can either
>   Review Orders or Cancel Orders.
> - It is strongly advised to close the POS register at the end of each day.

> **Note:**
>
> - [Shop features](shop.html)
> - [Restaurant features](restaurant.html)

---

# Receipts

|  |  |
| --- | --- |
| POS receipts display the following elements:   - The company logo - The receipt and order number - The customizable header and footer - The name of the cashier and the customer   (provided a customer was [set for the order](../use.html#pos-use-customers)) - The complete order, discounts, prices, and used   payment methods - Optionally, a QR code or URL link for customers to   generate [invoices](pos_invoices.html) | ../../../../_images/receipt.png |

To set up POS receipts, navigate to the [POS settings](../use.html#pos-use-settings) and scroll down to
the Bills & Receipts section.

- To customize the header and footer, activate the Header & Footer setting
  and fill in both fields with the information to be printed on the receipts.
- To print receipts automatically once a payment is registered, enable the Automatic
  Receipt Printing setting.
- To print receipts that don’t display product prices, enable the Basic Receipt setting.
- Receipts can be sent by email by default, but also by SMS or through WhatsApp. To do so, activate
  the SMS Enabled or WhatsApp Enabled option(s).

  > **Note:**
  >
  > The WhatsApp Enabled setting is only available if the WhatsApp
  > Messaging module is [installed](../../../general/apps_modules.html#general-install).

> **Note:**
>
> - [Bills and payment](../restaurant.html#pos-restaurant-bills)
> - [Invoices](pos_invoices.html)
> - [Receipt printers](../hardware_network/receipt_printers.html)

## Reprint a receipt

To reprint a receipt, navigate to the [POS interface](../use.html#pos-use-open-register), click
Orders, open the dropdown selection menu next to the search bar, and change the default
All active orders filter to Paid. Then, select the order and click
Print Receipt.

> **Note:**
>
> Filter the list of orders using the search bar: type in your reference and select
> Receipt Number, Date, or Customer.

---

# Invoices

Point of Sale allows you to issue and print invoices for [registered customers](../use.html#pos-use-customers) upon payment and retrieve all past invoiced orders.

> **Note:**
>
> An invoice created in a POS creates an entry into the corresponding [accounting journal](../../../finance/accounting/get_started/cheat_sheet.html#cheat-sheet-journals) [configured in the POS settings].

## Configuration

To define the default journals for a specific POS, go to the [POS’ settings](../use.html#pos-use-settings), scroll down to the Accounting section, and select the appropriate
journals for Orders and Invoices under Default Journals.

![accounting section in the POS settings](../../../../_images/invoice-config.png)
> **Note:**
>
> Specific journals can also be defined for each [payment method](../payment_methods.html).

## Invoice a customer

To invoice a customer, first make sure a [customer is set](../use.html#pos-use-customers) for the order.
Then, upon [processing the payment](../use.html#pos-use-sell), click Invoice underneath the
customer’s name to issue an invoice for that order.

Select the payment method and click Validate. The invoice is automatically issued
and ready to be downloaded and/or printed.

## Retrieve invoices

To retrieve the invoice of a POS order, follow these steps:

1. Go to Point of Sale ‣ Orders ‣ Orders.
2. Click the relevant invoiced order in the list.
3. On the order form, click the Invoice smart button.

> **Note:**
>
> - Invoiced orders have the Fully Invoiced Invoice Status.
> - You can filter the list of orders to only display invoiced orders in the list: click the search
>   bar and select the Invoiced filter.

## QR codes to generate invoices

Customers can also request an invoice by scanning the QR code printed on their receipt. Upon
scanning, they must fill in a form with their billing information and click Get my
invoice. The invoice is then generated and available for download and the order’s status is
updated to Fully invoiced.

To use this feature, enable QR codes on receipts by going to Point of Sale ‣
Configuration ‣ Settings. Then, select the POS in the Point of Sale field, scroll
down to the Bills & Receipts section, and enable Use QR code on ticket.

---

# Products

Products can be created from the backend or the POS interface. To manage products from the backend,
go to Point of Sale ‣ Products ‣ Products. Click New to create a
product, or open an existing one to edit it. Update the fields as needed and ensure the
Point of Sale checkbox is enabled at the top of the form.

To create products from the POS interface, access the POS register, click the
(hamburger menu) icon, then Create Product. Enter the product details in the
pop-up window and click Save. The product is immediately available in the register.

To update an existing product from the POS register, long-click a product to open the information
pop-up, and click Edit. Change the necessary product details and click Save
to return to the POS register.

> **Note:**
>
> [Product creation (video tutorial)](https://youtu.be/b5eVusXHEvg?si=Xn3EBMmRfJ35mqyu)

## POS product categories

POS product categories are used to organize products in the POS register.

To manage POS categories, follow these steps:

1. Navigate to Point of Sale ‣ Configuration ‣ PoS Product Categories.
2. Click New to create a category or click an existing one to update it.
3. Classify and build a hierarchy between categories: Associate a category with a parent
   category by filling in the Parent Category field. A parent category groups one or
   more child categories (e.g., use `Drinks` to group `Hot beverages` and `Soft drinks`).

Once POS product categories are created, assign them to specific products:

1. Go to Point of Sale ‣ Products ‣ Products and open a product form.
2. Navigate to the Point of Sale tab and fill in the Category field with one
   or multiple POS categories.

To limit the categories displayed on the POS register, navigate to the [POS settings](use.html#pos-use-settings) and select the relevant categories in the Restrict Categories field
under the Product & PoS categories section.

## Product combos

A product combo is a bundle of multiple products sold together as a unit. Each product combo
consists of multiple categories, known as [combo choices], and
each combo choice contains several items. When purchasing a product combo, customers can select one
or more items from each combo choice.

> **Tip:**
>
> A burger menu is offered as a product combo including three combo choices: one burger, one
> drink, and one portion of fries. For each combo choice, customers select one item from the
> available options (e.g., cheeseburger or chicken burger; soda or water; regular or large fries).

> **Note:**
>
> [Product combos (video tutorial)](https://youtu.be/H8e2CakLhaQ?si=yjPbvYkj00K7OP3q)

### Combo choice creation

To create the combo choices that will be added to the [product combo], follow the next steps:

1. Go to Point of Sale ‣ Products ‣ Combo Choices and click New.
2. Enter a name for the Combo Choice.
3. Set the maximum selectable items for the combo choice using the Maximum items field.
4. Set the number of items included in the combo choice using the Includes items field.
5. Click Add a line under the Options section to add the products that
   constitute the Combo Choices.
6. If needed, click a product to add an Extra Price.

> **Note:**
>
> - The Combo Price field shows the price applied to any additional product a customer
>   might select (i.e., when the Maximum items field is set to `2` or higher). This
>   price is automatically calculated based on the price of the least expensive product defined in
>   the Combo Choice.
> - The Extra Price field is used to set an additional charge for a specific product in
>   the combo choice, e.g., to cover higher costs or encourage upselling. This extra price is
>   applied each time a customer selects that product within the combo choice.

### Product combo creation

To create a specific product that contains [combo choices],
follow the next steps:

1. Go to Point of Sale ‣ Products ‣ Products and click New.
2. Enter a product name.
3. Set the Product Type to Combo and select the relevant [Combo
   Choices].
4. Add a Sales Price.
5. Optionally, click the Point of Sale tab to select the preferred Category.

> **Note:**
>
> [Product variants](../sales/products_prices/products/variants.html)

### Combo application

To apply combos, follow these steps:

1. Open the [POS register](use.html#pos-use-open-register).
2. Click the desired product combo, and select the preferred items for each combo choice.
3. Click Add to order.
4. Continue with the order process.

> **Note:**
>
> The total price of the product combo, as displayed in the [POS register](use.html#pos-use-open-register), is based on the Sales Price defined on the [product
> combo’s form]. Selecting several products in the combo choices and
> selecting a product with an Extra Price influences the total price.
>
> The Office Combo has a Sales Price of **300** € and offers a
> selection of chairs and desks. The combo choice for chairs includes a conference chair, an
> office chair, and an armchair with a maximum selectable amount set to 2. The Combo
> Price for the chair combo choice is **35** € per added item because the conference chair is
> the least expensive product. The armchair has an Extra Price of **100** € because
> it is made of leather. Selecting the conference chair with the armchair increases the price
> of the Office Combo to **435** €. Thus, selecting the armchair adds **35** €
> (Combo Price) + **100** € (Extra Price).
>
> ![../../../_images/office-combo.png](../../../_images/office-combo.png)

## Serial numbers and lots

Using **lots** and **serial numbers** allows you to track product movements throughout their
lifecycle. When traceability is enabled, Odoo identifies a product’s location based on its last
recorded movement.

To track products by lots or serial numbers:

1. [Enable the Lots & Serial Numbers setting](../../inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers.html#inventory-product-management-traceability-setting).
2. [Configure your products and assign tracking numbers](../../inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers.html#inventory-product-management-assign-sn).

### Selling tracked product

Adding a tracked product to the cart from the POS register imports its serial number or lot number
automatically.

When you [load a quotation/SO](shop.html#pos-shop-so) containing tracked products, a pop-up window asks
to confirm if the numbers linked to the SO should be imported. Click
Ok to proceed. Once imported, the tracking numbers appear in the cart below the
corresponding products, next to the  (Valid product lot) icon.

### Tracking status and manual changes

Tracking numbers can be monitored and modified using the  (product lot)
icon:

- **Green**  (Valid product lot) **icon**: The tracking number was
  successfully imported or assigned.
- **Red**  (Invalid product lot) **icon**: The tracking number is
  missing or incorrect.
- **Modification:** To change a tracking number, click the  (Valid
  product lot) icon and select a different lot or serial number from the pop-up window.

> **Note:**
>
> An invalid or missing tracking number does not block a sale. However, it triggers a warning
> pop-up that must be acknowledged before proceeding to the payment screen.

> **Note:**
>
> - [Serial numbers](../../inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers.html)
> - [Lot numbers](../../inventory_and_mrp/inventory/product_management/product_tracking/lots.html)

---

# Hardware and network

Odoo Point of Sale supports integration with a variety of hardware, including [payment
terminals](payment_methods/terminals.html), cash drawers, [customer displays](hardware_network/customer_display.html), [scales](hardware_network/scale.html), [barcode scanners](../../inventory_and_mrp/barcode/setup/hardware.html), [receipt printers](hardware_network/receipt_printers.html), and in-store [electronic shelf labels](hardware_network/electronic_labels.html).

---

# Local Network Access

[Local Network Access](https://developer.chrome.com/release-notes/142#local_network_access_restrictions)
is a security feature that limits a website’s ability to send requests to servers on a local
network. Access requires explicit user permission, which makes it possible to grant network access
to a specific web page. Using LNA, Odoo Point of Sale can communicate with devices with local
access, such as [supported ePOS printers](receipt_printers.html#pos-epos-printers-supported-printers), directly
from the browser and without requiring an [SSL certificate](epos_ssc.html).

> **Note:**
>
> Local Network Access is available in most browsers based on [Chromium version 142](https://developer.chrome.com/release-notes/142) or higher, including Google Chrome, Brave,
> Microsoft Edge, Vivaldi, and Opera.

> **Warning:**
>
> The ePOS printer must have a **static IP address**; otherwise, it may become unreachable. The
> static IP should be configured through the router.

## Activation

To activate LNA and ensure POS uses it over a secure connection, create a new system parameter
as follows:

1. [Enable the developer mode](../../../general/developer_mode.html#developer-mode).
2. Go to Settings ‣ Technical ‣ System Parameters.
3. Click New and fill in the fields:

   - Key: `point_of_sale.use_lna`
   - Value: `True`
4. Click Save.

## Browser permission

Once LNA is activated in Odoo and a device with local access, such as an [ePOS printer](receipt_printers.html#pos-epos-printers-supported-printers), is configured, the browser displays a popup requesting
permission to communicate with the devices on the local network.

![Permission popup to access local network devices](../../../../_images/pos-lna.png)
> **Note:**
>
> - If the popup does not appear, permission can be granted manually through the browser’s site
>   settings.
> - Some browsers may require enabling a flag to activate the feature:
>
>   - Brave: `brave://flags/#local-network-access-check`
>   - Google Chrome: `chrome://flags/#local-network-access-check`

## Point of sale LNA status

To view the point of sale’s LNA status, [open](../use.html#pos-use-open-register) or access the
register, click the  (hamburger menu) icon in the top-right corner, then
click the Local Network Access button at the bottom of the menu. The current LNA
status details are then displayed in the LNA Permission status popup.

---

# IoT system connection

To connect the POS with an [IoT system](../../../general/iot.html):

1. Make sure both the Point of Sale and Internet of Things (IoT) apps are installed on your
   database.
2. Set up the [IoT box](../../../general/iot/iot_box.html) or
   [Windows virtual IoT](../../../general/iot/windows_iot.html).
3. Connect the peripheral devices to the IoT system:

   | Device | Instructions |
   | --- | --- |
   | Printer | Connect a supported receipt printer to a USB port or to the network, and power it on. Refer to [Order printing](../restaurant.html#pos-restaurant-orders-printing). |
   | Cash drawer | The cash drawer should be connected to the printer with an RJ25 cable. |
   | Barcode scanner | The barcode scanner must end barcodes with an `ENTER` character (keycode 28) in order for the barcode scanner to be compatible. This is most likely the barcode scanner’s default configuration. |
   | Scale | [Connect the scale and power it on](scale.html). |
   | Customer display | [Connect a screen](customer_display.html) to the IoT box to display the PoS order. |
   | Payment terminal | The connection process depends on the terminal. Refer to the [payment terminals documentation](../payment_methods.html). |
4. [Connect the IoT system to your Odoo database](../../../general/iot/connect.html).
5. In the Connect to a Point of Sale popup that opens, select the Associated
   POS and click Continue. The IoT system and its devices are automatically linked to
   the POS.

   > **Note:**
   >
   > Alternatively, [access the POS settings](../use.html#pos-use-settings) and select the POS, or click
   > the vertical ellipsis button (⋮) on a POS card and click Edit. Then,
   > enable IoT Box, select the devices to use with the POS, and click
   > Save.

> **Note:**
>
> - [List of supported hardware](https://www.odoo.com/page/point-of-sale-hardware).
> - [IoT documentation](../../../general/iot.html)

## Setup example

![A suggested configuration for a point of sale system.](../../../../_images/pos-connections.png)

---

# Receipt printers

Receipt printers integrate with Point of Sale systems to receive print jobs directly from the POS.
Once properly configured and connected, this integration enables automatic receipt printing for
every completed transaction.

> **Warning:**
>
> Epson printers are strongly recommended. The following printers are compatible with Odoo:
>
> - Network-based printers that support the ePOS communication protocol (without IoT), such as
>   the TM-m30 iii (model 112 or 152).
> - ePOS printers with USB connectivity that need to be connected to an [IoT system](../../../general/iot/connect.html).
> - ESC/POS printers that require a connection via an [IoT system](../../../general/iot/connect.html) using either a USB or network-based interface.
>
> Bluetooth printers are not compatible with Odoo.

> **Note:**
>
> - [Receipt printers without IoT (video tutorial)](https://youtu.be/OUUi6N_xT-U?si=NZ9PPrsXDUcJ4kSy)
> - [Receipt printers with IoT (video tutorial)](https://youtu.be/ORojunUs5Bs?si=FrDJ0N-9f8SJlQrA)

## Configuration

To configure the printer, connect it to a power source, then to the network using either Wi-Fi or
an Ethernet cable. Then, power the printer on; an automatic ticket with the printer’s IP address
gets printed upon connection. Keep it for the configuration process.

To link the printer with Point of Sale, follow the next steps:

1. Go to Point of Sale ‣ Configuration ‣ Settings.
2. Scroll down to the Connected Devices section and enable ePos Printers.
3. Type the printer’s IP address in the dedicated field.
4. Click Save.

Enable the [Local Network Access](pos_lna.html) to allow Point of Sale to communicate directly with the printer on the
same network. Alternatively, once the printer is connected to Odoo, ensure the connection is
secure and reliable by generating a [self-signed certificate](epos_ssc.html#pos-epos-ssc-certificate).

> **Note:**
>
> - [Local Network Access](pos_lna.html)
> - [Self-signed certificate for ePOS printers](epos_ssc.html)
> - [Connect a printer](../../../general/iot/devices/printer.html)

## Directly supported ePOS printers

The **Epson TM-m30 i/ii/iii (Wi-Fi or Ethernet only) models** are strongly recommended, as they have
been fully tested with Odoo Point of Sale.

Other Wi-Fi or Ethernet Epson printer models that support the **ePoS protocol** should also be
compatible.

> **Warning:**
>
> - The printer must be capable of operating in HTTP mode.
> - When using [Local Network Access (LNA)](pos_lna.html), the printer must have a **static
>   IP address**; otherwise, it may become unreachable. The static IP should be configured
>   through the router.

## Printers with IoT system integration

The following printers require an [IoT system](../../../general/iot/devices/printer.html) to
be compatible with Odoo:

- Epson TM-T20 family (incompatible ePOS software)
- Epson TM-T88 family (incompatible ePOS software)
- Epson TM-U220 family (incompatible ePOS software)

## Troubleshooting

To resolve common hardware issues, including connectivity failures, configuration errors, and
physical maintenance, follow the instructions below:

- Check the printer’s blinking lights to help identify the source of a problem.
- If the printer does not print the first automatic ticket with the IP address, check the network
  cable or Wi-Fi connection.
- If the receipt comes out blank, the paper roll may be upside down; try flipping it.
- If the POS cannot connect to the printer, make sure the printer’s IP address entered in Odoo
  matches the one on the first automatically printed ticket. Also, ensure the router assigns the
  printer a static IP address.

---

# Electronic shelf labels

Electronic shelf labels allow you to display product information like prices and barcodes on store
shelves and to synchronize them remotely from the backend. This removes the need to print new labels
when product information changes.

> **Note:**
>
> Odoo uses electronic labels from [Pricer](https://www.pricer.com/).

## Configuration

### Pricer setup

1. [Get in touch with Pricer](https://www.pricer.com/contact) to create and configure your Pricer
   account.
2. Create your stores: one pricer store equates to one physical store.
3. Link as many transceivers as needed to the Pricer store(s).
4. Create the following variables to share product information between your Odoo database system and
   Pricer. These variables act like placeholders on the label template.

   - `itemId`: this holds the unique internal identifier assigned to each product
   - `itemName`: the actual name of the product
   - `price`: the selling price of the product, including any applicable taxes
   - `presentation`: the template name used in Pricer for displaying the product information on the
     label
   - `currency`: the currency of your company (e.g., USD, EUR)
   - `barcode`: the barcode number associated with each product
   > **Warning:**
   >
   > The names for these variables must be **identical** in your Pricer database.
5. Create a template named `NORMAL`. This template is used to display information on your digital
   tags.

Once your account, stores, variables, and template are configured on Pricer, you can proceed with
the setup of your Odoo database.

> **Warning:**
>
> The account associated with your Pricer store must have access to send API requests to Pricer.

### Odoo setup

As a pre-requisite, [activate](../../../general/apps_modules.html#general-install) the POS Pricer module *(technical
name: pos\_pricer)* to have all the required features to use Pricer electronic tags.

![Installing POS Pricer module from Apps](../../../../_images/pricer-module.png)

Once the module is activated, configure your [pricer stores] and associate
[Pricer tags] with your products.

#### Pricer stores

Similarly to the configuration in Pricer, you need to create one pricer store per physical location.
To do so, go to Point of Sale ‣ Configuration ‣ Pricer Stores, click
New, and fill in the line with the required information:

- Store Name: you can put any name of your liking.
- Pricer Tenant Name: the name of your company account in Pricer, usually followed by
  `-country_code`. This value is provided by Pricer.
- Pricer Login: the login of your Pricer account.
- Pricer Password: the password of your Pricer account.
- Pricer Store ID: the ID of the related Pricer store as defined on your Pricer
  database.

![Configuring a Pricer Store](../../../../_images/pricer-stores-setup.png)
> **Note:**
>
> - The Pricer Tags column is updated automatically when a label is linked to a
>   product.
> - The Last Update and Last Update Status columns are updated
>   automatically when the tags are updated.

#### Pricer tags

For a label to display specific product information, the label needs to be associated with the
product. To do so:

1. Open the product form by going to Point of Sale ‣ Products ‣ Products and
   clicking New or selecting an existing product.

   > **Note:**
   >
   > If you are creating a new product, configure and save it before associating any Pricer tags.
2. Go to the Sales tab, scroll to the Pricer section, and select the
   corresponding Pricer Store.

   ![Linking Pricer tags to products](../../../../_images/pricer-product.png)
3. Fill in the Pricer tags ids field by copying the label’s ID from the label itself or
   scanning its barcode.

   > **Note:**
   >
   > Pricer tag IDs are composed of a letter followed by 16 digits.

> **Note:**
>
> - We recommended using a barcode scanner to speed up the encoding process.
> - When setting up Pricer with Odoo for the first time, it is recommended that you configure only
>   one product first. Before configuring more products, ensure you can display their information
>   on a Pricer tag.

Now that you have a product associated with a Pricer tag, we can send its information to Pricer.

### Practical application

Odoo automatically sends requests to Pricer to synchronize the tags every 12 hours if you make any
modifications to:

> - Product name, price, barcode, or customer taxes
> - Currency
> - Associated Pricer store or Pricer tags

To force the update, activate the [developer mode](../../../general/developer_mode.html#developer-mode). Then:

1. Go to Point of Sale ‣ Configuration ‣ Pricer Store.
2. Select the desired store(s).
3. Click Update tags to update all tags affected by changes to:

   - Product name, price, barcode, or customer taxes
   - Currency
   - Associated Pricer store or Pricer tags

Alternatively, click Update all tags to force the update of every tag, regardless of
whether changes were made.

![Update all Pricer tags](../../../../_images/update-all.png)

If Pricer has processed and accepted the request, the status field shows Update
successfully sent to Pricer. If there is any issue, the system displays an error message.

> **Warning:**
>
> If a request sent to Pricer fails, Odoo still considers that the product has been updated. In
> that case, we recommend forcing the update of all tags.

### Discount labels

To display a discount label on a Pricer Tag, you need to link a [pricelist](../extra/pricing.html#pos-pricing-pricelists) to the product variant associated with the tag.

To do so, open the product variant form:

1. Go to Point of Sale ‣ Products ‣ Product Variants.
2. Select the product you want to apply a discount to.

Then, set the desired pricelist:

1. Go to the General Information tab.
2. Select a pricelist in the Pricer Sales Pricelist field.

Once a pricelist is set, the On Sale Price field appears, showing the Sales
Price with the discount applied.

![Linking a pricelist to a product variant](../../../../_images/pricer-sales-pricelist.png)

After updating your electronic labels, a `PROMO` tag should appear on the electronic label,
displaying both the old, crossed-out price and the discounted price.

> **Note:**
>
> - Currently, pricelists that offer discounts for purchasing multiple units or derive their prices
>   from other pricelists are not supported.
> - Assigning a pricelist to a product variant only affects the electronic label display. Scanning
>   the product at the point of sale does not automatically apply the discount.

> **Note:**
>
> [Discounts](../extra/pricing.html#pos-pricing-discounts)

---

# Customer display

The **customer display** feature provides real-time updates on a secondary screen for customers
during the checkout process. This screen shows the [items in the cart](../use.html#pos-use-sell), the
subtotal as items are added, and details throughout the payment process. It also displays the total
amount, the selected [payment method](../payment_methods.html), and any change to be returned.

![customer screen](../../../../_images/display.png)
> **Note:**
>
> Both the customer and POS displays must have a minimum diagonal size of 6 inches. For optimal
> readability, larger screens are recommended.

## Configuration

Depending on the POS setup, the feature can be displayed directly on a secondary screen connected
via USB-C or HDMI or on a screen connected through an IoT system.

The feature is activated by default, but its background image can still be configured. To do so,
navigate to the [POS settings](../use.html#pos-use-settings) and scroll down to the Connected
Devices section. Then, click Upload your file to set a background image.

For displays connected using an [IoT system](../../../general/iot.html):

1. Navigate to the [POS settings](../use.html#pos-use-settings).
2. Enable the IoT Box option to activate the IoT system in POS.
3. Click Save, which activates the IoT app in Odoo.
4. [Connect and configure an IoT system](../../../general/iot/connect.html) for a
   [display](../../../general/iot/devices/screen.html).
5. Return to the [POS settings](../use.html#pos-use-settings) and select an IoT-connected screen using the
   Customer Display field.

## Opening the customer display

To open the customer display, follow these steps:

1. [Access the POS register](../use.html#pos-use-open-register).
2. Click the  (hamburger menu) icon.
3. Click the  (Customer Display) icon, which opens the customer
   display either in a new window to drag onto the second screen or directly onto the IoT-connected
   screen.

> **Note:**
>
> For IoT-connected screens, both devices need to be connected to the same local network.

> **Note:**
>
> - [IoT system connection](pos_iot.html)
> - [Internet of Things (IoT)](../../../general/iot.html)

For POS terminals running the
[Odoo](https://play.google.com/store/apps/details?id=com.odoo.mobile) Android app with dual-screen
support, follow these steps:

1. [Activate the Point of Sale Mobile module](../../../general/apps_modules.html) to enable the
   customer display.
2. [Access the POS register](../use.html#pos-use-open-register).
3. Click the  (hamburger menu) icon.
4. Click the  (Customer Display) icon, which opens the customer
   display on the terminal’s secondary screen.

---

# Scale

> **Warning:**
>
> In EU member states, [certification is legally required](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG)
> to use a scale as an integrated device.

## Prerequisite

Connecting a scale requires the use of an **IoT System**.

> **Note:**
>
> - [IoT system connection to Odoo](../../../general/iot/connect.html)
> - [Connect a scale](../../../general/iot/devices/scale.html)

## Configuration

### Scale connection

1. [Access the POS settings](../use.html#pos-use-settings).
2. Scroll down to the Connected Devices section and enable IoT Box.
3. Select the scale in the Electronic Scale field.
4. Click Save.

> **Note:**
>
> Alternatively, click the  (Dropdown menu) icon on a POS card and
> click Edit to access this setting.

### Product configuration

In order to weigh products using an integrated scale, go to Point of Sale ‣
Products ‣ Products, create a product or open an existing product form, and configure it as
follows:

1. Ensure the Point of Sale checkbox is activated for the product to be available in
   POS.
2. On the General Information tab, define a Sales Price per kg.

   > **Note:**
   >
   > This step requires to enable the [Units of Measure](../../../inventory_and_mrp/inventory/product_management/configure/uom.html) feature. To
   > activate it:
   >
   > 1. Go to Inventory ‣ Configuration ‣ Settings.
   > 2. Scroll down to the Products section and activate Units of Measure.
3. Go to the Point of Sale tab and activate To Weigh With Scale. This
   enables the product to be weighed directly on the connected scale at the POS.

> **Warning:**
>
> The selected unit of measure for weighable products must be kg to ensure compliance
> with **European regulations**.

> **Note:**
>
> [Units of measure](../../../inventory_and_mrp/inventory/product_management/configure/uom.html)

## European regulations

When using scales in commercial transactions, the database integrated with a scale must be
configured to meet specific European requirements. This includes supporting at least three decimal
places for accuracy and using proper rounding for units of measure, such as `kg` instead of generic
`units`.

If the database is not compliant, a red  (scale) icon displays
as a warning. Click this icon to view the reasons for non-compliance and then select
Apply changes to automatically apply the necessary changes to the settings. Once the
database meets all regulatory requirements, the  (scale) icon
turns green.

![../../../../_images/legal-requirements.png](../../../../_images/legal-requirements.png)
> **Note:**
>
> Both the [customer](customer_display.html) and POS displays must have a minimum diagonal
> size of 6 inches. For optimal readability, larger screens are recommended.

## Using a scale in PoS

1. [Access the POS register](../use.html#pos-use-open-register).
2. Select the product to weigh on the order screen or scan its barcode.
3. Place the product on the scale and wait for the weight to be displayed in the popup window.
4. Once the weight is determined, the price is automatically computed.
5. Click Order  to add the product to the cart.
6. Remove the previous product from the scale.

![weighing window](../../../../_images/weigh.png)
> **Warning:**
>
> Make sure the scale returns to `zero` before weighing a new product. If it does not, the
> Order  button remains unclickable until it is reset.

---

# Self-signed certificate for ePOS printers

> **Warning:**
>
> Since the [Chromium 142 update](https://developer.chrome.com/release-notes/142), using a
> self-signed certificate is no longer required. The recommended approach is to use the
> [Local Network Access](pos_lna.html) method instead.

To work with Odoo, some printer models that can be used without an [IoT system](../../../general/iot.html) may require the HTTPS protocol to establish a secure connection
between the browser and the printer. However, trying to reach the printer’s IP address using HTTPS
results in a warning page in most web browsers. Force the connection to establish an HTTPS link and
enable the printer in Odoo.

## Generation, export, and import of self-signed certificates

Printers that operate without an [IoT system](../../../general/iot.html) still require secure
communication, which can be achieved by [generating],
[exporting], and/or [importing] a self-signed certificate.

> **Warning:**
>
> - Generating a self-signed certificate should only be done **once**. Creating another
>   certificate causes devices using the previous one to lose HTTPS access.
> - Printers that use an [IoT system](../../../general/iot.html) do not need a
>   self-signed certificate, as the IoT box generates it automatically.
> - For stable results, it is strongly recommended to use the Google Chrome browser to generate
>   the self-signed certificate.

> **Note:**
>
> To export self-signed certificates from an operating system or a web browser that is not
> mentioned in this documentation, search for `export SSL certificate` and the name of your
> browser or operating system in the preferred search engine. Similarly, to import self-signed
> certificates, search for `import SSL certificate root authority` in the preferred search engine.

### Self-signed certificate generation

The generation process depends on the OS and the browser.

Windows 10 & LinuxMac OS

To generate a self-signed certificate on **Google Chrome**, follow the next steps:

1. Open the browser, type the printer’s IP address in the search bar (e.g.,
   `https://192.168.1.25`), and press `Enter`.
2. On the security warning page, click Advanced, then Proceed to
   [IP address] (unsafe) to force the connection.
3. On the EPSON platform, click Advanced Settings, then Administrator
   Login to log in to the printer’s homepage.
4. Type the initial password located at the back of the printer in the Current
   Password field, then press `Enter`.
5. Go to Network Security ‣ SSL/TLS ‣ Certificate.
6. On the Certificate page, click Update under the
   Self-signed Certificate section.
7. Adapt the Common Name field to retain only the IP address, then click
   Next, then OK. Wait for the printer’s lights to stop blinking.

![Warning page about the connection privacy on Google Chrome](../../../../_images/browser-https-insecure.png)
> **Note:**
>
> The Epson homepage may vary depending on the printer model used. For the Epson TM-m30 ii,
> log in to the Epson homepage by typing `epson` as the username and the printer’s serial
> number as the password.

To generate a self-signed certificate using the [Keychain Access](https://support.apple.com/en-gb/guide/keychain-access/kyca8916/mac) app on Mac, follow the
next steps:

1. Access the Keychain Access app on Mac.
2. Go to Access ‣ Certificate Assistant ‣ Create a Certificate.
3. Enter a name for the certificate.
4. Select an identity type, then the type of certificate.
5. Click Create.
6. Review the certificate, then click Done.

### Self-signed certificate export

The export process depends on the OS and the browser.

Windows 10 & LinuxMac OS

Google ChromeMozilla Firefox

> To export the certificate, follow the next steps:
>
> 1. Once the printer’s lights are solid, hover the mouse over the browser’s search bar
>    and click Not secure, then Certificate details.
> 2. Click the Details tab in the Certificate Viewer popover, then
>    click Export.
> 3. Add `.crt` next to the IP address in the File name field.
> 4. Set the Save as type field to `Base64-encoded ASCII, single certificate`.
> 5. Click Save.

To export the certificate, follow the next steps:

1. Click Not secure next to the search bar.
2. Go to Connection not secure ‣ More information.
3. Click View certificate in the Security tab, then
   Details.
4. Select the certificate, click Export, then select a folder in your local
   drive.
5. Click Close.

Google ChromeMozilla Firefox

To export the certificate, follow the next steps:

1. Open the browser, type the printer’s IP address in the search bar (e.g.,
   `https://192.168.1.25`), and press `Enter`.
2. On the security warning page, click Advanced, then Proceed
   to [IP address] (unsafe) to force the connection.
3. Click Not secure next to the search bar, then Certificate is
   not valid.
4. Go to the Details tab and click Export.
5. Add `.crt` at the end of the file name to ensure it has the correct extension.
6. Select `Base64-encoded ASCII, single certificate`, at the bottom of the
   popover.
7. Click Save.

To export the certificate, follow the next steps:

1. Open the browser, type the printer’s IP address in the search bar (e.g.,
   `https://192.168.1.25`), and press `Enter`.
2. Click Not secure next to the search bar.
3. Go to Connection not secure ‣ More information.
4. Click View certificate in the Security tab, then
   Details.
5. Select the certificate, click Export, then select a folder in your local
   drive.
6. Click Close.

### Self-signed certificate import

The import process depends on the OS and the browser.

Windows 10LinuxAndroid OSiOS

To import a self-signed certificate from **Google Chrome**:

1. Open the browser.
2. Go to Settings ‣ Privacy and security ‣ Security, and click
   Manage certificates.
3. Click Manage imported certificates from Windows on the Certificate
   Manager page.
4. Click Import in the Certificates popover.
5. In the Certificate Import Wizard, click Next, then
   Browse to select the certificate, and click Next again.
6. Select the Place all certificates in the following store option.
7. Click Browse, select the Trusted Root Certification Authorities
   folder, and click OK.
8. Click Next, then Finish.
9. Click Yes in the Security Warning popover.

> **Note:**
>
> To import a self-signed certificate using **Mozilla Firefox** on Windows, see the steps in
> the Linux tab.

Google ChromeMozilla Firefox

To import a self-signed certificate, follow the next steps:

1. Open the browser.
2. Go to Settings ‣ Privacy and security ‣ Security, and click
   Manage certificates.
3. Click Installed by you under the Custom section on the
   Local certificates tab.
4. Click Import next to Trusted Certificates, and select the
   exported certification file from your local drive.
5. Accept all warnings.
6. Click ok.

To import a self-signed certificate, follow the next steps:

1. Open the browser.
2. Go to Settings ‣ Privacy & Security ‣ Security ‣ View
   Certificates.
3. In the Certificate Manager popover, click the Your
   Certificates tab, then Import, and select the certificate in your local
   drive.
4. Click the Servers tab in the Certificate Manager popover.
5. Click Add Exception.
6. Enter the printer’s IP address in the Location field, then click
   Get Certificate.
7. Enable the Permanently store this exception option and confirm.

> **Warning:**
>
> The specific steps for installing a certificate may vary depending on the Android version
> and the device manufacturer.

To import a self-signed certificate into an Android device, first create and export it from a
computer. Then, transfer the `.crt` file to the device via email, Bluetooth, or USB. Once
the file is on the device, install the EPSON ePOS SDK for JavaScript if required, then follow
the next steps:

1. Go to the device settings.
2. Type `certificate` in the search bar.
3. Click Certificate AC, then Install from device storage.
4. Select the certificate file to install it on the device.

> **Note:**
>
> Download the certificate on a computer if the tablet restricts direct downloads. Forward
> the file via email, then open it directly from the tablet to complete the installation.

To import a self-signed certificate into an iOS device, first create and export it from a
computer. Then, transfer the `.crt` file to the device via email, Bluetooth, or any
file-sharing service.

Downloading this file triggers a warning popover. Click Allow to download the
configuration profile, and close the second popover. Then follow the next steps:

1. Go to the **Settings** app on the iOS device.
2. Click Profile Downloaded under the user’s details box.
3. Locate the downloaded `.crt` file and select it.
4. Click Install in the top-right corner.
5. Enter a passcode if needed.
6. Click Install in the top-right corner of the certificate warning screen and
   the popover.
7. Click Done.

Once the certificate is installed, authenticate it as follows:

1. Go to Settings ‣ General ‣ About > Certificate Trust Settings.
2. Enable the installed certificate using the  (switch) toggle.
3. Click Continue in the popover.

## Certificate import verification

To confirm the printer’s connection is secure, connect to its IP address using HTTPS. For example,
navigate to `https://192.168.1.25` in a browser. If the self-signed certificate has been applied
correctly, no warning page appears, and the address bar should display a padlock icon, indicating a
secure connection.

---

# Shop features

## Quotations and sales orders

When working in retail, you might need to access quotations or sales orders created on the Sales app
from the POS register to finalize a sale.

### Select a sales order or quotation

From the POS register, click the  (vertical ellipsis) icon and
 Quotation/Order to open the list of quotations and sales orders created
from the sales application. When imported, the sales order reference number is displayed under
the ordered products, next to the  (shopping basket) icon.

### Apply a down payment or settle the order

Select a quotation or sales order, and on the pop-up that opens, choose the desired settlement
method. The customer can either:

- Settle the order **completely**: Click Settle the order to pay for the total of the
  quotation or sales order.
- Settle the order **partially**:

  1. Select Apply a down payment (percentage) or Apply a down payment
     (fixed amount) to make a down payment for the selected quotation or sales order.
  2. Enter the percentage or fixed amount the customer is paying, and click Apply to add
     the down payment to the cart.

![settlement possibilities for an so](../../../_images/so-settle.png)
> **Note:**
>
> Once a sales order is partially settled, the applied down payment is automatically deducted from
> the order’s total.

> **Note:**
>
> - [Sales quotations](../sales/sales_quotations.html)
> - [Down payments](../sales/invoicing/down_payment.html)

## Ship later

The **Ship Later** feature allows you to sell products and schedule delivery at a later date. It is
useful, for example, when a product is out of stock or so voluminous that it requires to be shipped,
or when, for any reason, the customer needs their order shipped later, etc.

### Configuration

[Go to the POS settings](use.html#pos-use-settings), scroll down to the Inventory section,
and enable Allow Ship Later.

Once activated, you can:

- Choose the location from where the products are shipped by selecting a Warehouse.
- Define a Specific route, or leave this field empty to use the default route.
- Define the Shipping Policy; select As soon as possible if the products
  can be delivered separately, or When all products are ready to ship all the products
  at once.

> **Note:**
>
> - [Delivery methods](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration.html)
> - [Warehouses](../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses.html)

### Practical application

1. [Access the POS register](use.html#pos-use-open-register) and make a sale.
2. On the payment screen, set a customer and select Ship Later.
3. In the pop-up window, set a shipping date and click Confirm to proceed to payment.

The system instantly creates a delivery order from the warehouse to the shipping address.

> **Note:**
>
> The selected customer must have referenced an address in the system for products to be shipped.

## Barcodes

Using a [barcode scanner](../../inventory_and_mrp/barcode/setup/hardware.html) improves efficiency
and provides quicker customer service. In Point of Sale, scanners are used to add products to a
cart, apply discounts, or log employees into the POS register.

Once enabled in the **Inventory** app, you can use the barcode feature with any product that has a
barcode assigned.

> **Note:**
>
> - [Set up a barcode scanner](../../inventory_and_mrp/barcode/setup/hardware.html)
> - [Activate barcode scanners](../../inventory_and_mrp/barcode/setup/software.html)

### Assign barcodes

To use this feature, [assign a barcode to your products](../../inventory_and_mrp/barcode/setup/software.html#inventory-barcode-set-barcodes)
following the [default barcode nomenclature](../../inventory_and_mrp/barcode/setup/software.html).
You can also assign barcodes automatically using the [barcode lookup feature and database](../../inventory_and_mrp/barcode/setup/barcodelookup.html).

> **Note:**
>
> Employees can [log into the POS by scanning a badge](extra/employee_login.html#pos-employee-login-badge). To
> configure this feature, open the **Employees** app, select an employee, then, in the
> HR Settings tab, fill in the PIN Code or Badge ID.

### Discount tags

Discount tags are specific barcodes used to apply a percentage discount to a product. They follow a
specific discount nomenclature that allows the POS to recognize the barcode as a price reduction
rather than a new product. These are commonly used for items nearing their [expiration date](../../inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates.html).

> **Tip:**
>
> A carton of milk is expiring tomorrow. By scanning a barcode following the discount nomenclature
> (e.g., a barcode starting with `2250`), Odoo automatically applies the defined price reduction of
> 50% to the milk during the current transaction.

### Barcode nomenclature

Barcode nomenclatures explain how barcodes are identified and classified. When a barcode is scanned,
it is linked to the first rule that matches its pattern. This pattern syntax adheres to a
standardized method of prefix matching; a barcode is considered a match if its prefix aligns with
the pattern.

Patterns also define how numerical values —such as weight, price, or percentage— are encoded into
the barcode. These are indicated by `{NNN}`, where the `N`’s define the position of the digits.

To view or edit these rules, go to the [POS settings](use.html#pos-use-settings), scroll to the
Inventory section, and click the  (Internal Link) icon
next to Barcode Nomenclature.

For discount tags, use the Discount Barcodes rule. The default pattern is
22{NN}, meaning the barcode must start with `22`, followed by two digits representing
the discount percentage.

![discount tags nomenclature setting form](../../../_images/barcode-nom.png)
> **Note:**
>
> To allow for three-digit discounts (such as `100%`), add an extra `N` to the Barcode
> Pattern field (e.g., `22{NNN}`).

> **Note:**
>
> [Default barcode nomenclature](../../inventory_and_mrp/barcode/operations/barcode_nomenclature.html)

### Use

To use discount tags, scan the product barcode or manually add it to the cart. Then, scan the
discount tag. The discount is automatically applied to the last product added to the cart.

---

# Restaurant features

Odoo Point of Sale provides various features to manage a restaurant or a bar:

- [Organizing the floors and tables];
- [Managing orders];
- [Notifying the kitchen or bar through the POS];
- [Printing and splitting bills];
- [Collecting tips];
- [Setting different taxes for takeout orders](extra/pricing.html#pos-pricing-taxes).

Three main buttons in the POS interface allow for navigating between tables, the register, and
orders:

- Tables: Access the [Floor plan] view to manage table
  occupancy.
- Register: Access the [POS register] to process orders.
- Orders: Access the overview of all orders.

> **Warning:**
>
> To configure restaurant-specific settings, the Is a Bar/Restaurant setting under the
> Point of Sale section must be enabled in the [POS settings](use.html#pos-use-settings).

> **Note:**
>
> When Booking is enabled in the [POS settings](use.html#pos-use-settings), a
> [Booking] button appears on the main interface for viewing
> and managing bookings.

## Default start screen

To define the point of sale’s default start screen, go to the [POS settings](use.html#pos-use-settings), scroll down to the PoS Interface section, and set the
Default Screen setting to Tables (i.e., [Floor plan] view) or [Register].

## Floors and tables

The Floor plan view allows for managing restaurant floors and tables and monitoring
table status in real time (occupancy, reservations, kitchen orders) using the following action
buttons:

- New Order: [Create a direct sales order] that is not linked to any table. Take the order, click
  Set Table to assign it to an existing table, or click Set Tab to
  record the open order’s name.
- Buttons for navigating between [configured floors]
  (e.g., Main Floor/Patio).
- (Table Selector): Enter an existing table number and click
  Jump to access it.

> **Note:**
>
> - Selecting a table on the Floor plan view or accessing it through the
>   Table Selector automatically confirms the table’s occupancy.
> - To order free physical QR codes adapted to the floor plan, activate the [QR menu](extra/self_order.html) setting, then click  Get QR Codes in the
>   Floor plan view. This [offer](https://www.odoo.com/app/point-of-sale-restaurant-qr-code)
>   is available worldwide and for all subscription types.

> **Tip:**
> ![example of a floor plan view with visual keys to understand it.](../../../_images/plan-understand.png)
>
> - Table 101: The table is currently available but booked for 15:00.
> - Table 102: The table is booked, and an order is sent to the kitchen.
> - Table 103: The 12:00 table is running late.
> - Table 104: The table has a pending order.
> - Table 105: The table is available.

### Configuration

Creating floors and tables allows for managing table selection and [orders].

#### From the POS backend

To create floors and tables from the backend, go to Point of Sale ‣ Configuration
‣ Floor Plans, and click New. Follow the next steps to configure the Floor
plan:

1. Enter a Floor Name.
2. Select the related Point of Sales.
3. Optionally, hover the mouse over the placeholder image and click the
   (Edit) icon to add a background image to the restaurant layout.
4. Click Add a line to create and configure a table:

   - Enter a Table Number.
   - Fill in the number of Seats.
   - Set the table’s Shape.
5. Optionally, activate additional settings by clicking the
   (settings) icon:

   - Adjust the Height, Width, and Color.
   - Tick the Active checkbox to make a table available or not.
6. Save.

> **Note:**
>
> - Enable the [Booking] setting to assign an
>   Appointment resource and make a table bookable.
> - Click the  (trash) icon to delete a table.

> **Note:**
>
> To create a Floor plan quickly, go to the Point of Sale section of the
> [POS settings](use.html#pos-use-settings). Under Floors & Tables Map, type the floor
> name in the Floors field, and press `Enter`.

#### From the POS frontend

To create floors and tables from the frontend, [open the POS register](use.html#pos-use-open-register),
click the  (hamburger menu) icon in the top right corner of the
Floor plan view, then Edit Plan. To configure the Floor plan,
follow the next steps:

1. Click the  (Add Floor) icon to add a floor.
2. Enter a Floor name and click Apply.
3. Click the  (Change Floor Background) icon to select a
   background color, or click  File to upload an image.
4. Optionally, click the  (Rename) icon to rename the
   Floor plan, the  (Clone) icon to create a copy, or
   the  (Delete) icon to delete it.
5. Click  Table to add a new table. To edit a table, select it
   and click one of the following icons:

   > - (Seats): Add or change the number of seats.
   > - (Square) or  (Round): Change
   >   the table’s shape.
   > - (Change Floor Background): Change the table’s color.
   > - (Rename): Change the table number.
   > - (Clone): Clone the table’s attributes using the following table
   >   number.
   > - (Delete): Remove the table.
6. Click Save.

> **Warning:**
>
> Removing a table or a floor is permanent.

### Booking

The Booking setting allows for creating and managing reservations for a designated
point of sale directly from the POS interface.

> **Note:**
>
> Enabling the Booking setting automatically installs the [Appointments](../../productivity/appointments.html) app.

#### Booking configuration

To enable and configure the bookings, follow these steps:

1. Go to the [POS settings](use.html#pos-use-settings), scroll down to the PoS Interface
   section, and enable Booking.
2. Enter a name in the Appointment type field and click Create and edit.
3. Configure the [Appointment type](../../productivity/appointments.html#appointments-configure) form and click Save.
4. Click Save in the POS settings.

> **Warning:**
>
> To ensure that only existing resources can be booked for a specific point of sale, set the
> Book field to Resources in the Appointment type form and
> select tables. Then, enable Manage Capacities to define the maximum amount each
> resource can handle.

> **Note:**
>
> To accommodate a booking that exceeds the capacity of a single table, click the
>  (Resources) icon in the Appointment Type form, select
> a table, and add additional tables in the Linked Resource field to merge them.

> **Note:**
>
> [Appointments](../../productivity/appointments.html)

#### Booking management

To manage table bookings from the POS interface, click Booking, then:

- Click New to create a booking. Add a name, the date and time, number of guests, phone
  number, duration, and [resources](../../productivity/appointments.html#appointments-resources), then click Save.
- Click a booking to Edit or Delete it. Click a stage name (e.g.,
  Booked, Checked-In, or No Show) or drag the booking card to
  move it to the relevant stage.

> **Note:**
>
> To quickly edit a booking from the [Floor plan] view, click the
> booking notification on the booked table.

## Order management

The POS register allows for [processing] and [transferring] orders, defining [presets],
and managing [courses].

### Order process

To process an order from the POS register, follow these steps:

1. Click products to add them to the cart.
2. Define how the order is handled:

   - Click Set Table to link the order to a table. Enter a table number and click
     Assign.
   - Click Set Tab to enter the open order’s name and click Apply.
3. Click Order to validate the order.

When ready, [process the order payment].

> **Note:**
>
> Clicking Order redirects to the [Floor plan] view if
> Tables is selected as the [default start screen].

> **Note:**
>
> - To cancel an order, click the  (Actions) icon, then
>   Cancel Order. If an [order printer is configured], a cancellation ticket is automatically printed for an
>   order sent to the kitchen.
> - After selecting a table in the [Floor plan] view, click
>   Release table in the cart to cancel the table’s occupancy. This action is
>   available when the cart is empty.
> - [Configure a printer] to send an order to the kitchen
>   printer when clicking Order.

### Order transfer

To transfer an order to another table from the [POS register], click
the  (Actions) icon, then Transfer/Merge, and choose
the target table in the [Floor plan] view:

> - Select an available table to transfer customers and their orders.
> - Select an occupied table to merge customers and their orders.

### Presets

Presets are used to apply preconfigured settings to orders and determine whether an order is for
Dine In, Takeout, or Delivery. They also control whether
customer contact information is required and apply capacity limits based on opening hours and order
quantity.

To use preconfigured presets, go to the [POS settings](use.html#pos-use-settings) and enable the
Take out / Delivery / Members setting under the Point of Sale section. Set
the Default field to the preferred preset, then save. From the [register], select the relevant preset, and [process the order]:

- Dine In: Assign a [table or open a tab].
- Takeout: Enter the order’s name and click Apply, then select a date
  and a time slot.
- Delivery: Select an existing customer, or click Create to add one. Then,
  select a time slot.

> **Note:**
>
> Click the preset button to switch to another one.

> **Note:**
>
> - [Preparation display](extra/preparation.html)
> - [Online food delivery](restaurant/online_food_delivery.html)

### Courses

The Course button allows for splitting orders into multiple courses, sending each course
to the kitchen sequentially.

To split an order into courses from the [register], click
Course and add products. Repeat the action as many times as needed, then click
Order to send the order to the kitchen, which also fires the first course.

When ready for the second course, retrieve the order from the [Floor plan] view or the Orders overview, and click Fire Course
2. Repeat the action as many times as needed.

> **Note:**
>
> - Alternatively, click Course as often as needed to display the desired number of
>   courses in the cart. Then, click each course, add products, and click Order.
> - To transfer a product or an entire course into another course, select it in the cart, click
>   the  (Actions) icon, then
>   Transfer course, and select the preferred course.

## Order printing

To enable sending orders to a kitchen or a bar printer, [connect a printer](hardware_network/receipt_printers.html) to Odoo, go to the [POS settings](use.html#pos-use-settings), and
follow these steps:

1. Scroll down to the Preparation section and enable the Preparation
   Printers setting.
2. Type the printer’s name in the Printers field and click Create and edit.
3. On the printer setup form, select the Printer Type:

   - If the printer is connected to an [IoT system](../../general/iot.html), select
     Use a printer connected to the IoT, and choose the relevant [device](../../general/iot/devices/printer.html). This process requires the IoT app and an IoT
     system.
   - If using an [Epson printer that does not require an IoT system connection](hardware_network/receipt_printers.html), select Use an Epson printer and enter the
     Epson Printer IP Address.
4. Define the product categories to be printed by clicking Add a line in the
   Printed Product Categories field and selecting the preferred category from the
   popover.
5. Click Save.
6. In the [POS settings](use.html#pos-use-settings), click Save.

The printer is then connected to the point of sale and can print kitchen orders and order receipts.

> **Note:**
>
> - Printing kitchen orders requires assigning a PoS Product Category.
> - To create a Printed Product Category on the Add: Printed Product
>   Categories popover, click New. Enter a name, select a Parent Category,
>   choose a Color, click the  (Edit) icon to add an
>   image, determine the product availability, then click Save & Close.

> **Note:**
>
> - To access all preparation printers from the [POS settings](use.html#pos-use-settings), scroll down
>   to the Preparation section and click  Printers.
>   Alternatively, go to Point of Sale ‣ Orders ‣ Preparations Printers.
> - After [processing an order], click the
>   (order) icon in the [POS register] next to
>   Payment to reprint a duplicate of the last kitchen order.

> **Note:**
>
> - [Connect an IoT system to a POS](hardware_network/pos_iot.html)
> - [Connect a printer](../../general/iot/devices/printer.html)
> - [IoT system connection to Odoo](../../general/iot/connect.html)
> - [Preparation display](extra/preparation.html)

## Bills and payment

### Bill splitting

To allow bill splitting, go to Point of Sale ‣ Configuration ‣ Settings, and
enable Allow Bill Splitting under the Point of Sale section.

To split a bill from the [POS register], follow these steps:

1. Click the  (Actions) icon, then Split.
2. Select at least one product and perform one of the following actions:

   - Payment: Process the direct payment for the selected product(s).
   - Split Order: Create a sub-order.
   - Transfer: Transfer one or all products to another table.
3. Process the [payment].
4. Click  Continue and repeat the process for each guest.

> **Note:**
>
> Splitting a bill requires ordering at least two products and creates a sub-order, which must
> be paid before returning to the main order.

### Order payment

To proceed with the order payment from the [POS register], follow
these steps:

1. Click Payment.
2. Select a [payment method](payment_methods.html).
3. Optionally, select a customer and send an invoice to them:

   - Click  Customer to select or create a customer account.
   - Enable  Invoice to allow sending an invoice to the
     customer.
4. Click Validate.

### Receipt printing

To allow receipt printing, go to Point of Sale ‣ Configuration ‣ Settings, and
enable Early Receipt Printing under the Point of Sale section.

After a successful [order payment], click
Print Full Receipt to generate and print a bill.

> **Warning:**
>
> If a printer is [configured and linked](hardware_network/receipt_printers.html) to a point of sale,
> the receipt is automatically printed upon payment confirmation.

> **Note:**
>
> [Invoices](use/pos_invoices.html)

## Tips

### Configuration

To allow tipping in a POS, go to the [POS settings](use.html#pos-use-settings), scroll down to the
Payment section, enable Tips, and click Save.

> **Warning:**
>
> - The Add tip after payment setting only works for a POS in the United States
>   of America with an [Adyen](payment_methods/terminals/adyen.html) or a [Stripe](payment_methods/terminals/stripe.html) [payment terminal](payment_methods/terminals.html#pos-terminals-configuration).
> - The Add tip through payment terminal (Adyen) setting only works with an
>   [Adyen](payment_methods/terminals/adyen.html#adyen-tips) terminal.

> **Note:**
>
> - Saving the Tips setting automatically fills the Tip product field
>   with the preconfigured [TIPS] Tips product, which is only used for tips. When
>   selecting another product in the Tip product field, the chosen product is no
>   longer available on the [POS register].
> - Choose only one tip product per POS.

### Tip and payment

To process a tip during [payment], follow these steps:

1. Click  Tip, add the amount, then click Ok.
2. Select a [payment method](payment_methods.html) for the order and the tip.
3. Click Validate.

> **Note:**
>
> If the order and the tip are paid using different payment methods, select a [payment method](payment_methods.html) for the order first. Then, select a payment method for the tip, click
>  Tip, add the tip amount, and click Ok.
> Finally, Validate the payment.

### Tip after payment (US only)

To allow tipping after payment for a POS in the United States of America, ensure the Add
tip after payment setting is enabled in the [POS settings](use.html#pos-use-settings). To process tips
after payment, follow these steps:

1. On the Payment screen, select a Card payment method linked to a
   [Stripe](payment_methods/terminals/stripe.html) or [Adyen](payment_methods/terminals/adyen.html) terminal.
2. Click Close Tab and select the relevant option in the Add a tip screen:

   - 15%, 20%, or 25%: Tip rates based on order total.
   - No Tip.
   - Tip Amount: Enter the relevant amount in the field.
3. Click Settle to validate.

---

# Online food delivery

**UrbanPiper** is an order management system that integrates with multiple food delivery platforms.
It consolidates orders from all connected platforms into a single interface, simplifying the
delivery process.

Supported providers:

- [Careem](https://www.careem.com)
- [Cari](https://getcari.com/)
- [ChowNow](https://www.chownow.com)
- [Deliveroo](https://deliveroo.co.uk/)
- [DoorDash](https://www.doordash.com)
- [EatEasy](https://www.eateasy.ae/dubai)
- [Glovo](https://glovoapp.com)
- [Grubhub](https://www.grubhub.com)
- [HungryPanda](https://www.hungrypanda.co)
- [HungerStation](https://hungerstation.com)
- [Jahez](https://www.jahez.net/)
- [Just Eat](https://www.just-eat.ie/)
- [Keeta](https://www.keeta-global.com/SA/en)
- [Mrsool](https://mrsool.co)
- [Ninja](https://ananinja.com/)
- [NoonFood](https://www.noon.com)
- [Postmates](https://www.postmates.com)
- [Rafeeq](https://www.gorafeeq.com/en)
- [Rappi](https://about.rappi.com/)
- [SkipTheDishes](https://www.skipthedishes.com/)
- [Swiggy](https://www.swiggy.com)
- [Talabat](https://www.talabat.com)
- [UberEats](https://www.ubereats.com)
- [Wolt](https://wolt.com/)
- [Zomato](https://www.zomato.com)

## Configuration

### Prerequisites

To use the UrbanPiper integration in a live production environment, ensure the following
requirements are satisfied:

- **UrbanPiper subscription:** A valid UrbanPiper subscription is mandatory.

  > **Note:**
  >
  > For any concerns or queries regarding your UrbanPiper subscription, please reach out to the
  > account manager linked to your Odoo database.
- **Odoo requirements:**

  - **Odoo subscription:** An active Odoo Enterprise subscription is required. Odoo Community does
    not support this integration.
  - **Odoo version:** Odoo Enterprise version 18.0 or above.
  - **Odoo platform:** All Odoo platforms are supported, including Odoo Online, Odoo.sh, and
    On-Premise installations.
- **Delivery platform reseller account:** A registered reseller account is required with each
  delivery platform to be integrated (e.g., Uber Eats, DoorDash, Careem, Deliveroo, Zomato).

### UrbanPiper credentials

1. Get your Atlas credentials:

   1. Go to the [POS settings](../use.html#pos-use-settings).
   2. Scroll down to the Food Delivery Connector section.
   3. Click Fill this form to get Username & Api key and fill out the survey.
2. [Go to your Atlas account](https://atlas.urbanpiper.com) and retrieve your API key and username
   by navigating to Settings ‣ API Access.

![Atlas API access](../../../../_images/urban-piper-api.png)

### Point of Sale

1. Enable the Urban Piper setting:

   1. Go to the [POS settings](../use.html#pos-use-settings).
   2. Scroll down to the Food Delivery Connector section.
   3. Check the Urban Piper setting.
2. Set up UrbanPiper:

   1. Fill in the Username and Api Key fields with your [UrbanPiper
      credentials].
   2. Select the desired delivery providers in the Food Delivery Platforms field under
      the Urban Piper Location section (i.e., Zomato, Uber Eats).
3. Save the settings.
4. Click the + Create Store button. Doing so creates a new location on the UrbanPiper
   Atlas platform.

> **Note:**
>
> - The Pricelist and Fiscal Position fields are automatically selected
>   after saving.
> - A successful store creation triggers a notification.
> - The store creation process may take 2–3 minutes to reflect changes on the UrbanPiper Atlas
>   platform.
> - The store is automatically named after your point of sale name.

![Food delivery connector settings](../../../../_images/create-store.png)

### Store timings

Configure the store timings to define when the delivery services are available:

1. Navigate to Point of Sale ‣ Configuration ‣ Store Timings.
2. Add a new timing record by clicking New to add a line, or edit an existing line.
3. Fill in the Week Day, Starting Hour, Ending Hour,
   and Point of Sale associated with this timing columns.

### Products

To make products available individually,

1. Go to Point of Sale ‣ Products ‣ Products.
2. Select any product to open its product form.
3. Go to the Point of Sale tab.
4. Complete the Urban Piper section:

   - Fill in the Available on Food Delivery with the desired POS.
   - Optionally, set up the Meal Type field and enable the Is Recommended
     and Is Alcoholic buttons.

![where to make a single product available for delivery](../../../../_images/product-form.png)

To make multiple products available for food delivery at once,

1. Go to Point of Sale ‣ Products ‣ Products.
2. Click the list icon () to switch to the list view.
3. Select the products.
4. Enter the desired POS in the Available on Food Delivery column.

![Product list](../../../../_images/product-list.png)
> **Note:**
>
> - Currently, UrbanPiper does not support combo products.
> - As a workaround, create a product and define combo choices as [Attributes & Variants](../../sales/products_prices/products/variants.html).

### Synchronization

To make products available on food delivery platforms, synchronize with your UrbanPiper account:

1. Go to the [POS settings](../use.html#pos-use-settings).
2. Scroll down the Food Delivery Connector section.
3. Click the Sync Menu button.

   - The Last Sync on timestamp below the Create Store and Sync
     Menu buttons updates.

> **Note:**
>
> - A successful synchronization triggers a notification.
> - The synchronization process may take 2–3 minutes to reflect changes on the UrbanPiper Atlas
>   platform.

### Go live

1. [Go to the Locations tab](https://atlas.urbanpiper.com/locations) of your Atlas account.
2. Select the location to activate, then click Request to go Live.

   ![Request to go live button in the locations tab of the Atlas account](../../../../_images/go-live.png)
3. In the popup window:

   1. Select the platform(s) to activate and click Next.
   2. Enter the Platform ID and Platform URL in the corresponding fields to
      establish the connection between the platform and UrbanPiper.
   3. Click the Request to Go Live button.![Go live parameters](../../../../_images/go-live-parameters.png)
   > **Note:**
   >
   > To find the location’s Platform ID and Platform URL,
   >
   > 1. Click the location to open its setup form.
   > 2. The location’s parameters are available in the HUB tab.
4. Verify that your location is live:

   1. [Go to the Locations tab](https://atlas.urbanpiper.com/locations) of your Atlas account.
   2. Select any provider in the Assoc. platform(s) column to review the status of that
      platform for this location.

## Order flow

An order placed via the configured delivery platform triggers a notification. To manage these
orders, open the orders’ list view by:

1. Clicking Review Orders on the notification popup.
2. Clicking the bag-shaped icon for online orders and New.

   ![Cart button](../../../../_images/cart-button.png)
   > **Note:**
   > - Clicking this icon displays the number of orders at each stage: New,
   >   Ongoing, and Done.
   > - The New button indicates newly placed orders, Ongoing is for
   >   accepted orders, and Done is for orders ready to be delivered.

Then,

1. Select the desired order.
2. Click the Accept button.
3. When an order is accepted, its Order Status switches from Placed to
   Acknowledged and is automatically displayed on the preparation display.

When the order is ready,

1. Open the orders’ list view.
2. Select the order.
3. Click the Mark as ready button. Its Order Status switches from
   Acknowledged to Food Ready, and its Status switches from
   Ongoing to Paid.

### Order rejection

Sometimes, the shop or restaurant may want to **reject** an order. In this case, open the orders’
list view,

1. Select the desired order.
2. Click the Reject button.
3. Select one of the reasons from the popup window.

![Reject order pop-up](../../../../_images/reject-order.png)
> **Warning:**
>
> **Swiggy** orders cannot be directly rejected. Attempting to reject one prompts Swiggy customer
> support to contact the restaurant. Similarly, **Deliveroo**, **JustEat**, and **HungerStation**
> do not allow order rejection. Always follow the respective provider’s guidelines for handling
> such cases.

---

# Extra features

---

# Multi-employee management

Odoo Point of Sale (POS) offers a **Log in with Employees** feature, allowing multiple users to
[log into the POS register]. Activating this feature enables the
following actions:

- Select specific users who can [log into the POS].
- [Assign minimal, basic or advanced permissions] to these
  users.
- [Track the employees involved in each order for enhanced analytics](../reporting.html#pos-analytics).

## Configuration

Access the multi-employee setting from the PoS Interface section of the [POS
settings](../use.html#pos-use-settings). Then,

1. Activate the Log in with Employees feature.
2. Add the employees with **basic POS functionality** access in the Basic rights field.
3. Add the employees with **extended POS functionalities** in the Advanced rights field.
4. Add the employees with **minimal POS functionality** access in the Minimal rights
   field.

![setting to enable multiple cashiers in POS](../../../../_images/activate-setting.png)
> **Note:**
>
> - Leaving the Minimal rights and Basic rights field empty allows all
>   employees to log in.
> - Leaving the Advanced rights field empty grants extended rights to Odoo users only.

> **Note:**
>
> Click the  (vertical ellipsis) button on the top right corner of
> a POS card and Edit to access the setting from the main POS dashboard.

> **Note:**
>
> [Access rights](../../../general/users/access_rights.html)

Minimal rightsBasic rightsAdvanced rights

Employees with minimal rights can perform the following actions within the POS:

**Register management:**

- Lock and unlock an open POS register.
- Reload data.

**Sales transactions:**

- [Process standard sales transactions](../use.html#pos-use-sell).
- [Set customers](../use.html#pos-use-customers).
- [Add notes to orders](../use.html#pos-use-notes).

**Pricing and discounts:**

- [Enter promotional codes](pricing.html#pos-pricing-loyalty-codes).

In addition to the minimal rights, employees with basic rights can also:

**Register management:**

- [Open the POS register](../use.html#pos-use-open-register).
- [Perform cash-in and cash-out operations](../use.html#pos-use-cash-register).

**Sales transactions:**

- [Create customers](../use.html#pos-use-customers).
- [Process refunds](../use.html#pos-use-refund).
- [Settle sales orders](../shop.html#pos-shop-so) from the POS interface.
- [Access past and current order history](../use.html#pos-use-orders).
- Cancel orders.

**Pricing and discounts:**

- Manually select another [pricelist](pricing.html#pos-pricing-pricelists).
- [Manually apply discounts](pricing.html#pos-pricing-discounts).
- Manually [change a product’s price](../use.html#pos-use-sell).
- [Give loyalty program’s rewards](pricing.html#pos-pricing-loyalty).
- Switch between [fiscal positions](pricing.html#pos-pricing-taxes).

In addition to the minimal and basic rights, employees with advanced rights can also:

- [Create products](../products.html).
- Access the Odoo backend interface.
- [Close the current POS register](../use.html#pos-use-register-close).

> **Note:**
>
> An employee with advanced POS rights who is not a database user cannot access the backend
> or create products.

## Usage guidelines

### Logging in

Once the **Log in with Employees** feature is enabled, employees must log in to [open the POS
register](../use.html#pos-use-open-register) and access the POS interface. They can [scan their employee
badge], click the  icon (users) to select
their name from the list of authorized users, or by entering [their PIN code] in the Enter your PIN field.

![Login window to open the register when the multiple cashiers feature is active](../../../../_images/log-in.png)

To switch between users from the [POS interface](../use.html#pos-use-open-register), click on the
currently logged-in employee’s name at the top right of the POS screen and select the user to
switch to.

> **Note:**
>
> In the absence of a scanner, click the  icon (barcode) to scan
> barcodes using the webcam.

### Logging in with badges

Employees can log in using their badge. To configure badge-based login, assign a unique badge ID to
the employee’s profile in the **Employees** module:

1. Navigate to the **Employees** module.
2. Open the form view of the specific employee.
3. Go to the Settings tab.
4. The Attendance/Point of Sale/Manufacturing category offers two options:

   - Manually enter any badge ID in the Badge ID field.
   - Click Generate to create a unique badge ID automatically.
5. Click Print Badge to generate a barcode representation of the assigned badge ID.

To switch between users from the [POS interface](../use.html#pos-use-open-register), using a badge, you
must first lock the register. To do so, click the  icon (lock) to
return to the login screen. Then, the new employee can scan their badge to log in.

### Adding a PIN Code

For enhanced security, employees may be forced to enter a PIN code each time they log into the POS
register. To set up a PIN code for an employee:

1. Navigate to the **Employees** module.
2. Open the form view of the relevant employee.
3. Go to the Settings tab.
4. Enter a desired numerical code in the PIN Code field of the
   Attendance/Point of Sale/Manufacturing category.

> **Note:**
>
> The PIN code must consist of a sequence of digits only.

---

# Preparation display

The preparation display feature allows you to handle POS orders requiring preparation. Concretely,

- **For retail**: The preparation team is notified after a payment is completed at the POS to
  gather the purchased items for customer pickup.
- **For restaurants**: POS orders inform the kitchen of the meals to be prepared.

## Configuration

To enable the preparation display feature,

1. Go to the [POS settings](../use.html#pos-use-settings).
2. Scroll down to the Preparation section.
3. Check the Preparation Display option.

![Setting to enable the preparation display feature](../../../../_images/preparation-setting.png)

To create and set up a preparation display,

1. Go to Point of Sale ‣ Orders ‣ Preparation Display
2. Click New.
3. Give the display a descriptive Name (e.g., `Main Kitchen`, `Bar`)
4. Set it up:

   1. Point of Sale: Select the POS that sends orders to this display.
   2. Product categories: Specify the POS Product categories sent to this
      display.
   3. Stages: Define the steps required for the orders to be ready.

      - Click Add a line to add a stage.
      - Assign specific colors to each stage for clarity (optional).
      - Define an Alert timer (min) for each stage to indicate the expected processing
        time.

![preparation display set-up form](../../../../_images/display-form.png)
> **Note:**
>
> To edit a pre-existing preparation display, click the vertical ellipsis button
> () on the display’s card and select Configure.

## Practical application

Go to Point of Sale ‣ Orders ‣ Preparation Display to get an overview of all
your displays.

![Kanban view of the preparation display](../../../../_images/display-card.png)

The display card shows:

- The configured stages.
- The number of orders currently In progress.
- The Average time employees usually take to complete an order.

> **Note:**
>
> Click the Kitchen Display app icon on your Odoo Dashboard for quicker access.

### Using the preparation display

To access the preparation display, click Preparation Screen. This interface, designed
for employees, shows:

- **Stages and order count**: Displays the progress of orders across stages such as `To prepare`,
  `Ready`, and `Completed`, along with the number of orders in each stage.
- **Ordered products by category**: Lists all items in progress, grouped by POS categories (e.g.,
  `Drinks`, `Food`).
- **Order cards**: Summarizes individual orders, including:

  - Associated tables and order numbers.
  - Status, such as `Ready`, highlighted with the defined colors.
  - Waiting time, with visual indicators.

> **Note:**
>
> The duration indicator turns red if the elapsed time exceeds the predefined alert time.

![the preparation display interface with orders to process.](../../../../_images/preparation-display.png)

To update order progress:

- Click items on the order card to cross them off individually.
- Click the order card itself to mark all items at once.
- The card automatically moves to the next stage once every item is crossed off.
- Click  Recall to move an order back to the previous stage if you
  mistakenly sent it to the next stage.

### Customer display

In parallel, click Order Status Screen to open the customer interface. This interface,
designed for customers, provides an overview of orders that are:

- Ready for pickup.
- Almost there, indicating they are taken care of.

> **Note:**
>
> The order number can be found at the top of the customer’s receipt.

---

# Self-ordering

The self-ordering feature allows customers to browse your menu or product catalog, place an order,
and complete payment using their mobile device or a self-ordering kiosk.

## Configuration

### Feature activation

To enable this feature and select a self-ordering type, access the [POS settings](../use.html#pos-use-settings), scroll down to the Mobile self-order & Kiosk section, and select a
Self Ordering type under the QR menu & Kiosk activation section.

You can choose from:

QR menuKiosk

Select QR menu or QR menu + Ordering to give customers access to your
menu or product catalog by scanning a QR code on their personal device. The latter also
allows them to place an order and make a payment.

![QR menu and kiosk setting activation](../../../../_images/qr-activation.png)

- Click  Print QR Codes to download a .pdf document with the
  generated QR codes.
- Click  Download QR Codes to download a compressed file
  with the generated QR codes.

> **Note:**
>
> In [restaurants](../restaurant.html#pos-restaurant-floors), printing or downloading QR codes generates
> as many QR codes as the number of available tables. In **shops**, it generates only one
> generic QR code.

> **Note:**
>
> To customize QR codes,
>
> 1. Scan the relevant QR code to acquire its URL.
> 2. Use a QR code generator (e.g., [QR code monkey](https://www.qrcode-monkey.com) or [QR
>    code generator](https://www.qr-code-generator.com)) to create a custom QR code.

When Kiosk is selected, customers can access the menu or product catalog, place
orders, and pay from a self-ordering kiosk.

![QR menu and kiosk setting activation](../../../../_images/kiosk-activation.png)

Once a self-ordering type is selected, the [additional settings]
update to fit the selected type’s needs.

### Additional settings

Home buttonsService location and payment optionsLanguageSplash screensEat in/ Take outLaunch on IoT Box

The Home buttons are displayed on the kiosk or mobile device interfaces when
customers are self-ordering. To set them up, click  Home
buttons. Then,

1. Click New to add a new button.
2. Set the Label.
3. Enter a URL preceded by `https://` to redirect customers to a specific URL when
   clicking the button. For instance, you might want to redirect them to a campaign video for
   a new product or to a contest page.
4. In the same URL column, enter `/products` to create a button that redirects
   customers to the product catalog.
5. Select the Points of Sale to ensure this button only appears on the selected
   POS’ self-ordering interface.
6. Select a predefined Style from the dropdown menu.

> **Note:**
>
> - Leaving the Points of Sale field empty shares the button with all POS.
> - The Preview column automatically updates, giving you a glimpse of the
>   button’s appearance based on its configuration.

- Set where the service occurs by selecting Table or Pickup zone
  under the Service field.
- Define when and how customers pay in the Pay after field. Customers can pay
  after Each meal or for Each order.
- The service location and payment options available depend on the type of self-ordering
  service and POS:

  - **QR menu + Ordering**:

    - **Restaurants**: Customers can be served at their table or the pickup zone.

      - When served at their table, they can pay after each meal or each order.
      - When served at the pickup zone, they can only pay after each order.
    - **Shops**: Customers can only be served at the pickup zone and pay after each order.
    - Regardless of the type of POS, customers can pay [online](../../../finance/payment_providers.html) or using any configured [payment
      method](../payment_methods.html).
  - **Kiosk**:

    - Regardless of the type of POS, customers can either be served at their table or in the
      pickup zone, but they must pay after each order.
    - The kiosk self-ordering only works with [Adyen](../payment_methods/terminals/adyen.html)
      and [Stripe](../payment_methods/terminals/stripe.html) terminals.
    - The Online Payment feature is not supported.

> **Note:**
>
> - [Online payments](../../../finance/payment_providers.html)
> - [Payment methods](../payment_methods.html)

This option allows you to enable multiple languages for the self-ordering interface. The
suggested languages are those already installed in Odoo. To expand the selection, add more
languages:

1. Click  Add Languages.
2. Add as many languages as needed to the Languages field.
3. Click Add.
4. Add those languages to the Available field.

> **Note:**
>
> [Change languages](../../../general/users/language.html)

Splash screens are introductory screens displayed when the self-ordering interface or kiosk is
launched. They typically contain branding, welcome messages, or usage instructions.

- To add a splash screen image, click  Add images, select and
  open an image.
- To remove a splash screen image, hover over the image and click
  (Delete).

> **Note:**
>
> You can add multiple splash screen images at once.

Activate this setting to [adjust the tax rate](pricing.html#pos-pricing-taxes) based on whether
customers dine in or take their order to go. Then,

- Fill in the field with an existing Alternative Fiscal Position;
- Create and set up a new fiscal position by filling in the field and clicking
  Create & Edit; or
- Create and set up a new fiscal position by clicking  Fiscal
  Positions.

> **Note:**
>
> - [Flexible taxes (fiscal positions)](pricing.html#pos-pricing-taxes)
> - [Fiscal positions (tax and account mapping)](../../../finance/accounting/taxes/fiscal_positions.html)

This option allows for using an [IoT Box](../../../general/iot/iot_box.html) connected to a
touchscreen as a self-ordering kiosk.

1. [Connect an IoT Box](../../../general/iot/connect.html) to your Odoo database.
2. Ensure a touchscreen [display](../../../general/iot/devices/screen.html) is connected
3. Select the IoT Box from the Launch on field.

> **Note:**
>
> Once connected to the IoT box, the touchscreen display appears as two separate
> devices in the IoT box’s list of devices: a display and a keyboard input device.

### Preview

Review the interface before making the self-ordering feature available to customers to ensure all
settings are applied correctly. Click  Preview Web interface
under the Self Ordering field to ensure all [additional settings] are correctly applied.

## Usage guidelines

QR menuKiosk

On the POS user’s end, access the self-ordering interface by

- Scanning a downloaded or printed QR code; or
- Clicking the  (vertical ellipsis) icon on the POS card,
  then Mobile Menu.

On the customers’ end,

1. Access the self-ordering interface by scanning a downloaded or printed QR code.
2. Click the [home button] to reach the menu or catalog.
3. Select the items and click Order to place an order.
4. Follow the instructions on-screen to assign a table and pay for the order.

On the POS user’s end, click Start Kiosk.

> **Note:**
>
> - If an IoT Box is configured as a kiosk, the self-ordering interface opens directly on
>   the connected touchscreen. Otherwise, it opens in a new browser tab on the device used
>   to access it.
> - Once the register is open, Start Kiosk switches to Open Kiosk on the
>   POS card.
> - Click Open Kiosk on the POS card to reopen the self-ordering interface in a new
>   tab or to refresh the kiosk’s IoT Box touchscreen display if it is already running.

On the customers’ end,

1. Click the [home button] from a self-ordering kiosk to
   reach the menu or product catalog.
2. Select the items and click Order to place an order.
3. Follow the instructions on-screen to assign a table and pay for the order.

![kiosk end-screen for customers](../../../../_images/kiosk-endscreen.png)

> **Warning:**
>
> - [The POS register must be open](../use.html#pos-use-open-register) for customers to place an order.
> - Once an order is placed, it is automatically sent to [the preparation screen](preparation.html) and added to the list of POS orders.

---

# Pricing features

## Discounts

Discounts allow users to reduce the price of item lines in POS orders. The discount can be applied
as a percentage of a product’s sale price or the total order amount.

To activate discounts, navigate to the [POS settings](../use.html#pos-use-settings), scroll down to the
Pricing section, and enable:

> - Global Discounts to allow users to set a discount on the entire order.
>   Modify the default discount percentage in the Discount % field if needed.
> - Line Discounts to allow users to set discounts on specific products in the cart.

> **Note:**
>
> [Discounts](../../sales/products_prices/prices/discounts.html)

### Global discounts

To apply a discount on the whole order from the [POS register](../use.html#pos-use-open-register), click
the  (vertical ellipsis) icon, then
Discount. Set the discount percentage and click Confirm.

### Line discounts

To set a discount on a specific product, select the product from the cart, click the %
cart modifier from the pad, then use the numpad to set the discount.

> **Note:**
>
> - Adding other products to the cart switches the cart modifier back to Qty
>   automatically.
> - To remove a discount, select the product from the cart, click %, then click
>   ⌫

## Discount and loyalty programs

Discount and loyalty programs provide flexible, customer-facing pricing strategies. Unlike
[pricelists](../../sales/products_prices/prices/pricing.html), which define structured
pricing rules, discount and loyalty programs are designed for promotional, time-sensitive, and
public offers, such as seasonal sales, limited-time deals, or customer rewards.

To activate discount and loyalty programs in Point of Sale, navigate to the [POS
settings](../use.html#pos-use-settings), scroll down to the Pricing section, and enable
Promotions, Coupons, Gift Card & Loyalty Program.

Once the feature has been activated, go to Point of Sale ‣ Products ‣
Discount & Loyalty and [configure the desired discount and loyalty programs](../../sales/products_prices/loyalty_discount.html#sales-products-loyalty-programs). These programs are triggered when an order meets the defined
requirements. Depending on the [program type](../../sales/products_prices/loyalty_discount.html#sales-pricing-management-program-types), rewards
are either applied automatically or manually by the cashier.

> **Note:**
>
> [Discount and loyalty programs](../../sales/products_prices/loyalty_discount.html)

### Codes

To apply a gift card, discount code, or coupon, click the  (vertical
ellipsis) icon, select  Enter Code, enter or scan the code, and
click Apply.

> **Note:**
>
> Coupon and next-order coupon codes are printed directly on customer receipts.

### Promotions

Promotions are fully automated. They are applied to the order as soon as all program conditions
(such as minimum spent or specific products) are met.

### Buy X get Y

When the order qualifies for a **Buy X get Y** deal, the reward must be added manually. Click the
 (vertical ellipsis) icon, select
Reward, and choose the desired item from the list.

### Loyalty cards

To track or spend loyalty points, you must first [select a customer](../use.html#pos-use-customers) in the POS register. Once selected, their Loyalty point(s) are
displayed at the bottom of the cart and updated in real-time.

To redeem points for a reward, click the  (vertical ellipsis) icon,
select  Reward, and choose the desired item from the list.

## Pricelists

Pricelists allow you to automate price adjustments based on specific criteria. They can be used to
set POS-specific prices, create temporary discount periods, reward loyal customers, or offer
bulk-buy discounts.

### Configuration

To enable pricelists in the Point of Sale app:

1. Navigate to Point of Sale ‣ Configuration ‣ Settings.
2. In the Pricing section, activate the Flexible Pricelists feature and
   Save.
3. Once the page reloads, click  Pricelists to [configure
   the pricelists](../../sales/products_prices/prices/pricing.html#sales-products-pricelist-configuration).
4. When configured, return to the [POS settings](../use.html#pos-use-settings) to add all relevant
   pricelists to the Available field, and select the one to be used as the
   Default.

### Assign pricelists

To manually assign a pricelist to an order from the [POS register](../use.html#pos-use-open-register),
click the  (vertical ellipsis) icon and the
icon, followed by the currently selected pricelist’s name. Then, click the new pricelist to apply.

> **Note:**
>
> You can also set a pricelist to be selected automatically for a specific [customer](../use.html#pos-use-customers). To do so, go to Point of Sale ‣ Orders ‣ Customers,
> select the relevant customer, and assign a pricelist in the Pricelist field of the
> Sales section in the Sales & Purchase tab.

> **Note:**
>
> - [Pricelists](../../sales/products_prices/prices/pricing.html)
> - [Pricelists in eCommerce](../../../websites/ecommerce/configuration/prices.html#ecommerce-prices-pricelists)

## Cash rounding

Cash rounding is used when the smallest physical currency denomination (the smallest
coin) is higher than the minimum unit of account.

For example, in countries that have phased out one-cent and two-cent coins, businesses must round
the total amount of a cash transaction to the nearest five cents. In Odoo, each point of sale can
be individually configured to apply these rounding rules to bills and receipts.

### Configuration

1. Go to Point of Sale ‣ Configuration ‣ Settings.
2. In the Payment section, enable Cash Rounding.
3. Enable Apply only on cash methods to deactivate rounding for [card
   payments](../payment_methods.html).
4. In the Rounding Method field, select an existing method or click Create
   to define a new one.

When creating a new rounding method, define the following:

- Rounding Precision: The value of the smallest coinage available (e.g., 0.05).
- Rounding Strategy: Choose how the adjustment is recorded:

  > - Modify tax amount: The rounding difference is applied in the taxes section.
  > - Add a rounding line: The rounding difference is added as a separate line on the
  >   receipt and the invoice.
- Profit Account and Loss Account: The accounts used to record the rounding
  discrepancies.
- Rounding Method: The tie-breaking rule used to determine the direction of the rounding
  (Up, Down, or Nearest).

> **Warning:**
>
> Odoo Point of Sale only supports the Add a rounding line rounding strategy.

> **Tip:**
>
> Example: Rounding a $19.92 total with a **rounding precision** of 0.05.
>
> The final total changes depending on the **rounding method** selected in the configuration:
>
> | Rounding method | Resulting total | Logic |
> | --- | --- | --- |
> | Up | $19.95 | Always rounds toward the higher value. |
> | Down | $19.90 | Always rounds toward the lower value. |
> | Nearest | $19.90 | Rounds to the nearest 0.05. |

> **Note:**
>
> Rounding only applies to the **Total** of the receipt, not to individual product prices.

## Flexible taxes (fiscal positions)

When running a business, you may need to apply different taxes and record transactions on various
accounts based on the location and type of business of your customers and providers.

Fiscal positions allow you to define rules that automatically select the appropriate taxes and
accounts used for each transaction.

> **Note:**
>
> - [Fiscal positions (tax and account mapping)](../../../finance/accounting/taxes/fiscal_positions.html)
> - [Taxes](../../../finance/accounting/taxes.html)

### Configuration

To use fiscal positions, go to Point of Sale ‣ Configuration ‣
Settings, scroll down to the Accounting section, and enable Flexible Taxes.

Then, configure the fiscal position for your POS:

- Set the default fiscal position to be automatically applied to all sales in the selected POS
  using the Default field.
- Select additional fiscal positions in the Allowed field to make them selectable during
  sales.

Depending on the installed [fiscal localization package](../../../finance/fiscal_localizations.html), several fiscal positions are already preconfigured
and ready to use in the POS. You can also [create new ones](../../../finance/accounting/taxes/fiscal_positions.html#fiscal-positions-configuration)
if needed.

> **Note:**
>
> - [A default fiscal position can also be assigned to a customer](../../../finance/accounting/taxes/fiscal_positions.html#accounting-fiscal-positions-partner).
> - If no fiscal position is configured, the tax defined in the product’s Sales Taxes
>   field is applied.

### Apply fiscal positions

To apply a fiscal position to a POS order in the [POS register](../use.html#pos-use-open-register),
click the  (vertical ellipsis) icon, click the
Tax button, and choose the desired fiscal position from the list.

---

# Payment methods

Configure a payment method with Odoo Point of Sale to provide customers with various payment
options, including cash, card payments through a [configured payment terminal](payment_methods/terminals.html#pos-terminals-configuration), [online payments](../../finance/payment_providers.html), or
[customer accounts](payment_methods/customer_credit.html).

To create a payment method, go to Point of Sale ‣ Configuration ‣ Payment
Methods, click New, and follow the next steps:

1. Enter a name for the payment method.
2. Enable the following options if needed:

   - Online Payment: To link the payment method to a [payment provider](../../finance/payment_providers.html) and enable online payments, select a provider in
     the Allowed Providers field or click  Payment
     Providers to install one.
   - Identify Customer: Force the selection of a customer during the payment.
3. Select the preferred [Journal](../../finance/accounting/get_started/journals.html) to record all
   transactions.
4. Select the appropriate Point of Sale to enable the payment method.
5. Set the Integration field to one of the following options:

   - None required: For cash payments.
   - Terminal: [Set up a terminal](payment_methods/terminals.html#pos-terminals-configuration) and allow card
     payments.
   - Bank App (QR Code): Add at least one [bank account](../../finance/accounting/get_started/journals.html#accounting-journals-bank) to the journal to enable [QR code payments](payment_methods/qr_code_payment.html) with a bank app. Select a QR Code Format in the
     form.
   - Cash Machine (Glory): Connect a [Glory](payment_methods/cash_machines/glory.html)
     [cash machine](payment_methods/cash_machines.html) to automate the point of sale’s cash
     transactions.
6. Save.

> **Note:**
>
> - The Delivery Payment option links a payment method to online orders placed through
>   [Urban Piper](restaurant/online_food_delivery.html). Select the appropriate
>   Delivery Provider to associate with the payment method.
> - If the Accounting app is installed, use the Intermediary Account field, if needed,
>   to record transactions for this payment method in a specific receivable account for
>   better traceability. Leave the field empty to use the company’s default [receivable
>   account](../../finance/accounting.html#accounting-accounts-receivable-payable). When a [journal](../../finance/accounting/get_started/journals.html#accounting-journals-bank) is selected, an [Outstanding Account](../../finance/accounting/get_started/journals.html#accounting-journals-outstanding-accounts) can also be set if required.

> **Note:**
>
> - Use a dedicated [cash journal](../../finance/accounting/get_started/journals.html#accounting-journals-cash) to record cash payments.
> - Always set the Journal to Bank when [configuring a payment
>   terminal](payment_methods/terminals.html#pos-terminals-configuration).

> **Note:**
>
> - [Payment methods (video tutorial)](https://www.youtube.com/watch?v=eHr4tS8Wmss)
> - [Payment terminals](payment_methods/terminals.html)
> - [Cash machines](payment_methods/cash_machines.html)

---

# Cash machines

Connecting and integrating a cash machine with a POS system automates cash transactions, cash
counting, and change return.

## Configuration

Configure the cash machine itself before setting it up in Odoo. Currently, Odoo supports [Glory](cash_machines/glory.html) cash machines. Once the cash machine is fully set up:

1. Create the associated [payment method](../payment_methods.html).
2. Select the POS in the Point of Sale field.

## Use

To process a [payment](../use.html#pos-use-sell) with a [configured cash machine], select the machine’s [payment method](../payment_methods.html)
on the **payment screen**, then follow the instructions on the machine.

Once the transaction is successful, the payment is automatically validated in Point of Sale.

> **Note:**
>
> - Connection issues between Odoo and the cash machine result in transaction cancellation.
> - To cancel the payment request, click Cancel.

---

# Customer account

The **Customer account** feature allows customers to use their account to make purchases. They can
deposit money for future purchases or select their account as a [payment method](../payment_methods.html) to purchase items on credit and [settle the debt later]
through a point-of-sale transaction or via an issued invoice.

## Configuration

To allow customers to pay using their customer account, [create a payment method](../payment_methods.html) and configure it as follows:

1. Enable Identify Customer to force the [selection of a customer](../use.html#pos-use-customers) to allow using this payment method.
2. Keep the Journal field blank to use the customer’s receivable account.
3. Select the points of sale where this payment method is available in the Point of Sale
   field.

> **Note:**
>
> Set a maximum sales credit to prevent customers from exceeding a defined credit limit. Once the
> maximum credit amount is reached, the selected customer button turns orange and a
>  (warning sign) icon appears next to the customer’s name as a
> warning. However, this warning does **not** prevent a sale from proceeding.

> **Note:**
>
> - [Payments](../../../finance/accounting/payments.html)
> - [Chart of accounts](../../../finance/accounting/get_started/chart_of_accounts.html)

## Payment process

### Deposit money

To deposit money to the customer account from the POS interface:

1. Click Customer and locate the desired customer in the list.
2. Click the  (hamburger menu) icon, then select Deposit
   money.
3. Choose the payment method.
4. When redirected to the payment screen, enter the amount to deposit using the keypad.
5. Validate the transaction.
6. Click Yes on the popup window to confirm.

### Customer account as payment method

To use the customer account as a payment method for a purchase from the POS payment screen:

1. Select the payment method [created for the customer account].
2. Click  Customer to open the customer list and select the customer.
3. Click the Invoice button.
4. Validate the purchase.

> **Warning:**
>
> To effectively monitor and manage the customer’s unpaid debt, either [create an invoice](../use/pos_invoices.html) for the order or install the [Accounting application](../../../finance/accounting.html).

## Debt tracking

When a customer pays using their customer account, the purchase amount is recorded as debt until it
is paid off. To keep track of a customer’s debt, consult their customer statement in the backend or
their customer profile from the POS register.

To access the Customer Statement report, go to Point of Sale ‣ Orders
‣ Customers, select a customer to open their form, and click the Customer Statements
smart button.

To view the total amount due or deposited by a customer from the POS register, access the customer
list by clicking Customer and search for the desired customer; the amount due or
deposited is displayed next to their name.

![customer list and summary of their customer accounts](../../../../_images/customer-list.png)
> **Note:**
>
> [Follow-up on invoices](../../../finance/accounting/payments/follow_up.html)

> **Note:**
>
> When a customer is related to a company, the customer statement report might be related to the
> company itself, and not the customer.

## Due amount settlement

To settle a customer’s due amount, [register the payment from the invoice](../../../finance/accounting/payments.html#accounting-payments-from-invoice-bill) or, from the POS interface, follow these steps:

1. Click Customer and search for the desired customer in the list.
2. Click the  (hamburger menu) icon next to the customer’s name.
3. Select Settle orders or Settle invoices.
4. Select the orders or invoices to settle.
5. Click Payment and select the relevant payment method.
6. Click Validate.
7. Click Yes on the popup window to confirm the deposit of the payment received from the
   customer.

---

# QR code payments

QR code payments allow users to generate a code that customers can scan with their mobile banking
app to initiate a bank transfer or pay instantly.

## Configuration

### Activate and set up QR code payments

Go to Accounting ‣ Configuration ‣ Settings, and

1. Activate or upgrade your country’s fiscal localization package under the Fiscal
   Localization section to access all country-specific accounting features.
2. Activate QR codes under the Customer Payments section.

Then, as the QR code type differs depending on your country, follow the corresponding documentation
page from the following table to set them up.

| QR code types | Module name | Technical name | Description |
| --- | --- | --- | --- |
| Pix | [Brazilian - Accounting](../../../finance/fiscal_localizations/brazil.html) | `l10n_br` | The base module to manage the accounting chart and localization for Brazil. |
| FPS | [Hong Kong - Accounting](../../../finance/fiscal_localizations/hong_kong.html) | `l10n_hk` | The base module to manage the accounting chart and localization for Hong Kong. |
| QRIS | [Indonesian - Accounting](../../../finance/fiscal_localizations/indonesia.html) | `l10n_id` | The base module to manage the accounting chart and localization for Indonesia. |
| PayNow | [Singapore - Accounting](../../../finance/fiscal_localizations/singapore.html) | `l10n_sg` | The base module to manage the accounting chart and localization for Singapore. |
| QR-bill | [Switzerland - Accounting](../../../finance/fiscal_localizations/switzerland.html) | `l10n_ch` | The base module to manage the accounting chart and localization for Switzerland. |
| PromptPay | [Thailand - Accounting](../../../finance/fiscal_localizations/thailand.html) | `l10n_th` | The base module to manage the accounting chart and localization for Thailand. |
| VietQR | [Vietnam - Accounting](../../../finance/fiscal_localizations/vietnam.html) | `l10n_vn` | The base module to manage the accounting chart and localization for Vietnam. |
| EPC | [Account SEPA QR Code](../../../finance/accounting/customer_invoices/epc_qr_code.html) | `account_qr_code_sepa` | This module adds support for SEPA Credit Transfer QR-code generation. |

### Create the payment method

1. Open the Point of Sale application.
2. Go to Configuration ‣ Payment Methods and create a payment method.
3. Set a bank-type journal.
4. Select Bank App (QR Code) under the Integration section.
5. Select the QR Code Format from the dropdown menu.

   - Select SEPA Credit Transfer QR if you are part of the Single Euro Payments Area
     (SEPA).
   - Select EMV Merchant-Presented QR-code for other QR code types.

![QR code payment method configuration](../../../../_images/qr-payment-methods-setting.png)
> **Warning:**
>
> At least one bank account must be defined in the journal to allow QR code payments to be
> registered with bank apps.

Once the payment method is created, go to the [POS’ settings](../use.html#pos-use-settings) and add the
payment method to your POS under the Payment section.

![Enable QR code payment method](../../../../_images/qr-configuration-setting.png)

## Register payments using QR codes

When processing a payment, select the payment method for QR code payments. A QR code is generated
and displayed on the screen for the customer to scan and pay with their mobile banking app.

![QR code payment example](../../../../_images/qr-payment-example.png)

Hit Confirm Payment to validate the transaction.

> **Warning:**
>
> Odoo does **not** check the bank payment. It is recommended that users verify payments for
> validity before confirming them on the POS register.

---

# Payment terminals

Connect and integrate a payment terminal to a [POS system](../use.html#pos-use-open-register) to accept
multiple payment options, including credit and debit cards.

## Configuration

To activate a payment terminal and allow processing payments with it, follow these steps:

1. Go to Point of Sale ‣ Configuration ‣ Settings and scroll down to the
   Payment Terminals section.
2. Enable the relevant terminal.
3. Click Save.
4. Go to Point of Sale ‣ Configuration ‣ Payment Methods and [create the
   corresponding payment method](../payment_methods.html).
5. Set the Integration field to Terminal, select the relevant terminal, and
   complete the terminal-specific configuration:

   - [Adyen](terminals/adyen.html)
   - [Dpopay](terminals/dpo.html)
   - [Ingenico](terminals/ingenico.html)
   - [Mercado Pago](terminals/mercado_pago.html)
   - [Pine Labs](terminals/pine_labs.html)
   - [QFPay](terminals/qfpay.html)
   - [Razorpay](terminals/razorpay.html)
   - [SIX](terminals/six.html)
   - [Stripe](terminals/stripe.html)
   - [Tyro](terminals/tyro.html)
   - [Viva.com](terminals/viva_com.html)
   - [Worldline](terminals/worldline.html)
6. Save.

## Terminal use

To process a [payment](../use.html#pos-use-sell) with a [configured terminal] for an order, select the terminal’s [payment method](../payment_methods.html) on the Payment screen, then follow the instructions on the
terminal device.

Once the transaction is successful, the payment is automatically validated in Point of Sale.

> **Note:**
>
> - Connection issues between Odoo and the payment terminal result in transaction cancellation.
> - To cancel the payment request, click Cancel.

---

# Reporting

## View statistics

To access your statistics, go to Point of Sale ‣ Reporting ‣ Orders. Or, from
the **POS dashboard**, click the vertical ellipsis (⋮) button, Reporting,
and Orders.

These statistics are available in a graph or pivot view that you can filter or group depending on
your needs.

## Analytics

Once you [close the POS register](use.html#pos-use-register-close), access the comprehensive
report to review all session activities, including who initiated the session (i.e., [opened
the register](use.html#pos-use-open-register)) and who handled specific orders. To access the report:

1. Click the  (vertical ellipsis) icon on the POS card.
2. Click Sessions under the View section.
3. From that list view, you can see all the sessions and who initiated them under the
   Opened By column.
4. Select a session to open a detailed session report.
5. Click the Orders smart button to display a list of all orders placed during that
   session.
6. From that view, you can retrieve the following information:

   - The Order Ref
   - The Date of the order.
   - The Point of Sale where that order was made.
   - The Receipt Number.
   - The Customer.
   - The Employee that placed this order.
   - The Total paid amount.
   - The order Status.

To get an overview of all orders for a specific POS, regardless of the session, click the
 (vertical ellipsis) button on the POS card and select
Orders from the View section.