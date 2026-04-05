from odoo import models, fields, api
from odoo.exceptions import ValidationError
import hashlib


class GreenLightEmployee(models.Model):
    _name = "greenlight.employee"
    _description = "Dispensary Employee"
    _inherit = ["mail.thread"]
    _order = "name"

    name = fields.Char(required=True, tracking=True)
    pin_hash = fields.Char("PIN Hash", required=True)
    role = fields.Selection(
        [
            ("budtender", "Budtender"),
            ("manager", "Manager"),
            ("admin", "Admin"),
        ],
        required=True,
        default="budtender",
        tracking=True,
    )
    is_active = fields.Boolean(default=True, tracking=True)

    # MFA
    mfa_enabled = fields.Boolean("MFA Enabled", default=False)
    totp_secret = fields.Char("TOTP Secret")

    # Shift tracking
    current_shift_id = fields.Many2one("greenlight.shift", "Current Shift", readonly=True)
    transaction_ids = fields.One2many("greenlight.transaction", "employee_id")

    def set_pin(self, pin):
        """Hash and store a 4-digit PIN."""
        self.ensure_one()
        if not pin or len(pin) != 4 or not pin.isdigit():
            raise ValidationError("PIN must be exactly 4 digits.")
        self.pin_hash = hashlib.sha256(pin.encode()).hexdigest()

    def verify_pin(self, pin):
        """Verify a PIN against stored hash."""
        self.ensure_one()
        return self.pin_hash == hashlib.sha256(pin.encode()).hexdigest()


class GreenLightShift(models.Model):
    _name = "greenlight.shift"
    _description = "Employee Shift"
    _order = "clock_in desc"

    employee_id = fields.Many2one("greenlight.employee", required=True)
    clock_in = fields.Datetime(required=True, default=fields.Datetime.now)
    clock_out = fields.Datetime()
    is_open = fields.Boolean(compute="_compute_is_open", store=True)

    @api.depends("clock_out")
    def _compute_is_open(self):
        for rec in self:
            rec.is_open = not rec.clock_out
