from odoo import models, fields, api
from odoo.exceptions import UserError


class GreenLightReasonCode(models.Model):
    _name = "greenlight.reason.code"
    _description = "Reason Code"
    _order = "name"

    name = fields.Char(required=True)
    code_type = fields.Selection(
        [
            ("adjustment", "Adjustment"),
            ("void", "Void"),
            ("return", "Return"),
            ("waste", "Waste"),
        ],
        string="Type",
        required=True,
    )
    is_active = fields.Boolean(default=True)


class GreenLightInventoryAdjustment(models.Model):
    _name = "greenlight.inventory.adjustment"
    _description = "Inventory Adjustment"
    _inherit = ["mail.thread"]
    _order = "create_date desc"

    name = fields.Char("Reference", readonly=True, default="New")
    product_id = fields.Many2one(
        "greenlight.product",
        required=True,
        tracking=True,
        ondelete="restrict",
    )
    quantity = fields.Integer(
        required=True,
        help="Positive to add stock, negative to remove stock.",
    )
    reason_code_id = fields.Many2one(
        "greenlight.reason.code",
        required=True,
        domain="[('code_type', '=', 'adjustment')]",
        ondelete="restrict",
    )
    employee_id = fields.Many2one(
        "greenlight.employee",
        required=True,
        tracking=True,
        ondelete="restrict",
    )
    notes = fields.Text()
    stock_before = fields.Integer("Stock Before", readonly=True)
    stock_after = fields.Integer("Stock After", readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = (
                    self.env["ir.sequence"].next_by_code("greenlight.inventory.adjustment")
                    or "New"
                )
        records = super().create(vals_list)
        for rec in records:
            rec._apply_adjustment()
        return records

    def _apply_adjustment(self):
        """Atomically update product inventory and record before/after."""
        self.ensure_one()
        if self.quantity == 0:
            raise UserError("Adjustment quantity cannot be zero.")
        product = self.product_id
        stock_before = product.inventory_count
        self.env.cr.execute(
            "UPDATE greenlight_product "
            "SET inventory_count = inventory_count + %s "
            "WHERE id = %s "
            "RETURNING inventory_count",
            (self.quantity, product.id),
        )
        row = self.env.cr.fetchone()
        stock_after = row[0] if row else stock_before + self.quantity
        product.invalidate_recordset(["inventory_count"])
        self.write({
            "stock_before": stock_before,
            "stock_after": stock_after,
        })


class GreenLightInventoryCount(models.Model):
    _name = "greenlight.inventory.count"
    _description = "Inventory Count Session"
    _inherit = ["mail.thread"]
    _order = "create_date desc"

    name = fields.Char("Reference", readonly=True, default="New")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
        ],
        default="draft",
        tracking=True,
    )
    employee_id = fields.Many2one(
        "greenlight.employee",
        required=True,
        tracking=True,
        ondelete="restrict",
    )
    item_ids = fields.One2many("greenlight.inventory.count.item", "count_id")
    notes = fields.Text()
    completed_at = fields.Datetime("Completed At", readonly=True)
    total_discrepancy = fields.Integer(
        "Total Discrepancy",
        compute="_compute_total_discrepancy",
        store=True,
    )

    @api.depends("item_ids.discrepancy")
    def _compute_total_discrepancy(self):
        for rec in self:
            rec.total_discrepancy = sum(rec.item_ids.mapped("discrepancy"))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = (
                    self.env["ir.sequence"].next_by_code("greenlight.inventory.count")
                    or "New"
                )
        return super().create(vals_list)

    def action_start(self):
        """Populate count items from all active products and move to in_progress."""
        for rec in self:
            if rec.state != "draft":
                raise UserError("Only draft counts can be started.")
            # Remove any existing items (shouldn't happen, but defensive)
            rec.item_ids.unlink()
            products = self.env["greenlight.product"].search([("is_active", "=", True)])
            if not products:
                raise UserError("No active products found to count.")
            item_vals = []
            for product in products:
                item_vals.append({
                    "count_id": rec.id,
                    "product_id": product.id,
                    "expected_qty": product.inventory_count,
                    "counted_qty": 0,
                })
            self.env["greenlight.inventory.count.item"].create(item_vals)
            rec.state = "in_progress"

    def action_complete(self):
        """Apply discrepancies to product inventory and finalize the count."""
        for rec in self:
            if rec.state != "in_progress":
                raise UserError("Only in-progress counts can be completed.")
            for item in rec.item_ids:
                if item.discrepancy != 0:
                    self.env.cr.execute(
                        "UPDATE greenlight_product "
                        "SET inventory_count = inventory_count + %s "
                        "WHERE id = %s",
                        (item.discrepancy, item.product_id.id),
                    )
                    item.product_id.invalidate_recordset(["inventory_count"])
            rec.write({
                "state": "completed",
                "completed_at": fields.Datetime.now(),
            })

    def action_reset_to_draft(self):
        """Allow resetting a count back to draft (only if not completed)."""
        for rec in self:
            if rec.state == "completed":
                raise UserError("Completed counts cannot be reset.")
            rec.item_ids.unlink()
            rec.state = "draft"


