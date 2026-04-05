# Inventory — Warehouses, Operations & Valuation

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

Inventory management: warehouses, routes, replenishment, operations types, putaway rules, valuation, and barcode scanning. Use when configuring stock movements, costing, or fulfilment workflows.

---

# Inventory

Odoo *Inventory* is both an inventory application and a warehouse management system. The app allows
users to easily manage lead times, automate replenishment, configure advanced routes, and more.

> **Note:**
>
> - [Odoo Tutorials: Inventory](https://www.odoo.com/slides/inventory-24)

---

# Product management

---

# Configure product

A group of products in Odoo can be further defined using:

- [Units of measure (UoM)](configure/uom.html): a standard quantity for specifying product amounts
  (e.g., meters, yards, kilograms). Enables automatic conversion between measurement systems in
  Odoo, such as centimeters to feet.

  - *Ex: Purchasing fabric measured in meters but receiving it in yards from a vendor.*
- [Packages](configure/package.html): A physical container used to group products together, regardless of
  whether they are the same or different.

  - *Ex: A box containing assorted items for delivery, or a storage box of two hundred buttons on a
    shelf.*
- [Packaging](configure/packaging.html): groups the *same* products together to receive or sell them in
  specified quantities.

  - *Ex: Cans of soda sold in packs of six, twelve, or twenty-four.*

## Comparison

This table provides a detailed comparison of units of measure, packages, and packaging to help
businesses evaluate which best suits their requirements.

| Feature | Unit of measure | Packages | Packaging |
| --- | --- | --- | --- |
| Purpose | Standardized measurement for product units (e.g., cm, lb, L) | Tracks the specific physical container and its contents | Groups a fixed number of items together for easier management (e.g., packs of 6, 12 or 24) |
| Product uniformity | Defined per product; saved as one UoM in the database | Allows mixed products | Same products only |
| Flexible | Converts between vendor/customer UoMs and database UoM | Items can be added or removed from the container | Quantities are fixed (e.g., always packs of 6, 12 or 24) |
| Complexity | Simplest for unit conversions | More complex due to container-level inventory tracking | Simpler; suitable for uniform product groupings |
| Inventory tracking | Tracks product quantities within the warehouse in the specific UoM defined in the product form | Tracks package location and contents within the warehouse | Tracks grouped quantities but not individual items’ locations |
| Smooth barcode operations | Not available | Requires scanning both the package and individual items for reception. (even if there are 30 items in a package). Can enable the [Move Entire Packages](configure/package.html#inventory-product-management-move-entire-pack) feature to update the package’s contained items’ locations, when moving the package | Scanning a packaging barcode automatically records all included units. (e.g. 1 pack = 12 units) |
| Product lookup | Not available | Scanning a product’s barcode identifies its typical storage location in the Odoo database | Barcode identifies grouped quantity, not storage location |
| Unique barcodes | Not available | Unique barcodes for individual packages (e.g. Pallet #12) | Barcodes set at the packaging type level (e.g. for a pack of 6) |
| Reusability | Not applicable | Can be disposable or reusable, configured via the [Package Use](configure/package.html#inventory-warehouses-storage-cluster-pack) field | Disposable only |
| Container weight | Not applicable | Weight of the container itself is included in the *Shipping Weight* field of a package (Inventory app ‣ Products ‣ Packages) | Weight of the container is defined in the *Package Type* settings |
| Lot/serial number tracking | Requires manual adjustments to track UoMs via lots (See [use case] for details) | Applies only to contained products | Applies to both contained products and the container |
| Custom routes | Cannot be set | Cannot be set | Routes can define specific warehouse paths for a particular packaging type |

## Use cases

After comparing the various features, consider how these businesses, with various inventory
management and logistics workflows, came to their decision.

### Pallets of items using packaging

A warehouse receives shipments of soap organized on physical pallets, each containing 96 bars. These
pallets are used for internal transfers and are also sold as standalone units. For logistical
purposes, the pallet’s weight must be included in the total shipping weight for certain deliveries.
Additionally, the pallet requires a barcode to facilitate tracking, and the number of individual
bars of soap must be included in the stock count when the pallet is received.

After evaluating various options, *product packaging* was the most suitable solution. Packaging
enables assigning a barcode to a pallet, identifying it as a “pallet type” containing 96 soap bars.
This barcode streamlines operations by automatically registering the grouped quantity. Key
distinctions include:

- **Warehouse tracking limitations**: Odoo tracks only the total quantity, not the number of
  packagings. For instance, if a pallet with 12 and 24 quantities is received, Odoo records 36
  quantities, not the pallet details.
- **Packaging barcodes are type-specific, not unique**: Barcodes represent packaging types (e.g.,
  “pallet of 96 soap bars”) but do not uniquely identify individual pallets, such as Pallet #1 or
  Pallet #2.

### Capture product information using barcode

An Odoo user expects the **Barcode** app to display the typical storage location of a product by
scanning a barcode for a container.

*Packages* was the most suitable. When the [appropriate setting is enabled](configure/package.html#inventory-warehouses-storage-enable-package), scanning a package barcode displays its contents in
the **Barcode** app.

Packages represent physical containers, enabling detailed tracking of the items they hold.
Scanning a package provides visibility into its contents and facilitates operations, like inventory
moves.

### Track different units of measure in storage

A fruit juice distributor tracks multiple UoMs for their operations:

- Fruits are purchased in tons.
- Juice is produced and stored in kilograms.
- Small samples are stored in grams for recipe testing.

*Unit of Measure* was most suitable. Odoo automatically converts tons to kilograms during
receipts. However, since Odoo tracks only one UoM per product in the database, the company uses
lot numbers to differentiate UoMs:

- LOT1: Grams (g)
- LOT2: Kilograms (kg)

Manual inventory adjustments are required to convert between lots, such as subtracting 1 kg from
LOT2 to add 1,000 g to LOT1. While functional, this workaround can be time-consuming and prone to
errors.

---

# Product tracking

*Lots* and *serial numbers* are the two ways to identify and track products in Odoo. While there are
similarities between the two traceability methods, there are also notable differences that affect
receipts, deliveries, and inventory reports.

A *lot* usually indicates a specific batch of an item that was received, is currently stored, or was
shipped from a warehouse. However, it can also pertain to a batch of products manufactured in-house,
as well.

A *serial number* is a unique identifier assigned incrementally (or sequentially) to an item or
product, used to distinguish it from other items or products.

> **Note:**
>
> - [Lot numbers](product_tracking/lots.html)
> - [Serial numbers](product_tracking/serial_numbers.html)

## Enable lots & serial numbers

To track products using lots and serial numbers, the *Lots & Serial Numbers* feature must be
enabled.

To do that, go to the Inventory app ‣ Configuration ‣ Settings, scroll down to
the Traceability section, and click the box next to Lots & Serial Numbers.
Then, click the Save button to save changes.

![Enabled lots and serial numbers feature in inventory settings.](../../../../_images/differences-enabled-setting.png)

## When to use lots

Lots are useful for products that are manufactured or received in large quantities, such as clothes
or food. Lots and can be used to trace a product back to a group, which is especially useful when
managing product recalls or expiration dates.

> **Tip:**
> ![Created lot with quantity of products in it.](../../../../_images/differences-lot.png)

Manufacturers assign lot numbers to groups of products that have common properties; this can lead to
multiple goods sharing the same lot number. This helps identify a number of products in a single
group, and allows for end-to-end traceability of these products through each step in their life
cycles.

## When to use serial numbers

The goal of assigning serial numbers to individual products is to make sure every item’s history is
identifiable when it travels through the supply chain. This can be especially useful for
manufacturers that provide after-sales services related to products they sell and deliver.

> **Tip:**
> ![List of serial numbers for product.](../../../../_images/differences-serial-numbers.png)

Serial numbers can contain many different types of characters: numbers, letters, typographical
symbols, or a mixture of all three types.

## Traceability

Manufacturers and companies can refer to traceability reports to see the entire life cycle of a
product. These reports include vital information, like where it came from (and when), where it was
stored, and to whom it was sent.

To see the full traceability of a product, or group products by lots and/or serial numbers, go to
Inventory app ‣ Products ‣ Lots/Serial Numbers. Doing so reveals the
Lots/Serial Numbers dashboard.

From here, products with lots or serial numbers assigned to them are listed by default. They can
also be expanded to show what lots or serial numbers have been specifically assigned to them.

To group by lots or serial numbers, first remove any default filters from the search bar in the
upper-right corner. Then, click Group By, and select Add Custom Group, which
reveals a mini drop-down menu. From this mini drop-down menu, select Lot/Serial Number,
and click Apply.

Doing so reveals all existing lots and serial numbers, and each can be expanded to show all product
quantities with that assigned number. For unique serial numbers that are *not* reused, there should
*only* be one product per serial number.

![Reporting page with drop-down lists of lots and serial numbers.](../../../../_images/differences-tracking.png)
> **Note:**
>
> For additional information regarding an individual lot number or serial number, click the line
> item for the lot or serial number to reveal that specific number’s Lot or
> Serial Number form. From this form, click the Location and
> Traceability smart buttons to see all stock on-hand using that serial number. Any
> operations made using that lot or serial number can be found here, as well.

---

# Warehouses and storage

---

# Inventory management

In the Odoo *Inventory* app, [warehouses](inventory_management/warehouses.html) handle the broader
organization and distribution of stock across different physical sites, while [locations](inventory_management/use_locations.html) provide a more detailed breakdown within each warehouse for
efficient item management.

This document serves as an introduction to the terminology and concepts necessary to master
*Inventory*. For specific instructions and examples of how things work, refer to individual
documentation pages.

> **Note:**
>
> [Odoo Tutorials: Warehouses & Locations](https://www.youtube.com/watch?v=zMvudZVLuUo)

## Warehouses

[Warehouses](inventory_management/warehouses.html) represent a physical place, with a physical
address, where a company’s items are stored.

Configure [routes](../shipping_receiving/daily_operations/use_routes.html) in a warehouse to
control how products move to customers, from vendors, within the warehouse, or [between
warehouses](replenishment/resupply_warehouses.html).

## Locations

[Locations](inventory_management/use_locations.html) refer to specific areas within a warehouse,
such as shelves, floors, or aisles. These are sub-divisions within a warehouse, and are unique to
that warehouse. Users can create and manage numerous locations within a single warehouse to organize
inventory more precisely.

> **Note:**
>
> - [Locations](inventory_management/use_locations.html)
> - [Inventory adjustments](inventory_management/count_products.html)
> - [Cycle counts](inventory_management/cycle_counts.html)
> - [Scrap inventory](inventory_management/scrap_inventory.html)

### Location types

*Location types* in Odoo help categorize and manage where products are, and what actions need to be
taken with them. By default, on the Inventory app ‣ Configuration ‣ Locations
page, only internal locations are displayed.

To view the seven location types in Odoo, select any location, and in the Location Type
field, there are:

- Vendor: defines an area where products purchased from vendors originate. Items here
  are **not** in stock.
- Virtual: used to organize and structure the warehouse hierarchy. For example, the
  virtual location `WH` (short for warehouse) groups all internal locations, such as `Stock`,
  receiving docks, quality checkpoints, and packing areas to show they all belong to the same
  warehouse.

  > **Warning:**
  >
  > Virtual locations should **not** contain products, but it is possible to move them there.
- Internal: storage locations within the warehouse. Items stored in these locations are
  accounted for in [inventory valuation](../inventory_valuation/cheat_sheet.html).
- Customer: where sold products are tracked; items here are no longer in stock.
- Inventory Loss: counterpart location to consume missing items or create stock,
  accounting for discrepancies.

  In Odoo, examples of inventory loss locations are *Inventory adjustment*, used to account for
  discrepancies during an inventory count, and *Scrap*, which is where damaged goods are sent to
  account for inventory losses.

  > > **Tip:**
  > >
  > > `Inventory adjustment` is a location with the Inventory Loss type. The database
  > > shows `8` units in `WH/Stock`, but an inventory check reveals `4`. To correct the quantity,
  > > four units are moved from `WH/Stock` to `Inventory adjustment`.
  > >
  > > ![Product ends up in Inventory adjustment.](../../../../_images/inventory-loss.png)
- Production: where raw materials are consumed, and [manufactured products](../../manufacturing.html) are created.
- Transit: used for inter-company or inter-warehouse operations to track products
  shipped between different addresses, such as [Physical Locations/Inter-warehouse
  transit].

![List of locations in Odoo.](../../../../_images/locations1.png)
> **Note:**
>
> In Odoo, location types are color-coded:
> :   - **Blue**: virtual locations
>     - **Black**: internal and external locations (including inventory loss, vendor, and customer
>       locations).

### View locations in Odoo

Odoo databases include preconfigured virtual locations to organize the hierarchy of locations. These
provide helpful context, and distinguish between internal and external locations.

- *Physical locations* group internal locations—such as secondary warehouses and subcontractor
  sites. Because [inventory valuation](../inventory_valuation/cheat_sheet.html) changes only when
  goods move from internal to external locations, Odoo uses physical locations to track stock that
  is off-site or in transit without affecting valuation.

> > **Tip:**
> >
> > When moving products in warehouses `WH` and `WH2`, the items are not in either warehouse, but
> > still belong to the company. While in transit, they are placed in the `Inter-warehouse transit`
> > location, a Transit type.
> >
> > This location is under the view location, `Physical Locations`, indicating that
> > `Inter-warehouse transit` is outside of a warehouse, but still part of the company. Doing so
> > does not affect the inventory valuation of the products.

- *Partner locations* group customer and vendor locations (external locations) together. Transfers
  to these locations affect inventory valuation.
- *Virtual locations* are locations that do **not** exist physically, but it is where items that are
  not in inventory can be placed. These can be items that are no longer in inventory due to loss, or
  other factors.

---

# Replenishment

In Odoo, stock can be replenished one of three ways: *reordering rules*, the *make to order* (MTO)
route, or using the *master production schedule* (MPS).

Each replenishment mechanism triggers the creation or suggestion of a purchase order (PO) or
manufacturing order (MO), with the best choice depending on the business process.

[#### Reordering rules

Automatically suggest or generate POs or MOs when stock falls below a minimum level.

Recommended](replenishment/reordering_rules.html)[#### Just in time logic

Avoid overstocking by placing order precisely to meet deadlines.

Recommended](replenishment/just_in_time.html)[#### MTO

Automatically generate POs or MOs when sales orders are confirmed.

Beginner-friendly](replenishment/mto.html)[#### MPS

Manage long-term replenishment based on inputted sales forecasts, via a dashboard.](../../manufacturing/workflows/use_mps.html)[#### Suggest quantities

Suggest quantities to order based on a past sales.

Beginner-friendly](../../purchase/advanced/suggest.html)

## Replenishment strategies

### Replenishment report and reordering rules

Reordering rules are rules that can be set up to maintain a minimum stock level. They are often
configured to support manufacturing or sales requirements. When a product’s stock falls at or below
the minimum level, Odoo generates (or suggests) a purchase or manufacturing order to replenish stock
to the maximum level.

When using automatic reordering rules, Odoo generates a new order. When using manual, Odoo suggests
orders on the replenishment report. For detailed guidance, refer to the [replenishment report](replenishment/report.html) and [reordering rules](replenishment/reordering_rules.html).

Key points include:

- [Automatic reordering rules](replenishment/reordering_rules.html#inventory-warehouses-storage-auto-rr): Automatically create
  POs or MOs when stock falls below the minimum level. While this is convenient, it is less
  flexible.
- [Manual reordering rules](replenishment/reordering_rules.html#inventory-warehouses-storage-manual-rr): Generate suggestions in
  the replenishment report for user review, allowing adjustments and batch orders while meeting
  deadlines.
- [Just in time logic](replenishment/just_in_time.html): A strategy to replenish only what is
  needed to prevent overstocking.

> **Note:**
>
> - [Reordering rules](replenishment/reordering_rules.html)
> - [Replenishment report](replenishment/report.html)

### Make to order

An MTO strategy means that procurement or production is triggered only after a sales order has
been confirmed. This strategy is recommended when products are customizable, demand is
unpredictable, there is limited storage capacity, and when products are high in value and low in
demand. In such cases, it does not make sense to keep on-hand inventory.

Unlike products replenished using reordering rules, Odoo automatically links the sales order to the
PO or MO generated by the MTO route.

Another difference between reordering rules and MTO is, with MTO, Odoo generates a draft PO or
MO immediately after the SO is confirmed. With reordering rules, Odoo generates a draft PO or
MO when the product’s forecasted stock falls below the set minimum quantity.

In addition, Odoo automatically adds quantities to the PO or MO as the forecast changes, so long
as the PO or MO is not confirmed.

The MTO route is the best replenishment strategy for products that are customized, and/or for
products that have no stock kept on-hand.

> **Note:**
>
> [Replenish on order (MTO)](replenishment/mto.html)

### Master production schedule

The MPS is a dashboard where products and their forecasted
quantities are entered. Based on confirmed manufacturing and purchase orders, the dashboard
recommends amounts to order or produce.

This a useful **manual** tool for keeping track of quantities. The MPS **should absolutely not** be used alongside reordering rules, as the automated workflow
disrupts its manual replenishment method.

> **Note:**
>
> [Master production schedule](../../manufacturing/workflows/use_mps.html)

---

# Reporting

---

# Shipping and receiving

---

# Inbound and outbound flows

Configuring inbound and outbound flows in Odoo is key to optimizing efficiency, traceability, and
cost. Warehouse managers must balance speed and control, choosing between a streamlined process or
added checkpoints.

Odoo offers one-step, two-step, and three-step flows, with more steps providing greater control but
increasing operations. The best setup depends on quality checks, packaging, and warehouse size.

This guide helps businesses determine the most suitable configuration.

## One-step flow

The *one-step inventory flow* is the simplest option, with minimal handling steps and the least
traceability. In this setup, products move directly from vendors to stock or from stock to
customers, with Odoo only tracking when items enter or leave the warehouse. This makes it ideal for
businesses with high-volume, low-risk products or fast-moving operations where additional validation
steps aren’t necessary.

- **Receiving**: Products go directly into stock.
- **Shipping**: Products ship directly from stock.
- **Best for**: Small warehouses, low stock levels, and non-perishable items, where minimal
  processing is needed before products are stored or shipped.

> **Note:**
>
> [One-step receipt and delivery](daily_operations/receipts_delivery_one_step.html)

## Two-step flow

A *two-step flow* adds an input or output area for processing products before storage or shipment.
Incoming goods can be unboxed and inspected before shelving, while outgoing shipments are sorted and
consolidated before dispatch. This setup improves efficiency by assigning storage teams to picking
and stocking, while dedicated teams handle unboxing, (possibly) packing, and final verification to
reduce order fulfillment errors.

- **Receiving**: Products move to an *input* area before being transferred into stock.

  - Until transferred, received products are not automatically reserved for manufacturing, shipping,
    or other operations.
- **Shipping**: Products move to an *output* before shipping to allow for [sorting or
  consolidation](picking_methods.html).
- **Best for**: Large warehouses, high stock levels, bulky items, and workflows that separate
  receiving from storage to improve organization and efficiency.

> **Note:**
>
> [Two-step receipt and delivery](daily_operations/receipts_delivery_two_steps.html)

## Three-step flow

A three-step flow builds on the two-step process by adding a quality check and packing area,
enforcing stricter processes and improving oversight.

> **Warning:**
>
> While this setup enhances process control, separating picking and packing requires validation at
> each step. If the same person handles both, it may cause redundancy and slow operations.
>
> Quality checks and packing **do not** require a three-step flow. To quality check outside of this
> flow:
>
> - Enable [quality control points](../../quality/quality_management/quality_control_points.html)
>   separately
> - Perform [manual quality checks](../../quality/quality_management/quality_checks.html#quality-quality-checks-manual)
>
> Activate the [Packages feature](../product_management/configure/package.html#inventory-warehouses-storage-enable-package) to package
> outside of the three-step flow.

- **Receiving**: Products follow a structured process: *input area* → *quality control* → *stock*.
- **Shipping**: Products are *picked*, *packed*, and then *shipped*, ensuring proper handling and
  organization.
- **Best for**: Very large warehouses with strict quality control requirements, dedicated picking
  and packing workflows, and a need for clear traceability across multiple handling stages. Suitable
  when multiple teams manage different steps before products are stocked or shipped.

> **Note:**
>
> - [Three-step receipt](daily_operations/receipts_three_steps.html)
> - [Three-step delivery](daily_operations/delivery_three_steps.html)

## Add-ons

To optimize each flow, Odoo provides additional features that can enhance the process.

### Storage

To organize and store products efficiently, use:

[#### Putaway rules

Guide products to specific storage locations based on predefined rules](daily_operations/putaway.html)[#### Storage categories

Set item or weight limits to prevent overstocking at the location and ensure proper
organization](daily_operations/storage_category.html)[#### Consignment

Keep track of products owned by third parties](daily_operations/owned_stock.html)

### Delivery

Tailor the outgoing shipment process to fit the business needs. Picking methods and removal
strategies control how products are reserved for orders, while dropshipping determines how they
move. Configuring these options in Odoo ensures visibility into product movement and confirms that
items reach customers efficiently.

[#### Dropshipping

Coordinate with vendors to deliver orders directly to customers, bypassing internal stock](daily_operations/dropshipping.html)[#### Picking methods

Optimize picking operations using piece, batch, cluster, or wave picking techniques](picking_methods.html)[#### Removal strategies

Use FIFO, LIFO, or FEFO strategies to automate the selection of products for delivery](removal_strategies.html)

### Customization

Odoo’s flexible framework enables businesses to tailor workflows to match specific operational
needs.

[#### Custom routes

Define tailored receiving or delivery workflows to meet specific business needs](daily_operations/use_routes.html)

---

# Delivery methods

In Odoo, *delivery methods* make it possible to calculate shipping costs directly on sales orders
and [e-commerce](../../../websites/ecommerce/shipping.html) carts, providing customers and
sales teams with accurate shipping fee information. This transparency helps close sales by showing
customers the exact cost for each shipping carrier or delivery timeframe.

When activated in Odoo, the *Delivery Methods* setting adds the option of calculating the cost of
shipping on sales orders and e-commerce shopping carts.

When integrated with a [third-party carrier](setup_configuration/third_party_shipper.html#inventory-shipping-third-party), shipping prices
are calculated based on the carrier’s pricing information.

> **Note:**
>
> - [Third-party shipping carrier setup](setup_configuration/third_party_shipper.html#inventory-shipping-third-party)
> - [Odoo Tutorials: Delivery Prices](https://www.odoo.com/slides/slide/delivery-prices-613?fullscreen=1)

## Configuration

To calculate shipping on sales orders and e-commerce, the **Delivery Costs** module must be
installed. To do so, navigate to the Apps application from the main Odoo dashboard.

Then, remove the Apps filter, and type in `Delivery Costs` in the search bar. After
finding the Delivery Costs module, click Install to install it.

![Install the Delivery Costs module.](../../../../_images/install-module.png)

## Add shipping

Shipping methods are added to sales orders in the form of delivery products, which appear as
individual line items. First, navigate to the desired sales order by going to Sales
app ‣ Orders ‣ Orders.

Open the desired sales order, then click the Add shipping button. The Add a
shipping method pop-up window opens. Then, using the drop-down menu, select an available shipping
method.

The Total Order Weight is pre-filled based on product weights (that are defined in the
[Inventory](../product_management/configure/type.html#inventory-product-management-manufacture) tab for each product form). Edit the
field to specify the exact weight, and then click Add to add the shipping method.

> **Warning:**
>
> The amount defined in Total Order Weight overwrites the total product weights defined
> on the product form.

> **Note:**
>
> Some connected shipping methods require obtaining rates from the carrier. In this situation,
> click the  Get rate button, and the shipping costs are
> automatically updated from the carrier. These rates cannot be modified.

The shipping cost is added as a line item in the Order Lines tab as the
Delivery Product detailed on the shipping method form.

> **Tip:**
>
> A customer purchased a left-sided desk with storage and requested the item be delivered by hand.
> This delivery method is defined as `Furniture Delivery (Manual)` and has a cost of `$200`. The
> sales order contains two line items: one for the desk, and another for the delivery method.
>
> > ![Show delivery order on the sales order line.](../../../../_images/delivery-product1.png)

### Delivery order

The shipping method added to the sales order is linked to the shipping carrier details on the
delivery order. After confirming the order, a  Delivery smart button
appears at the top of the page. Click the  Delivery smart button to open
the warehouse delivery form. To add or change the delivery method on the delivery itself, open the
Additional Info tab and modify the Carrier field.

![Shipping carrier information on the delivery form.](../../../../_images/delivery-order1.png)

## Supported hardware

![The Zebra ZD411 works best to print labels from Odoo.](../../../../_images/label-printer.png)

For label printers, Odoo recommends the [Zebra ZD411](https://www.zebra.com/us/en/products/spec-sheets/printers/desktop/zd411-series.html), as Odoo
supports the ZPL protocol for automatic printing from a point of sale.

This printer has been tested on most label formats (PDF, PNG, ZPL) for all carriers that Odoo
supports.

---

# Reservation methods

Companies that sell and deliver goods to customers need to make sure they always have stock on-hand,
so when new sales orders are confirmed, they can deliver products on time.

In Odoo, this can be handled using *reservation methods*. Reservation methods control how products
included in a delivery order (DO) should be reserved for delivery, ensuring they are reserved at the
correct times, for the correct orders.

There are three different reservation methods in Odoo: *At Confirmation*, *Manually*, and *Before
scheduled date*.

At ConfirmationManuallyBefore scheduled date

Reserves products **only** when a sales order is confirmed, **and** if stock is already
available.

Once a quote is confirmed, product availability **must** be checked manually, and the required
quantity **must** be reserved manually.

A specific number of days can be selected; this is the maximum number of days **before** a
scheduled delivery date that products should be reserved.

## Configuration

Reservation methods are set on individual operations types. To configure reservation methods, go to
Inventory app ‣ Configuration ‣ Operations Types. Then, select the desired
operation type. Or, create a new one by clicking New.

In the General tab of the operation type form, locate the Reservation Method
option, and choose which method should be used for this type of operation.

![Reservation method field on delivery order operation type form.](../../../../_images/reservation-methods-operations-type-field.png)
> **Note:**
>
> If the Before scheduled date reservation method is selected, a new
> Reserve before scheduled date field appears below. From this field, the number of
> days before and days before when starred can be changed from the default
> `0`.
>
> Changing the days before value changes the maximum number of days before a scheduled
> date that products should be reserved.
>
> Changing the days before when starred value changes the maximum number of days before
> a scheduled date that starred (favorited) transfers for products should be reserved.
>
> ![Reserve before scheduled date fields with before scheduled date method chosen.](../../../../_images/reservation-methods-before-scheduled-date.png)

## Required applications

The two required applications that **must** be [installed](../../../general/apps_modules.html#general-install) to use reservation
methods are the *Sales* and *Inventory* apps.

> **Note:**
>
> In addition to delivery orders, reservation methods can also be used for *manufacturing orders*,
> *resupply subcontractor* orders, orders for *repairs*, and *internal transfers*, if desired. To
> enable this, configure the additional settings:
>
> - **For manufacturing orders:** Install the *Manufacturing* application by going to the
>   Apps application, locating the *Manufacturing* app, and clicking
>   Install.
> - **For resupply subcontractor:** Navigate to Manufacturing app ‣ Configuration
>   ‣ Settings, and under the Operations section, enable Subcontracting.
>   Then, click Save.
> - **For repairs:** Install the *Repairs* application by going to the Apps
>   application, locating the *Repairs* app, and clicking Install.
> - **For internal transfers:** Navigate to Inventory app ‣ Configuration ‣
>   Settings, and under the Warehouse section, enable Storage Locations.
>   Then, click Save.

Once these apps are installed, no additional features need to be enabled from the settings for
reservation methods to work. They will be available by default on certain operations types, and can
be viewed and changed by navigating to Inventory app ‣ Configuration ‣
Operations Types, and then clicking on a specific operations type.

> **Note:**
>
> When the Type of Operation is changed to Receipt on an
> Operations Type form, reservation methods are **not** available.

![Operations Types highlighted from the Configurations submenu in the Inventory app.](../../../../_images/reservation-methods-operations-type-menu.png)
> **Note:**
>
> - [At confirmation reservation](reservation_methods/at_confirmation.html)
> - [Manual reservation](reservation_methods/manually.html)
> - [Before scheduled date reservation](reservation_methods/before_scheduled_date.html)

---

# Picking methods

---

# Removal strategies

For companies with warehouses, *removal strategies* determine **which** products are taken from the
warehouse, and **when**. For example, for perishable products, prioritizing the picking of goods
with the nearest expiration date helps minimize food spoilage.

The following columns in the table below list the removal strategies available in Odoo, and detail
how pickings are determined and the picking order. Leverage these removal strategies to have
Odoo automatically select how products are selected for orders:

|  | [FIFO](removal_strategies/fifo.html) | [LIFO](removal_strategies/lifo.html) | [FEFO](removal_strategies/fefo.html) | [Closest Location](removal_strategies/closest_location.html) | [Least Packages](removal_strategies/least_packages.html) |
| --- | --- | --- | --- | --- | --- |
| Based on | [Incoming date](removal_strategies/fifo.html#inventory-warehouses-storage-arrival-date) | [Incoming date](removal_strategies/fifo.html#inventory-warehouses-storage-arrival-date) | [Removal date](removal_strategies/fefo.html#inventory-warehouses-storage-removal-date) | [Location sequence](removal_strategies/closest_location.html#inventory-warehouses-storage-sequence) | [Package quantity](removal_strategies/least_packages.html#inventory-warehouses-storage-pkg-qty) |
| Selection order | First in | Last in | [First to expire](removal_strategies/fefo.html#inventory-warehouses-storage-exp-date) | Alphanumeric name of location | Quantity closest to fulfilling demand |

For comprehensive examples of how to use each removal strategy, refer to each individual
documentation page.

> **Note:**
>
> FIFO is the default removal strategy. When a removal strategy is not set for the location or the
> product category, FIFO is used.

## Configuration

Removal strategies are set at either the product category or the storage location level.

![Change the Force Removal Strategy for either the product categories or locations.](../../../../_images/navigate-location-category.png)

Configure removal strategies on the location by going to Inventory ‣ Configuration
‣ Locations, and selecting the desired location. On the location form, choose a removal strategy
from the Removal Strategy field’s drop-down menu options.

> **Warning:**
>
> To set a removal strategy on a location, the Storage Locations and
> Multi-Step Routes settings **must** be enabled in Inventory ‣
> Configuration ‣ Settings.
>
> These features are **only** necessary when setting the removal strategy for a location.

Configure removal strategies on product categories by going to Inventory ‣
Configuration ‣ Categories, then selecting the intended product category. Next, choose a removal
strategy from the Force Removal Strategy drop-down menu options.

> **Warning:**
>
> When different removal strategies are applied to both the location and product category for a
> product, the value set in the Force Removal Strategy field on the category form takes
> priority.

## Required features

While some removal strategies are available by default, some additional features **must** be enabled
in Inventory ‣ Configuration ‣ Settings for the removal strategy option to
appear in the drop-down menu of the Force Removal Strategy or Removal
Strategy field.

Refer to the table below for a summary of required features. Otherwise, refer to the dedicated
sections for the removal strategy for more details on requirements and usage.

|  | FIFO | LIFO | FEFO | Closest Location | Least Packages |
| --- | --- | --- | --- | --- | --- |
| Required features | Lots & Serial Numbers | Lots & Serial Numbers | Lots & Serial Numbers, Expiration Date | Storage Locations, Multi-Step Routes | Packages |

### Lots and serial numbers

Lots and serial numbers differentiate identical products and track information like arrival or
expiration dates. To enable this feature, navigate to Inventory ‣ Configuration
‣ Settings. Under the *Traceability* heading, check the box beside Lots & Serial
Numbers to enable the feature.

![Enable lots and serial numbers.](../../../../_images/enable-lots.png)

Next, ensure the intended product is tracked by lots or serial numbers by navigating to the product
form through Inventory ‣ Products ‣ Products, and selecting the desired
product. On the product form, switch to the Inventory tab, and under the
Tracking field, select either the By Unique Serial Number or By
Lots options.

After enabling the features, assign lot or serial numbers to products using an [inventory
adjustment](../warehouses_storage/inventory_management/count_products.html) or during [product
reception](../product_management/product_tracking/lots.html#inventory-product-management-assign-lots).

### Locations and routes

**Storage locations** and **multi-step routes** are necessary features for setting **all** types of
removal strategies on a location. However, these features are specifically required for the closest
location removal strategy, as it is applied at the location level.

To activate these features, navigate to Inventory ‣ Configuration ‣ Settings.
Under the *Warehouse* heading, enable the Storage Location and Multi-Step
Routes features.

![Enable the locations and route features.](../../../../_images/enable-location1.png)

### Expiration date

Enable the **expiration date** feature to track expiration dates, best-before dates, removal dates,
and alert dates on a lot or serial number by navigating to Inventory ‣
Configuration ‣ Settings.

Under the *Traceability* heading, ensure the Lots & Serial Numbers feature is selected,
and then select the check box for Expiration Dates to enable the feature.

![Enable expiration dates feature for FEFO.](../../../../_images/enable-expiration.png)

### Packages

The *packages* feature is used to group products together and is required for the least packages
removal strategy.

Navigate to Inventory ‣ Configuration ‣ Settings and select the check box for
the Packages feature.

![Enable the packages feature.](../../../../_images/enable-pack.png)
> **Note:**
>
> - [Packages](../product_management/configure/package.html)
> - [2-step delivery](daily_operations/receipts_delivery_two_steps.html)
> - [3-step delivery](daily_operations/delivery_three_steps.html)

---

# Inventory valuation

---

# Valuation cheat sheet

> **Warning:**
>
> This documentation is for Odoo 19 or later.
> [Discover why we changed.]

## Costing Methods

Odoo supports 3 costing methods configured in accounting’s settings and, optionally,
the product’s category.

Standard Cost: fixed unit cost, updated manually
:   | Operation | Unit Cost | Qty On Hand | Delta Value | Inventory Value |
    | --- | --- | --- | --- | --- |
    |  | $10 | 0 |  | $0 |
    | Receive 8 @$10 | $10 | 8 | +8×$10 | $80 |
    | Receive 4 @$16 | $10 | 12 | +4×$10 | $120 |
    | Deliver 10 | $10 | 2 | -10×$10 | $20 |
    | Receive 2 @$9 | $10 | 4 | +2×$10 | $40 |

Average Cost: weighted average of all units
:   | Operation | Unit Cost | Qty On Hand | Delta Value | Inventory Value |
    | --- | --- | --- | --- | --- |
    |  | $0 | 0 |  | $0 |
    | Receive 8 @$10 | $10 | 8 | +8×$10 | $80 |
    | Receive 4 @$16 | $12 | 12 | +4×$16 | $144 |
    | Deliver 10 | $12 | 2 | -10×$12 | $24 |
    | Receive 2 @$6 | $9 | 4 | +2×$6 | $36 |

FIFO: first in, first out
:   | Operation | Unit Cost | Qty On Hand | Delta Value | Inventory Value |
    | --- | --- | --- | --- | --- |
    |  | $0 | 0 |  | $0 |
    | Receive 8 @$10 | $10 | 8 | +8×$10 | $80 |
    | Receive 4 @$16 | $12 | 12 | +4×$16 | $144 |
    | Deliver 10 | $16 | 2 | -8×$10  -2×$16 | $32 |
    | Receive 2 @$6 | $11 | 4 | +2×$6 | $44 |

> **Note:**
>
> Removal strategies also support LIFO and FEFO, but they only impact which product is first picked, not the
> valuation method. For example, you can pick using LIFO, but using average cost for valuation,
> as LIFO is not allowed by IFRS.

## Inventory vs Accounting

The [Inventory app](../../inventory.html) keeps track of the inventory
value in real time as you **receive and deliver goods**. The reporting menu lets you analyze
inventory quantities and values by company, location, product, and more.

The [Accounting app](../../../finance/accounting.html) updates accounts when you receive
**invoices or bills**. Even though receipts and invoices differ, it’s not practical for
accountants to post journal entries for every inventory movement. So, they post a closing entry
to account for the difference between what has been invoiced and received/delivered. This closing
process happens usually once a year for SMEs, or once a month for larger companies.

|  | Accounting | Inventory |
| --- | --- | --- |
| Purchase Order | / | / |
| Receipt | / | ✓ |
| Vendor Bill | ✓ | / |
| Sales Order | / | / |
| Customer Invoice | ✓ | / |
| Delivery | / | ✓ |
| Closing Entry | ✓ | / |

## Accounting Methods

There are two accounting practices on how to maintain your accounts, defined in
Accounting app ‣ Configuration ‣ Settings, under the
Inventory Valuation section:

**Periodic:** Post vendor bills as expenses by nature, and update stock valuation in the closing
entry by reducing expenses (stock variation). This is the best practice in Europe.

**Perpetual:** Post vendor bills as assets (stock valuation), report expenses when goods are sold
(cost of goods sold). This is the best practice in countries that follow Anglo-Saxon accounting,
like the USA and India.

- Stock Account on the product’s category
- Stock Variation on the stock account
- Expense/Cost of Goods Sold on the product/category
- Inventory Adjustment on the Inventory Loss location
  (optional, recommended for Anglo-Saxon accounting)
- Expense on the stock account
  (for perpetual Continental accounting only)

|  | EU Periodic | EU Perpetual | US Periodic | US Perpetual |
| --- | --- | --- | --- | --- |
| ADJUSTMENT |  | Stock |  | Stock |
|  |  | LOSS |  | Shrinkage |
|  |  |  |  |  |
| BILL | Expense | Stock | COGS | Stock |
|  | Payable | Payable | Payable | Payable |
|  |  |  |  |  |
| INVOICE |  | Expense |  | COGS |
|  |  | Stock |  | Stock |
|  | Income | Income | Income | Income |
|  | Receivable | Receivable | Receivable | Receivable |
|  |  |  |  |  |
| Closing | Stock | Stock | Stock | Stock |
| [1] | Variation | Expense | Variation | Variation |
| [2] | LOSS |  | Shrinkage |  |
| [3] |  | Variation |  |  |
|  |  | Expense |  |  |

1. Inventory valuation - Accounting valuation
2. Inventory valuation lost,
   only if an account is set on the loss location
3. Accounting valuation end of period -
   Valuation beginning of period

## Accounting Entries

## Journal Entries Configuration

## Reporting

### In Inventory

Open Inventory ‣ Reporting ‣ Stock to view your current inventory level and
valuation for each product, or to review historical data as of a previous date.

![../../../../_images/valuation-stock.png](../../../../_images/valuation-stock.png)

#### Unit cost

To check a product’s existing unit price updates and their origins, click on the product’s
Unit Cost. In AVCO this allows you to understand how the
currently used value was calculated.

![../../../../_images/unit-cost.png](../../../../_images/unit-cost.png)

#### Total value

To see all incoming quantities for which you still have a remaining quantity and the value used for
their valuation, click on a product’s Total Value.

- In AVCO or standard cost, the used value is always the current average unit cost.
- In FIFO, remaining units from each previous incoming move retain their own individual valuation.

In FIFO or AVCO, remaining quantities from a previous incoming move can have their value adjusted if
necessary: Select the incoming moves to be adjusted, click  Actions, and
then click Adjust Valuation. Enter the new Value and, optionally, a
Description.

![../../../../_images/total-value.png](../../../../_images/total-value.png)

### In Accounting

To view the difference between the accounting stock value and the current inventory value recorded
thanks to the incoming moves with a remaining quantity, go to Accounting ‣ Review
‣ Inventory Valuation.

To generate a new accounting entry to review and post, click Generate Entry.

![../../../../_images/valuation-accounting.png](../../../../_images/valuation-accounting.png)

To view a list of sales and purchase orders for which accrual entries should be encoded, go to
Accounting ‣ Review and select the relevant menu item (Bill To
Receive, Invoices To Be Issued, Billed Not Received and Invoiced
Not Delivered). Select the desired lines and click Create Accrual
Entries.

With Anglo-Saxon perpetual accounting, this will also help to distribute recorded inventory
variations to accounts such as Bills to Receive/GRNI or
COGS as shown in the [Accounting Entries]
and [Journal Entries Configuration] sections.

![../../../../_images/accrual.png](../../../../_images/accrual.png)
![../../../../_images/accrual1.png](../../../../_images/accrual1.png)
![../../../../_images/accrual2.png](../../../../_images/accrual2.png)
![../../../../_images/accrual3.png](../../../../_images/accrual3.png)

## Changes in Odoo 19

Before Odoo 19, the Perpetual accounting method was implemented by posting real-time accounting
entries at each stock movement. That created a lot of journal items in accounting, which was an
issue for performance, general ledger clarity and auditability.

Since Odoo 19, the Perpetual method impacts the stock valuation account at the invoice level. The
closing entry is then used to manage bills to receive, invoices to issue, deferred revenues, prepaid
expenses, and other gaps between inventory values and accounting ones.

|  | Odoo 18 | Odoo 19 |
| --- | --- | --- |
| Periodic Continental | Manual closing | Automated closing |
| Periodic Anglo-Saxon | Not supported | Fully supported |
| Perpetual Continental | Manual closing | ✓ |
| Perpetual Anglo-Saxon | Manual closing | ✓ |
| Accounting valuation | Requires inventory | Accounting only |
| Perpetual Entries | Invoices + every moves | Invoices + one closing |
| Invoices to issue | ✗ | ✓ |
| Prepaid expenses | ✗ | ✓ |
| Bills to receive | ✗ | ✓ |
| Deferred revenues | ✗ | ✓ |
| Performance | Slower | Faster |
| General ledger | More journal entries | Fewer journal entries |

---

# Landed costs

In Odoo, the *Landed Costs* feature is used to take additional costs into account when calculating
the valuation of a product. This includes the cost of shipment, insurance, customs duties, taxes,
and other fees.

## Configuration

To add landed costs to products, the *Landed Costs* feature must first be enabled. To enable this
feature, navigate to Inventory app ‣ Configuration ‣ Settings, and scroll to
the Valuation section.

Tick the checkbox next to the Landed Costs option, and click Save to save
changes.

Once the page refreshes, a new Default Journal field appears below the Landed
Costs feature in the Valuation section.

Click the Default Journal drop-down menu to reveal a list of accounting journals. Select
a journal for which all accounting entries related to landed costs should be recorded.

![Landed Costs feature and resulting Default Journal field in the Inventory settings.](../../../../_images/integrating-landed-costs-enabled-setting.png)

## Create landed cost product

For charges that are consistently added as landed costs, a landed cost product can be created in
Odoo. This way, a landed cost product can be quickly added to a request for quotation (RfQ) or a
vendor bill as an invoice line, instead of having to be manually entered every time a new vendor
bill is created.

To do this, create a new product by going to Inventory app ‣ Products ‣
Products, and clicking New.

Assign a name to the landed cost product in the Product Name field (i.e. `International
Shipping`). In the Product Type field, select Service as the
Product Type.

> **Warning:**
>
> Landed cost products **must** have their Product Type set to Service.

Click the Purchase tab, and tick the checkbox next to Is a Landed Cost in
the Vendor Bills section. Once ticked, a new Default Split Method field
appears below it, prompting a selection. Clicking that drop-down menu reveals the following options:

- Equal: splits the cost equally across each product included in the receipt, regardless
  of the quantity of each.
- By Quantity: splits the cost across each unit of all products in the receipt.
- By Current Cost: splits the cost according to the cost of each product unit, so a
  product with a higher cost receives a greater share of the landed cost.
- By Weight: splits the cost, according to the weight of the products in the receipt.
- By Volume: splits the cost, according to the volume of the products in the receipt.

![Is a Landed Cost checkbox and Default Split Method on service type product form.](../../../../_images/integrating-landed-costs-landed-cost-product.png)

When creating new RfQs, this product can be added as an invoice line as a landed cost. This
product can also be added to vendor bills that are in the draft state.

> **Warning:**
>
> To apply a landed cost on a vendor bill, products in the original PO **must** belong to a
> *Product Category* with a *Costing Method* of either AVCO or FIFO.

## Create purchase order

Navigate to Purchase app ‣ New to create a new RfQ. In the Vendor
field, add a vendor to order products from. Then, click Add a product, under the
Products tab, to add products to the RfQ.

Once ready, click Confirm Order to confirm the order. Then, click Receive
once the products have been received, followed by Validate.

### Create vendor bill

Once the vendor fulfills the PO and sends a bill, a vendor bill can be created from the PO in
Odoo.

Navigate to the Purchase app, and click into the PO for which a vendor bill
should be created. Then, upload the bill or click the Bill Matching smart button to
match with an existing bill. This opens a new Vendor Bill in the Draft
stage.

In the Bill Date field, click the line to open a calendar popover menu, and select the
date on which this draft bill should be billed.

Click Add a line. Add the landed cost product to the vendor bill.

Click the  (Save) icon to manually save and update the
draft bill.

![Landed Costs column checkboxes for product and landed cost.](../../../../_images/integrating-landed-costs-checkboxes.png)

In the Landed Costs column, the product ordered from the vendor does **not** have its
checkbox ticked, while the landed cost product’s checkbox **is** ticked. This differentiates landed
costs from all other costs displayed on the bill.

Additionally, at the top of the form, a Create Landed Costs button appears.

![Create Landed Costs button on vendor bill.](../../../../_images/integrating-landed-costs-create-button.png)

## Add landed cost

Click Create Landed Costs at the top of the vendor bill.

Doing so automatically creates a landed cost record, with a set landed cost pre-filled in the
product line in the Additional Costs tab.

From the Landed Cost form, click the Transfers drop-down menu, and select
which transfer the landed cost belongs to. Only validated transfers can be selected.

![Landed cost form with selected receipt transfer.](../../../../_images/integrating-landed-costs-transfers-menu.png)
> **Note:**
>
> In addition to creating landed costs directly from a vendor bill, landed cost records can *also*
> be created by navigating to Inventory app ‣ Operations ‣ Landed Costs, and
> clicking New.

After setting the picking from the Transfers drop-down menu, click Compute
(at the bottom of the form, under the Total: cost).

Click the Valuation Adjustments tab to see the impact of the landed costs. The
Original Value column lists the original price of the PO, the Additional
Landed Cost column displays the landed cost, and the New Value column displays the sum
of the two, for the total cost of the PO.

Once ready, click Validate to post the landed cost entry to the accounting journal.

> **Note:**
>
> Each journal entry created for a landed cost on a vendor bill can be viewed in the
> Accounting app.
>
> To locate these journal entries, navigate to Accounting app ‣ Accounting ‣
> Journal Entries, and locate the correct entry, by number (e.g. `STJ/2025/XXXXX`).
>
> Click into the journal entry to view the Journal Items, and other information about
> the entry.
>
> ![Journal Entry form for landed cost created from vendor bill.](../../../../_images/integrating-landed-costs-journal-entry.png)

---

# Valuation by lots/serial numbers

Track [inventory valuation](cheat_sheet.html) by [lots or serial numbers](../product_management/product_tracking.html) to:

1. [Compare and differentiate purchasing cost],
   based on lot or serial numbers.
2. Track the actual cost of manufactured products, based on the real cost of each tracked component
   used.
3. Depreciate specific lot or serial numbers when they sit in stock for too long.

> **Warning:**
>
> Please read this [introduction to inventory valuation](cheat_sheet.html) before setting up
> valuation by lot/serial numbers.

## Configuration

To enable valuation by lots or serial numbers, begin by enabling the [Lots and Serial Numbers
feature](../product_management/product_tracking.html#inventory-product-management-enable-lot-serial). After that, go to
Inventory app ‣ Products ‣ Products, and select the desired product, or create
a new product, by clicking New.

On the product form, in the Category field, choose a product category. Ensure the
product category’s Costing Method is set to *First In First Out (FIFO)* or
*Average Cost (AVCO)*.

> **Note:**
>
> To check the costing method set on the product category, hover over the Category
> field, and click the  (Internal Link) icon.

Next, activate the product to be tracked by lots or serial numbers by ticking the Track
Inventory checkbox. Then, click the adjacent field that appears, and choose either By
Lots or By Unique Serial Number from the resulting drop-down menu.

Doing so makes the Valuation by Lot/Serial number checkbox appear below it. Tick that
checkbox, and the configuration to track valuation by lot or serial numbers is complete.

![Product form showing the Valuation by Lot or Serial Number feature.](../../../../_images/product-form1.png)

Product form showing the Valuation by Lot or Serial Number feature

## Valuation layers

To understand how valuation by lots and serial numbers works, consider these scenarios:

1. [Purchase and sell products]: cost is
   calculated based on the *product category’s* costing method.
2. [Create new lot/serial numbers] using an
   inventory adjustment: value of the new lot/serial number is assigned to the cost from the product
   form.
3. Inventory adjustment to update quantities for an [existing lot/serial number]: value is assigned based on the most
   recent cost for that lot/serial number.

For both AVCO and FIFO methods, the *Cost* field
on the product form is calculated using this formula:

\(Avg~Cost = \frac{Total~Value}{Total~Qty}\)

### Purchase products

Consider how purchasing products affect the inventory valuation, in the table below.

|  | Quantity | Lot number | Math | Average cost on product form |
| --- | --- | --- | --- | --- |
| Empty stock | 0.00 |  |  | $0 |
| Day 1: Receive one product at $10/unit | 1.00 | LOT 1 | \(\frac{10}{1}\) | $10 |
| Day 2: Receive another product at $20/unit | 1.00 | LOT 2 | \(\frac{10+20}{2}\) | $15 |

![Show Cost on the product form.](../../../../_images/lip-gloss.png)

As a result, the product form displays an average cost of $15 in the **Cost** field.

### Create new lot/serial number

Creating a new lot/serial number through an [inventory adjustment](../warehouses_storage/inventory_management/count_products.html) assigns the same value as the cost
on the product form.

To make an inventory adjustment, and assign a lot number, go to Inventory app ‣
Operations ‣ Physical Inventory. Then, click New.

In the new inventory adjustment line that appears, set the Product, create the
Lot/Serial Number, set the Counted Quantity, and click
Apply.

To view the valuation layer, go to Inventory app ‣ Reporting ‣ Valuation. The
Total Value per unit matches the *Cost* on the product form.

> **Tip:**
>
> Continuing the example in the table above, when the product cost is `$15`, the valuation for a
> newly-created `LOT3` is also be `$15`.
>
> ![Show inventory adjustment valuation.](../../../../_images/create-new.png)

### Existing lot/serial number

When adjusting the quantity of an existing lot/serial number, the value is based on the most recent
valuation layer for that specific lot/serial number.

> **Tip:**
>
> Continuing the example in the table above, the value for `LOT 1` is `$10`.
>
> So, when the quantity is updated from `1.00` to `2.00`, the additional quantity is also valued at
> `$10`, reflecting the latest valuation layer for `LOT 1`.
>
> ![Show valuation of LOT 1 getting updated.](../../../../_images/existing.png)
>
>
> The inventory adjustment (top line) is valued the same as LOT 1 (bottom line).

## View valuation

To find the average cost of a specific lot/serial number, go to Inventory app ‣
Products ‣ Lots/Serial Numbers, and select the desired record.

Both the Cost and Average Cost fields show a unit’s average cost. The
Total Value reflects the total on-hand value for that lot/serial number.

> **Warning:**
>
> Ensure the costing method is set to *First In First Out (FIFO)* or *Average Cost (AVCO)* to
> display the cost on this page.

![Show cost of the lot/serial number.](../../../../_images/lot1.png)

Lot form, displaying **Cost** field. The **Valuation** smart button is in the top-right.

Valuation layers of a lot/serial number can be viewed through the [valuation report], or by clicking the lot/serial number’s
Valuation smart button. These detailed, line-by-line records can help determine how each
inventory move of the specific lot/serial number affects its valuation.

### Valuation report

Display the valuation of lots and serial numbers in the database by going to
Inventory app ‣ Reporting ‣ Valuation.

On the resulting Stock Valuation report, click the search bar, and in the
 Group By section of the resulting drop-down menu, select
Lot/Serial number.

> **Note:**
>
> Click the  (plus) icon to the right of a collapsed lot number line to
> manually modify the cost.
>
> This is useful for adjusting individual lot prices when a purchase order or bill includes
> multiple lots/serial numbers, as initial prices are identical upon reception.

![Show valuation report, by lots.](../../../../_images/stock-valuation.png)

### Valuation smart button

To access a filtered part of the *Stock Valuation* report, specific to a lot or serial number, go to
Inventory app ‣ Products ‣ Lots/Serial Numbers, and select the desired item.

On the Lot/Serial Numbers page, click the Valuation smart button.

![All stock moves relating to `LOT 1`.](../../../../_images/lot-stock-valuation.png)

All stock moves that affect the valuation of `LOT 1`.

---

# Account for scrapped goods

It’s essential to strike a balance between having sufficient stock on hand to meet demand while
avoiding overpurchasing. When working with perishable products, or when inventoried goods have
defects that prevent the product from being sold, occasionally, products must be scrapped and
removed from inventory. It’s important to account for these losses in the [Profit and Loss
report](../../../finance/accounting/reporting.html#accounting-reporting-profit-and-loss).

Generally, follow this process to account for scrapped goods in the *Profit and Loss* report:

1. [Enable settings in the Inventory configuration].
2. [Configure the product category].
3. [Set up a scrap location and its scrap journal].
4. [Scrap products].
5. [View scrapped products in the Profit and Loss report].

## Enable settings

To ensure scrapped goods can be seen in the *Profit and Loss* report, open Inventory
app ‣ Configuration ‣ Settings. In the Warehouse section, enable Storage
Locations.

## Configure the product category

Next, configure the product category. Open Inventory app ‣ Configuration ‣
Categories. Open or create a product category.

Next, set the Costing Method to either First In First Out (FIFO) or
Average Cost (AVCO):

- First In First Out (FIFO): Inventory is valued, and the cost of goods sold (COGS) is
  calculated by assuming the oldest items purchased are the first ones sold, tracking costs by
  specific receipt lots. It’s a precise method for fluctuating costs, and requires tracking units by
  their entry time (load/serial numbers) for accurate removal from stock.
- Average Cost (AVCO): Inventory value is calculated by dynamically averaging the cost
  of all units in stock, updating with each new purchase or manufacturing receipt to reflect
  fluctuating prices, making it ideal for varied vendor costs, with the system automatically
  recalculating the unit cost and value for assets and COGS. Odoo handles the math, adjusting the
  average cost automatically as products are bought or sold, but doesn’t change it when products
  sell, only updating when new stock arrives at a different price.

Next, set the Inventory Valuation field to Perpetual (at invoicing). This
setting ensures that real-time journal entries are created in the *Accounting* app whenever stock
enters or leaves the company’s warehouse.

## Set up a scrap location and its scrap journal

Next, you must create or edit an existing scrap location. Open Inventory app ‣
Configuration ‣ Locations. Open an existing location or create a new one by clicking
New.

> **Note:**
>
> By default, the Locations list is filtered to show only internal locations. Remove
> this filter to view all locations, including *Inventory Loss* locations.

Update the Location Type field to select Inventory Loss.

Specify a Loss Account by selecting the account used for scrapped goods.

> **Tip:**
>
> The `WH/Scrap` location is an Inventory Loss location that uses the `600001 Scrapped
> Goods` journal as its Loss Account.
>
> ![Specify an Inventory Loss Location Type and a Loss Account.](../../../../_images/example-scrap-location.png)

## Scrap products

After the product category and location are set up, [products can be scrapped](../warehouses_storage/inventory_management/scrap_inventory.html). Be sure to select the scrap location
in the Scrap Location field.

> **Tip:**
>
> `20` units of `Under-Eye Masks` are scrapped to `WH/Scrap`.
>
> ![Specify the Product, Quantity, and Scrap Location.](../../../../_images/example-scrap-order.png)

## View scrapped products in the Profit and Loss report

After products have been scrapped to the correct scrap location, view items scrapped to it in the
Profit and Loss report. Open Accounting app ‣ Reporting ‣ Profit and Loss. To
view the scrap order in the report, under the Gross Profit section, expand the
Expense category. Search for the scrap journal in the list and click the
 (vertical ellipsis) icon next to the scrap account and select
General Ledger.

> **Tip:**
>
> `$100` worth of `Under-Eye Masks` appear as a debit in the Profit and Loss’ General Ledger.
>
> ![View the General Ledger to see scrapped items in the Profit and Loss report.](../../../../_images/scrapped-profit-loss.png)

> **Note:**
>
> [Profit and Loss report](../../../finance/accounting/reporting.html#accounting-reporting-profit-and-loss)