from odoo import models, fields, api


class GreenLightAuditLog(models.Model):
    _name = "greenlight.audit.log"
    _description = "Audit Log"
    _order = "create_date desc"
    _rec_name = "action"

    action = fields.Selection(
        [
            ("create", "Create"),
            ("update", "Update"),
            ("delete", "Delete"),
            ("login", "Login"),
            ("logout", "Logout"),
            ("view", "View"),
            ("export", "Export"),
            ("void", "Void"),
            ("confirm", "Confirm"),
            ("refund", "Refund"),
            ("adjustment", "Inventory Adjustment"),
            ("pin_change", "PIN Change"),
            ("role_change", "Role Change"),
            ("settings_change", "Settings Change"),
        ],
        required=True,
        readonly=True,
    )
    resource_type = fields.Char("Resource Type", required=True, readonly=True, index=True)
    resource_id = fields.Integer("Resource ID", readonly=True)
    resource_name = fields.Char("Resource Name", readonly=True)
    employee_id = fields.Many2one(
        "greenlight.employee",
        string="Employee",
        readonly=True,
        ondelete="restrict",
    )
    ip_address = fields.Char("IP Address", readonly=True)
    details = fields.Text("Details (JSON)", readonly=True)
    is_phi_access = fields.Boolean(
        "PHI Access",
        readonly=True,
        help="Indicates access to Protected Health Information (patient medical data).",
    )

    @api.model
    def log_action(self, action, resource_type, resource_id=False,
                   resource_name=False, employee_id=False, ip_address=False,
                   details=False, is_phi_access=False):
        """Create an audit log entry. Called from controllers and model overrides."""
        return self.sudo().create({
            "action": action,
            "resource_type": resource_type,
            "resource_id": resource_id or 0,
            "resource_name": resource_name or "",
            "employee_id": employee_id,
            "ip_address": ip_address or "",
            "details": details or "",
            "is_phi_access": is_phi_access,
        })


class GreenLightChangeLog(models.Model):
    _name = "greenlight.change.log"
    _description = "Field Change Log"
    _order = "create_date desc"
    _rec_name = "display_name_computed"

    table_name = fields.Char("Model", required=True, readonly=True, index=True)
    record_id = fields.Integer("Record ID", required=True, readonly=True)
    record_name = fields.Char("Record Name", readonly=True)
    field_name = fields.Char("Field", required=True, readonly=True)
    old_value = fields.Text("Old Value", readonly=True)
    new_value = fields.Text("New Value", readonly=True)
    changed_by = fields.Many2one(
        "greenlight.employee",
        string="Changed By",
        readonly=True,
        ondelete="restrict",
    )
    display_name_computed = fields.Char(
        "Description", compute="_compute_display_name_computed", store=True,
    )

    @api.depends("table_name", "field_name", "record_id")
    def _compute_display_name_computed(self):
        for rec in self:
            rec.display_name_computed = (
                f"{rec.table_name}#{rec.record_id} - {rec.field_name}"
            )

    @api.model
    def log_change(self, table_name, record_id, field_name, old_value,
                   new_value, changed_by=False, record_name=False):
        """Log a field-level change."""
        return self.sudo().create({
            "table_name": table_name,
            "record_id": record_id,
            "record_name": record_name or "",
            "field_name": field_name,
            "old_value": str(old_value) if old_value is not None else "",
            "new_value": str(new_value) if new_value is not None else "",
            "changed_by": changed_by,
        })
