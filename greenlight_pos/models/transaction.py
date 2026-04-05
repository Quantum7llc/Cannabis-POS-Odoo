from odoo import models, fields, api
from odoo.exceptions import UserError


class GreenLightTransaction(models.Model):
    _name = "greenlight.transaction"
    _description = "POS Transaction"
    _inherit = ["mail.thread"]
    _order = "create_date desc"

    name = fields.Char("Reference", readonly=True, default="New")
    customer_id = fields.Many2one("greenlight.customer", required=True, tracking=True, ondelete="restrict")
    employee_id = fields.Many2one("greenlight.employee", required=True, tracking=True, ondelete="restrict")
    line_ids = fields.One2many("greenlight.transaction.line", "transaction_id")

    # Totals (stored in cents for precision, displayed as currency)
    subtotal = fields.Monetary(currency_field="currency_id", compute="_compute_totals", store=True)
    tax_amount = fields.Monetary(currency_field="currency_id", compute="_compute_totals", store=True)
    total = fields.Monetary(currency_field="currency_id", compute="_compute_totals", store=True)
    cogs_total = fields.Monetary("COGS Total", currency_field="currency_id", compute="_compute_totals", store=True)
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)

    payment_method = fields.Selection(
        [("cash", "Cash"), ("debit", "Debit"), ("card", "Card")],
        required=True,
        default="cash",
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("voided", "Voided"),
        ],
        default="draft",
        tracking=True,
    )

    # Metrc sync (populated by greenlight_metrc module)
    metrc_receipt_id = fields.Char("Metrc Receipt ID", readonly=True)
    metrc_sync_status = fields.Selection(
        [
            ("pending", "Pending"),
            ("synced", "Synced"),
            ("failed", "Failed"),
            ("skipped", "Skipped"),
        ],
        default="pending",
        readonly=True,
    )

    @api.depends("line_ids.subtotal", "line_ids.tax", "line_ids.cogs")
    def _compute_totals(self):
        for rec in self:
            rec.subtotal = sum(rec.line_ids.mapped("subtotal"))
            rec.tax_amount = sum(rec.line_ids.mapped("tax"))
            rec.total = rec.subtotal + rec.tax_amount
            rec.cogs_total = sum(rec.line_ids.mapped("cogs"))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code("greenlight.transaction") or "New"
        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
            if rec.state != "draft":
                raise UserError("Only draft transactions can be confirmed.")
            for line in rec.line_ids:
                self.env.cr.execute(
                    "UPDATE greenlight_product SET inventory_count = inventory_count - %s WHERE id = %s",
                    (line.quantity, line.product_id.id),
                )
                line.product_id.invalidate_recordset(["inventory_count"])
            rec.state = "confirmed"

    def action_void(self):
        for rec in self:
            if rec.state != "confirmed":
                raise UserError("Only confirmed transactions can be voided.")
            for line in rec.line_ids:
                self.env.cr.execute(
                    "UPDATE greenlight_product SET inventory_count = inventory_count + %s WHERE id = %s",
                    (line.quantity, line.product_id.id),
                )
                line.product_id.invalidate_recordset(["inventory_count"])
            rec.state = "voided"


class GreenLightTransactionLine(models.Model):
    _name = "greenlight.transaction.line"
    _description = "Transaction Line Item"

    transaction_id = fields.Many2one("greenlight.transaction", required=True, ondelete="cascade")
    product_id = fields.Many2one("greenlight.product", required=True)
    quantity = fields.Integer(required=True, default=1)
    unit_price = fields.Monetary(currency_field="currency_id")
    subtotal = fields.Monetary(currency_field="currency_id", compute="_compute_amounts", store=True)
    tax = fields.Monetary(currency_field="currency_id", compute="_compute_amounts", store=True)
    cogs = fields.Monetary("COGS", currency_field="currency_id", compute="_compute_amounts", store=True)
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)

    # MMCEU tracking
    weight_grams = fields.Float(related="product_id.weight_grams", readonly=True)
    cannabis_type = fields.Selection(related="product_id.cannabis_type", readonly=True)

    @api.depends("quantity", "unit_price", "product_id.cost")
    def _compute_amounts(self):
        tax_rate = self.env["greenlight.settings"].get_tax_rate()
        for rec in self:
            rec.subtotal = rec.quantity * rec.unit_price
            rec.tax = rec.subtotal * tax_rate
            rec.cogs = rec.quantity * (rec.product_id.cost or 0.0)
