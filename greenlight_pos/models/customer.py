from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class GreenLightCustomer(models.Model):
    _name = "greenlight.customer"
    _description = "Cannabis Dispensary Patient/Customer"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "last_name, first_name"

    first_name = fields.Char(required=True, tracking=True)
    last_name = fields.Char(required=True, tracking=True)
    display_name = fields.Char(compute="_compute_display_name", store=True)
    dob = fields.Date("Date of Birth", required=True)
    age = fields.Integer(compute="_compute_age")

    # ID verification
    id_number = fields.Char("ID Number", required=True, index=True)
    id_state = fields.Char("ID State", required=True, size=2)
    id_expiry = fields.Date("ID Expiration", required=True)
    id_expired = fields.Boolean(compute="_compute_id_expired")

    # Medical card
    medical_card_number = fields.Char("Medical Card #")
    medical_card_expiry = fields.Date("Card Expiration")
    recommending_physician = fields.Char("Recommending Physician")

    # Contact
    phone = fields.Char()
    email = fields.Char()
    street = fields.Char()
    city = fields.Char()
    state = fields.Char(size=2)
    zip_code = fields.Char(size=10)

    # Loyalty
    loyalty_points = fields.Integer(default=0)

    # Relationships
    transaction_ids = fields.One2many("greenlight.transaction", "customer_id")
    transaction_count = fields.Integer(compute="_compute_transaction_count")

    is_active = fields.Boolean(default=True)
    notes = fields.Text()

    _sql_constraints = [
        ("id_number_uniq", "unique(id_number)", "A customer with this ID number already exists."),
    ]

    @api.depends("first_name", "last_name")
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.first_name} {rec.last_name}" if rec.first_name and rec.last_name else ""

    @api.depends("dob")
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.dob:
                rec.age = today.year - rec.dob.year - ((today.month, today.day) < (rec.dob.month, rec.dob.day))
            else:
                rec.age = 0

    @api.depends("id_expiry")
    def _compute_id_expired(self):
        today = date.today()
        for rec in self:
            rec.id_expired = rec.id_expiry < today if rec.id_expiry else True

    @api.depends("transaction_ids")
    def _compute_transaction_count(self):
        for rec in self:
            rec.transaction_count = len(rec.transaction_ids)

    @api.constrains("dob")
    def _check_age(self):
        today = date.today()
        for rec in self:
            if rec.dob:
                age = today.year - rec.dob.year - ((today.month, today.day) < (rec.dob.month, rec.dob.day))
                if age < 18:
                    raise ValidationError("Customer must be at least 18 years old.")
