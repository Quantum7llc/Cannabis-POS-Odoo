from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class GreenLightLocation(models.Model):
    _name = "greenlight.location"
    _description = "Dispensary Location"
    _inherit = ["mail.thread"]
    _order = "name"

    name = fields.Char(required=True, tracking=True, index=True)
    address = fields.Char()
    city = fields.Char()
    state = fields.Char(default="MS")
    zip = fields.Char("ZIP Code", size=10)
    phone = fields.Char(size=20)
    is_active = fields.Boolean(default=True, tracking=True)

    room_ids = fields.One2many("greenlight.room", "location_id", string="Rooms")
    room_count = fields.Integer(compute="_compute_room_count")
    inventory_ids = fields.One2many("greenlight.location.inventory", "location_id", string="Inventory")
    inventory_count = fields.Integer("Products Stocked", compute="_compute_inventory_count")

    @api.depends("room_ids")
    def _compute_room_count(self):
        for rec in self:
            rec.room_count = len(rec.room_ids)

    @api.depends("inventory_ids")
    def _compute_inventory_count(self):
        for rec in self:
            rec.inventory_count = len(rec.inventory_ids)

    @api.constrains("name")
    def _check_name_unique(self):
        for rec in self:
            if self.search_count([("name", "=ilike", rec.name), ("id", "!=", rec.id)]):
                raise ValidationError("Location name must be unique.")

    def name_get(self):
        return [(rec.id, rec.name) for rec in self]


class GreenLightRoom(models.Model):
    _name = "greenlight.room"
    _description = "Room within a Location"
    _order = "location_id, name"

    name = fields.Char(required=True)
    room_type = fields.Selection(
        [
            ("dispensary", "Dispensary Floor"),
            ("safe", "Safe / Vault"),
            ("storage", "Storage"),
            ("processing", "Processing"),
        ],
        required=True,
        default="storage",
    )
    location_id = fields.Many2one(
        "greenlight.location", required=True, ondelete="restrict", index=True,
    )
    inventory_ids = fields.One2many("greenlight.location.inventory", "room_id", string="Inventory")

    def name_get(self):
        return [(rec.id, f"{rec.location_id.name} / {rec.name}") for rec in self]


class GreenLightLocationInventory(models.Model):
    _name = "greenlight.location.inventory"
    _description = "Per-Location Product Stock"
    _order = "location_id, product_id"

    product_id = fields.Many2one(
        "greenlight.product", required=True, ondelete="cascade", index=True,
    )
    location_id = fields.Many2one(
        "greenlight.location", required=True, ondelete="cascade", index=True,
    )
    room_id = fields.Many2one(
        "greenlight.room", ondelete="restrict",
        domain="[('location_id', '=', location_id)]",
        help="Optional: specific room within the location.",
    )
    quantity = fields.Float("Qty on Hand", digits=(12, 3), default=0.0)

    @api.constrains("product_id", "location_id", "room_id")
    def _check_unique_product_location_room(self):
        for rec in self:
            domain = [
                ("product_id", "=", rec.product_id.id),
                ("location_id", "=", rec.location_id.id),
                ("room_id", "=", rec.room_id.id if rec.room_id else False),
                ("id", "!=", rec.id),
            ]
            if self.search_count(domain):
                raise ValidationError(
                    "A stock record already exists for this product/location/room combination."
                )

    @api.constrains("quantity")
    def _check_quantity_non_negative(self):
        for rec in self:
            if rec.quantity < 0:
                raise ValidationError("Stock quantity cannot be negative.")

    def name_get(self):
        result = []
        for rec in self:
            room_part = f" ({rec.room_id.name})" if rec.room_id else ""
            result.append((rec.id, f"{rec.product_id.name} @ {rec.location_id.name}{room_part}"))
        return result


