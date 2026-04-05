import logging
import requests
from odoo import models, fields, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

METRC_SANDBOX_URL = "https://sandbox-api-ms.metrc.com"
METRC_PRODUCTION_URL = "https://api-ms.metrc.com"


class GreenLightMetrcConfig(models.Model):
    _name = "greenlight.metrc.config"
    _description = "Metrc API Configuration"
    _order = "facility_name"

    facility_license = fields.Char("Facility License", required=True)
    facility_name = fields.Char(required=True)
    api_key = fields.Char("Vendor API Key", required=True, groups="greenlight_pos.group_admin")
    user_key = fields.Char("User API Key", required=True, groups="greenlight_pos.group_admin")
    environment = fields.Selection(
        [("sandbox", "Sandbox"), ("production", "Production")],
        default="sandbox",
        required=True,
    )
    base_url = fields.Char(
        compute="_compute_base_url",
        store=True,
    )
    auto_sync = fields.Boolean("Auto-Sync Sales", default=False)
    sync_interval_minutes = fields.Integer(default=15)
    last_sync_at = fields.Datetime(readonly=True)
    is_active = fields.Boolean(default=True)

    sync_log_ids = fields.One2many("greenlight.metrc.sync.log", "config_id")

    @api.depends("environment")
    def _compute_base_url(self):
        for rec in self:
            rec.base_url = METRC_PRODUCTION_URL if rec.environment == "production" else METRC_SANDBOX_URL

    def _get_auth(self):
        """Return HTTP Basic Auth tuple for Metrc API."""
        self.ensure_one()
        return (self.api_key, self.user_key)

    def action_test_connection(self):
        """Test the Metrc API connection."""
        self.ensure_one()
        try:
            url = f"{self.base_url}/facilities/v2"
            resp = requests.get(url, auth=self._get_auth(), timeout=10)
            if resp.status_code == 200:
                return {
                    "type": "ir.actions.client",
                    "tag": "display_notification",
                    "params": {
                        "message": f"Connected to Metrc ({self.environment}). {len(resp.json())} facilities found.",
                        "type": "success",
                    },
                }
            else:
                raise UserError(f"Metrc returned HTTP {resp.status_code}: {resp.text[:200]}")
        except requests.RequestException as e:
            raise UserError(f"Connection failed: {e}") from e