class GreenLightInventoryCountItem(models.Model):
    _name = "greenlight.inventory.count.item"
    _description = "Inventory Count Line Item"

    count_id = fields.Many2one(
        "greenlight.inventory.count",
        required=True,
        ondelete="cascade",
    )
    product_id = fields.Many2one(
        "greenlight.product",
        required=True,
        ondelete="restrict",
    )
    expected_qty = fields.Integer("Expected Qty", readonly=True)
    counted_qty = fields.Integer("Counted Qty")
    discrepancy = fields.Integer(
        compute="_compute_discrepancy",
        store=True,
    )

    @api.depends("expected_qty", "counted_qty")
    def _compute_discrepancy(self):
        for rec in self:
            rec.discrepancy = rec.counted_qty - rec.expected_qty


class GreenLightPurchaseOrder(models.Model):
    _name = "greenlight.purchase.order"
    _description = "Purchase Order"
    _inherit = ["mail.thread"]
    _order = "create_date desc"

    name = fields.Char("Reference", readonly=True, default="New")
    supplier_name = fields.Char("Supplier", required=True, tracking=True)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("ordered", "Ordered"),
            ("received", "Received"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        tracking=True,
    )
    employee_id = fields.Many2one(
        "greenlight.employee",
        string="Ordered By",
        tracking=True,
        ondelete="restrict",
    )
    line_ids = fields.One2many("greenlight.purchase.order.line", "order_id")
    notes = fields.Text()
    ordered_at = fields.Datetime("Ordered At", readonly=True)
    received_at = fields.Datetime("Received At", readonly=True)

    total_cost = fields.Monetary(
        "Total Cost",
        currency_field="currency_id",
        compute="_compute_total_cost",
        store=True,
    )
    currency_id = fields.Many2one(
        "res.currency",
        default=lambda self: self.env.company.currency_id,
    )
    total_items = fields.Integer(
        "Total Items",
        compute="_compute_total_cost",
        store=True,
    )

    @api.depends("line_ids.subtotal", "line_ids.quantity")
    def _compute_total_cost(self):
        for rec in self:
            rec.total_cost = sum(rec.line_ids.mapped("subtotal"))
            rec.total_items = sum(rec.line_ids.mapped("quantity"))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = (
                    self.env["ir.sequence"].next_by_code("greenlight.purchase.order")
                    or "New"
                )
        return super().create(vals_list)

    def action_order(self):
        """Mark the PO as ordered."""
        for rec in self:
            if rec.state != "draft":
                raise UserError("Only draft orders can be submitted.")
            if not rec.line_ids:
                raise UserError("Cannot submit an order with no line items.")
            rec.write({
                "state": "ordered",
                "ordered_at": fields.Datetime.now(),
            })

    def action_receive(self):
        """Receive the PO — increment product inventory per line quantity."""
        for rec in self:
            if rec.state != "ordered":
                raise UserError("Only ordered POs can be received.")
            for line in rec.line_ids:
                self.env.cr.execute(
                    "UPDATE greenlight_product "
                    "SET inventory_count = inventory_count + %s "
                    "WHERE id = %s",
                    (line.quantity, line.product_id.id),
                )
                line.product_id.invalidate_recordset(["inventory_count"])
            rec.write({
                "state": "received",
                "received_at": fields.Datetime.now(),
            })

    def action_cancel(self):
        """Cancel the PO. Only draft or ordered POs can be cancelled."""
        for rec in self:
            if rec.state not in ("draft", "ordered"):
                raise UserError("Only draft or ordered POs can be cancelled.")
            rec.state = "cancelled"


class GreenLightPurchaseOrderLine(models.Model):
    _name = "greenlight.purchase.order.line"
    _description = "Purchase Order Line Item"

    order_id = fields.Many2one(
        "greenlight.purchase.order",
        required=True,
        ondelete="cascade",
    )
    product_id = fields.Many2one(
        "greenlight.product",
        required=True,
        ondelete="restrict",
    )
    quantity = fields.Integer(required=True, default=1)
    unit_cost = fields.Monetary(
        "Unit Cost",
        currency_field="currency_id",
    )
    subtotal = fields.Monetary(
        currency_field="currency_id",
        compute="_compute_subtotal",
        store=True,
    )
    currency_id = fields.Many2one(
        "res.currency",
        default=lambda self: self.env.company.currency_id,
    )

    @api.depends("quantity", "unit_cost")
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.quantity * rec.unit_cost

    @api.onchange("product_id")
    def _onchange_product_id(self):
        if self.product_id:
            self.unit_cost = self.product_id.cost
