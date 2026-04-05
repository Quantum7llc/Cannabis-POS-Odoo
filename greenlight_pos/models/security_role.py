from odoo import models, fields, api
from odoo.exceptions import UserError


class GreenLightSecurityRole(models.Model):
    _name = "greenlight.security.role"
    _description = "Security Role"
    _order = "name"

    name = fields.Char(required=True)
    description = fields.Text()
    is_system = fields.Boolean(
        "System Role",
        default=False,
        readonly=True,
        help="System roles cannot be deleted.",
    )
    is_active = fields.Boolean("Active", default=True)
    role_permission_ids = fields.One2many(
        "greenlight.role.permission", "role_id", string="Permissions",
    )
    permission_count = fields.Integer(
        compute="_compute_permission_count",
    )
    employee_ids = fields.One2many(
        "greenlight.employee", "security_role_id", string="Employees",
    )
    employee_count = fields.Integer(compute="_compute_employee_count")

    @api.depends("role_permission_ids")
    def _compute_permission_count(self):
        for rec in self:
            rec.permission_count = len(rec.role_permission_ids)

    @api.depends("employee_ids")
    def _compute_employee_count(self):
        for rec in self:
            rec.employee_count = len(rec.employee_ids)

    def unlink(self):
        for rec in self:
            if rec.is_system:
                raise UserError("System roles cannot be deleted.")
        return super().unlink()

    def action_view_permissions(self):
        """Open the role permissions for this role."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": f"Permissions: {self.name}",
            "res_model": "greenlight.role.permission",
            "view_mode": "list",
            "domain": [("role_id", "=", self.id)],
            "context": {"default_role_id": self.id},
        }

    def has_permission(self, permission_name):
        """Check if this role has a specific permission by code name."""
        self.ensure_one()
        return bool(self.role_permission_ids.filtered(
            lambda rp: rp.permission_id.name == permission_name
        ))


class GreenLightPermission(models.Model):
    _name = "greenlight.permission"
    _description = "Granular Permission"
    _order = "category, name"

    name = fields.Char("Permission Code", required=True, index=True)
    display_name_label = fields.Char("Display Name", required=True)
    category = fields.Selection(
        [
            ("sales", "Sales"),
            ("inventory", "Inventory"),
            ("customers", "Customers"),
            ("reports", "Reports"),
            ("settings", "Settings"),
            ("employees", "Employees"),
            ("compliance", "Compliance"),
        ],
        required=True,
        index=True,
    )
    description = fields.Text()

    def name_get(self):
        return [(rec.id, f"[{rec.category}] {rec.display_name_label}") for rec in self]


class GreenLightRolePermission(models.Model):
    _name = "greenlight.role.permission"
    _description = "Role-Permission Assignment"
    _order = "role_id, permission_id"

    role_id = fields.Many2one(
        "greenlight.security.role",
        required=True,
        ondelete="cascade",
    )
    permission_id = fields.Many2one(
        "greenlight.permission",
        required=True,
        ondelete="cascade",
    )
    permission_category = fields.Selection(
        related="permission_id.category", store=True, readonly=True,
    )
    permission_description = fields.Text(
        related="permission_id.description", readonly=True,
    )
