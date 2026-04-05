from odoo import models, fields, api
from odoo.exceptions import ValidationError


class GreenLightPromotion(models.Model):
    _name = "greenlight.promotion"
    _description = "Promotion / Discount"
    _inherit = ["mail.thread"]
    _order = "start_date desc"

    name = fields.Char(required=True, tracking=True)
    description = fields.Text()

    discount_type = fields.Selection(
        [
            ("percentage", "Percentage Off"),
            ("fixed", "Fixed Amount Off"),
        ],
        required=True,
        default="percentage",
        tracking=True,
    )
    discount_value = fields.Float(
        "Discount Value",
        required=True,
        digits=(10, 2),
        help="Percentage (e.g. 10 for 10%) or fixed dollar amount depending on discount type.",
    )

    # Scope — optional: applies to a specific product or category, or store-wide if both blank
    product_id = fields.Many2one(
        "greenlight.product", string="Specific Product", ondelete="cascade",
    )
    category_id = fields.Many2one(
        "greenlight.product.category", string="Product Category", ondelete="cascade",
    )
    scope_display = fields.Char(
        "Applies To", compute="_compute_scope_display",
    )

    # Schedule
    start_date = fields.Datetime("Start Date", required=True, default=fields.Datetime.now)
    end_date = fields.Datetime("End Date", required=True)

    # Limits
    max_uses = fields.Integer(
        "Max Uses", default=0,
        help="Maximum number of times this promotion can be applied (0 = unlimited).",
    )
    current_uses = fields.Integer("Current Uses", default=0, readonly=True)

    # Display
    display_on_pos = fields.Boolean(
        "Show on POS Screen", default=True,
        help="When enabled, budtenders see this promotion highlighted on the POS interface.",
    )
    is_active = fields.Boolean("Active", default=True, tracking=True)

    # Computed
    is_expired = fields.Boolean(compute="_compute_is_expired", store=True)
    is_maxed = fields.Boolean(compute="_compute_is_maxed", store=True)
    is_usable = fields.Boolean(
        "Currently Usable", compute="_compute_is_usable", store=True,
    )

    @api.depends("product_id", "category_id")
    def _compute_scope_display(self):
        for rec in self:
            if rec.product_id:
                rec.scope_display = f"Product: {rec.product_id.name}"
            elif rec.category_id:
                rec.scope_display = f"Category: {rec.category_id.name}"
            else:
                rec.scope_display = "Store-Wide"

    @api.depends("end_date")
    def _compute_is_expired(self):
        now = fields.Datetime.now()
        for rec in self:
            rec.is_expired = rec.end_date < now if rec.end_date else False

    @api.depends("max_uses", "current_uses")
    def _compute_is_maxed(self):
        for rec in self:
            rec.is_maxed = rec.max_uses > 0 and rec.current_uses >= rec.max_uses

    @api.depends("is_active", "is_expired", "is_maxed")
    def _compute_is_usable(self):
        for rec in self:
            rec.is_usable = rec.is_active and not rec.is_expired and not rec.is_maxed

    @api.constrains("discount_type", "discount_value")
    def _check_discount_value(self):
        for rec in self:
            if rec.discount_value <= 0:
                raise ValidationError("Discount value must be greater than zero.")
            if rec.discount_type == "percentage" and rec.discount_value > 100:
                raise ValidationError("Percentage discount cannot exceed 100%.")

    @api.constrains("start_date", "end_date")
    def _check_date_range(self):
        for rec in self:
            if rec.start_date and rec.end_date and rec.end_date <= rec.start_date:
                raise ValidationError("End date must be after start date.")

    @api.constrains("product_id", "category_id")
    def _check_scope_exclusive(self):
        """A promotion targets a product, a category, or the whole store -- not both."""
        for rec in self:
            if rec.product_id and rec.category_id:
                raise ValidationError(
                    "A promotion can target a specific product or a category, not both."
                )

    def action_increment_use(self):
        """Record one use of this promotion (called from transaction confirm)."""
        for rec in self:
            rec.current_uses += 1

    def action_activate(self):
        for rec in self:
            rec.is_active = True

    def action_deactivate(self):
        for rec in self:
            rec.is_active = False

    @api.model
    def get_active_promotions(self):
        """Return promotions currently usable on the POS."""
        now = fields.Datetime.now()
        promos = self.search([
            ("is_active", "=", True),
            ("start_date", "<=", now),
            ("end_date", ">=", now),
            ("display_on_pos", "=", True),
        ])
        return promos.filtered(
            lambda p: p.max_uses == 0 or p.current_uses < p.max_uses
        )

    @api.model
    def get_applicable_promotions(self, product_id=None, category_id=None):
        """Return promotions applicable to a given product/category."""
        now = fields.Datetime.now()
        domain = [
            ("is_active", "=", True),
            ("start_date", "<=", now),
            ("end_date", ">=", now),
        ]
        promos = self.search(domain)
        result = self.env["greenlight.promotion"]
        for promo in promos:
            if promo.max_uses > 0 and promo.current_uses >= promo.max_uses:
                continue
            # Store-wide promotions apply to everything
            if not promo.product_id and not promo.category_id:
                result |= promo
            elif promo.product_id and promo.product_id.id == product_id:
                result |= promo
            elif promo.category_id and promo.category_id.id == category_id:
                result |= promo
        return result