class GreenLightStockTransfer(models.Model):
    _name = "greenlight.stock.transfer"
    _description = "Inter-Location Stock Transfer"
    _inherit = ["mail.thread"]
    _order = "create_date desc"

    name = fields.Char("Reference", readonly=True, default="New")
    source_location_id = fields.Many2one(
        "greenlight.location", "Source Location",
        required=True, ondelete="restrict", tracking=True,
    )
    dest_location_id = fields.Many2one(
        "greenlight.location", "Destination Location",
        required=True, ondelete="restrict", tracking=True,
    )
    employee_id = fields.Many2one(
        "greenlight.employee", "Transferred By",
        required=True, ondelete="restrict", tracking=True,
    )
    metrc_manifest_id = fields.Char("Metrc Manifest #", size=50, tracking=True)

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("received", "Received"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        tracking=True,
    )

    line_ids = fields.One2many("greenlight.stock.transfer.line", "transfer_id", string="Transfer Lines")
    line_count = fields.Integer(compute="_compute_line_count")

    confirmed_at = fields.Datetime(readonly=True)
    received_at = fields.Datetime(readonly=True)
    notes = fields.Text()

    @api.depends("line_ids")
    def _compute_line_count(self):
        for rec in self:
            rec.line_count = len(rec.line_ids)

    @api.constrains("source_location_id", "dest_location_id")
    def _check_different_locations(self):
        for rec in self:
            if rec.source_location_id == rec.dest_location_id:
                raise ValidationError("Source and destination locations must be different.")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code("greenlight.stock.transfer") or "New"
        return super().create(vals_list)

    def action_confirm(self):
        """Validate stock availability and deduct from source location."""
        for rec in self:
            if rec.state != "draft":
                raise UserError("Only draft transfers can be confirmed.")
            if not rec.line_ids:
                raise UserError("Cannot confirm a transfer with no lines.")

            # Validate all lines have stock before deducting anything
            for line in rec.line_ids:
                if line.quantity <= 0:
                    raise UserError(f"Quantity must be positive for {line.product_id.name}.")

                inv = self.env["greenlight.location.inventory"].search([
                    ("product_id", "=", line.product_id.id),
                    ("location_id", "=", rec.source_location_id.id),
                ], limit=1)
                if not inv or inv.quantity < line.quantity:
                    available = inv.quantity if inv else 0.0
                    raise UserError(
                        f"Insufficient stock for {line.product_id.name} "
                        f"at {rec.source_location_id.name}. "
                        f"Available: {available}, Requested: {line.quantity}"
                    )

            # Deduct from source atomically using SQL to prevent races
            for line in rec.line_ids:
                self.env.cr.execute(
                    """
                    UPDATE greenlight_location_inventory
                       SET quantity = quantity - %s
                     WHERE product_id = %s
                       AND location_id = %s
                       AND quantity >= %s
                    RETURNING id
                    """,
                    (line.quantity, line.product_id.id, rec.source_location_id.id, line.quantity),
                )
                row = self.env.cr.fetchone()
                if not row:
                    raise UserError(
                        f"Stock for {line.product_id.name} changed during confirmation. "
                        f"Please try again."
                    )
                # Invalidate ORM cache
                self.env["greenlight.location.inventory"].browse(row[0]).invalidate_recordset(["quantity"])

            rec.state = "confirmed"
            rec.confirmed_at = fields.Datetime.now()

    def action_receive(self):
        """Credit destination location inventory."""
        for rec in self:
            if rec.state != "confirmed":
                raise UserError("Only confirmed transfers can be received.")

            for line in rec.line_ids:
                # Find or create destination inventory record
                inv = self.env["greenlight.location.inventory"].search([
                    ("product_id", "=", line.product_id.id),
                    ("location_id", "=", rec.dest_location_id.id),
                ], limit=1)

                if inv:
                    # Atomic add via SQL
                    self.env.cr.execute(
                        """
                        UPDATE greenlight_location_inventory
                           SET quantity = quantity + %s
                         WHERE id = %s
                        """,
                        (line.quantity, inv.id),
                    )
                    inv.invalidate_recordset(["quantity"])
                else:
                    self.env["greenlight.location.inventory"].create({
                        "product_id": line.product_id.id,
                        "location_id": rec.dest_location_id.id,
                        "quantity": line.quantity,
                    })

            rec.state = "received"
            rec.received_at = fields.Datetime.now()

    def action_cancel(self):
        """Cancel a transfer. If confirmed, reverse the source deduction."""
        for rec in self:
            if rec.state not in ("draft", "confirmed"):
                raise UserError("Only draft or confirmed transfers can be cancelled.")

            if rec.state == "confirmed":
                # Reverse the deduction — add stock back to source
                for line in rec.line_ids:
                    inv = self.env["greenlight.location.inventory"].search([
                        ("product_id", "=", line.product_id.id),
                        ("location_id", "=", rec.source_location_id.id),
                    ], limit=1)
                    if inv:
                        self.env.cr.execute(
                            """
                            UPDATE greenlight_location_inventory
                               SET quantity = quantity + %s
                             WHERE id = %s
                            """,
                            (line.quantity, inv.id),
                        )
                        inv.invalidate_recordset(["quantity"])
                    else:
                        self.env["greenlight.location.inventory"].create({
                            "product_id": line.product_id.id,
                            "location_id": rec.source_location_id.id,
                            "quantity": line.quantity,
                        })

            rec.state = "cancelled"


class GreenLightStockTransferLine(models.Model):
    _name = "greenlight.stock.transfer.line"
    _description = "Stock Transfer Line"

    transfer_id = fields.Many2one(
        "greenlight.stock.transfer", required=True, ondelete="cascade",
    )
    product_id = fields.Many2one(
        "greenlight.product", required=True, ondelete="restrict",
    )
    quantity = fields.Float(required=True, digits=(12, 3))

    @api.constrains("quantity")
    def _check_positive_quantity(self):
        for rec in self:
            if rec.quantity <= 0:
                raise ValidationError("Transfer quantity must be greater than zero.")
