from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class GreenLightOrder(models.Model):
    _name = "greenlight.order"
    _description = "Pre-Order / Online Order"
    _inherit = ["mail.thread"]
    _order = "create_date desc"
    _rec_name = "name"

    name = fields.Char("Reference", readonly=True, default="New")
    customer_id = fields.Many2one(
        "greenlight.customer", required=True, tracking=True, ondelete="restrict",
    )
    employee_id = fields.Many2one(
        "greenlight.employee", string="Assigned To", tracking=True, ondelete="restrict",
    )

    source = fields.Selection(
        [
            ("in_store", "In-Store"),
            ("leafly", "Leafly"),
            ("weedmaps", "Weedmaps"),
            ("website", "Website"),
            ("phone", "Phone"),
        ],
        required=True,
        default="in_store",
        tracking=True,
    )

    state = fields.Selection(
        [
            ("order_placed", "Order Placed"),
            ("in_progress", "In Progress"),
            ("ready_for_pickup", "Ready for Pickup"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        default="order_placed",
        required=True,
        tracking=True,
    )

    line_ids = fields.One2many("greenlight.order.line", "order_id")

    # Scheduling
    requested_date = fields.Datetime("Requested Pickup Time")
    completed_date = fields.Datetime("Completed At", readonly=True)

    # Totals
    subtotal = fields.Monetary(
        currency_field="currency_id", compute="_compute_totals", store=True,
    )
    total = fields.Monetary(
        currency_field="currency_id", compute="_compute_totals", store=True,
    )
    currency_id = fields.Many2one(
        "res.currency", default=lambda self: self.env.company.currency_id,
    )

    line_count = fields.Integer(compute="_compute_line_count")
    notes = fields.Text("Customer Notes")

    @api.depends("line_ids.subtotal")
    def _compute_totals(self):
        for rec in self:
            rec.subtotal = sum(rec.line_ids.mapped("subtotal"))
            tax_rate = self.env["greenlight.settings"].get_tax_rate()
            rec.total = rec.subtotal * (1 + tax_rate)

    @api.depends("line_ids")
    def _compute_line_count(self):
        for rec in self:
            rec.line_count = len(rec.line_ids)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = (
                    self.env["ir.sequence"].next_by_code("greenlight.order") or "New"
                )
        return super().create(vals_list)

    def action_start(self):
        """Move order to In Progress."""
        for rec in self:
            if rec.state != "order_placed":
                raise UserError("Only newly placed orders can be started.")
            rec.state = "in_progress"

    def action_ready(self):
        """Mark order as ready for pickup."""
        for rec in self:
            if rec.state != "in_progress":
                raise UserError("Only in-progress orders can be marked ready.")
            rec.state = "ready_for_pickup"

    def action_complete(self):
        """Complete the order."""
        for rec in self:
            if rec.state != "ready_for_pickup":
                raise UserError("Only orders ready for pickup can be completed.")
            rec.state = "completed"
            rec.completed_date = fields.Datetime.now()

    def action_cancel(self):
        """Cancel the order."""
        for rec in self:
            if rec.state in ("completed", "cancelled"):
                raise UserError("Cannot cancel a completed or already cancelled order.")
            rec.state = "cancelled"

    @api.constrains("line_ids")
    def _check_has_lines(self):
        for rec in self:
            if rec.state not in ("order_placed",) and not rec.line_ids:
                raise ValidationError("An order must have at least one line item.")


class GreenLightOrderLine(models.Model):
    _name = "greenlight.order.line"
    _description = "Pre-Order Line Item"

    order_id = fields.Many2one(
        "greenlight.order", required=True, ondelete="cascade",
    )
    product_id = fields.Many2one(
        "greenlight.product", required=True, ondelete="restrict",
    )
    quantity = fields.Integer(required=True, default=1)
    unit_price = fields.Monetary(currency_field="currency_id")
    subtotal = fields.Monetary(
        currency_field="currency_id", compute="_compute_subtotal", store=True,
    )
    currency_id = fields.Many2one(
        "res.currency", default=lambda self: self.env.company.currency_id,
    )

    @api.depends("quantity", "unit_price")
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.quantity * rec.unit_price

    @api.onchange("product_id")
    def _onchange_product_id(self):
        if self.product_id:
            self.unit_price = self.product_id.price
