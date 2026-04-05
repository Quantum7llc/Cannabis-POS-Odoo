from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class GreenLightCustomerQueue(models.Model):
    _name = "greenlight.customer.queue"
    _description = "Customer Check-In Queue"
    _inherit = ["mail.thread"]
    _order = "check_in_time asc"
    _rec_name = "display_name"

    customer_id = fields.Many2one(
        "greenlight.customer", required=True, tracking=True, ondelete="restrict",
    )
    display_name = fields.Char(compute="_compute_display_name", store=True)

    state = fields.Selection(
        [
            ("waiting", "Waiting"),
            ("being_served", "Being Served"),
            ("completed", "Completed"),
        ],
        default="waiting",
        required=True,
        tracking=True,
    )

    served_by_id = fields.Many2one(
        "greenlight.employee", string="Served By", tracking=True, ondelete="restrict",
    )
    check_in_time = fields.Datetime(
        "Check-In Time", required=True, default=fields.Datetime.now,
    )
    served_time = fields.Datetime("Service Started", readonly=True)
    completed_time = fields.Datetime("Completed At", readonly=True)

    wait_minutes = fields.Float(
        "Wait (min)", compute="_compute_wait_minutes", store=True,
    )
    notes = fields.Text("Notes")

    @api.depends("customer_id", "check_in_time")
    def _compute_display_name(self):
        for rec in self:
            customer_name = rec.customer_id.full_name or "Unknown"
            time_str = rec.check_in_time.strftime("%H:%M") if rec.check_in_time else ""
            rec.display_name = f"{customer_name} ({time_str})"

    @api.depends("check_in_time", "served_time")
    def _compute_wait_minutes(self):
        now = fields.Datetime.now()
        for rec in self:
            if not rec.check_in_time:
                rec.wait_minutes = 0.0
                continue
            end = rec.served_time or now
            delta = end - rec.check_in_time
            rec.wait_minutes = round(delta.total_seconds() / 60.0, 1)

    @api.constrains("customer_id", "state")
    def _check_no_duplicate_active(self):
        """Prevent a customer from being in the queue twice while active."""
        for rec in self:
            if rec.state in ("waiting", "being_served"):
                existing = self.search([
                    ("customer_id", "=", rec.customer_id.id),
                    ("state", "in", ["waiting", "being_served"]),
                    ("id", "!=", rec.id),
                ])
                if existing:
                    raise ValidationError(
                        f"{rec.customer_id.full_name} is already in the queue."
                    )

    def action_start_service(self):
        """Begin serving this customer."""
        for rec in self:
            if rec.state != "waiting":
                raise UserError("Only waiting customers can be served.")
            rec.state = "being_served"
            rec.served_time = fields.Datetime.now()
            if not rec.served_by_id:
                # Auto-assign the current employee if we can find one
                employee = self.env["greenlight.employee"].search(
                    [("is_active", "=", True)], limit=1,
                )
                if employee:
                    rec.served_by_id = employee.id

    def action_complete_service(self):
        """Mark service as completed."""
        for rec in self:
            if rec.state != "being_served":
                raise UserError("Only customers being served can be completed.")
            rec.state = "completed"
            rec.completed_time = fields.Datetime.now()

    def action_reset_to_waiting(self):
        """Reset a customer back to waiting (e.g., budtender had to step away)."""
        for rec in self:
            if rec.state != "being_served":
                raise UserError("Only customers being served can be reset to waiting.")
            rec.state = "waiting"
            rec.served_time = False
            rec.served_by_id = False
