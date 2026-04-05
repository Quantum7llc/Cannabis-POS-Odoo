from odoo import models, fields


class GreenLightMetrcSyncLog(models.Model):
    _name = "greenlight.metrc.sync.log"
    _description = "Metrc API Sync Log"
    _order = "create_date desc"

    config_id = fields.Many2one("greenlight.metrc.config", required=True, index=True)
    direction = fields.Selection(
        [("outbound", "Outbound (POS→Metrc)"), ("inbound", "Inbound (Metrc→POS)")],
        default="outbound",
        required=True,
    )
    endpoint = fields.Char(required=True)
    method = fields.Selection(
        [("GET", "GET"), ("POST", "POST"), ("PUT", "PUT"), ("DELETE", "DELETE")],
        required=True,
    )
    request_body = fields.Text()
    response_status = fields.Integer()
    response_body = fields.Text()
    success = fields.Boolean(default=False)
    error_message = fields.Text()
    duration_ms = fields.Integer("Duration (ms)")

    transaction_id = fields.Many2one("greenlight.transaction")
    package_tag = fields.Char("Metrc Package Tag", size=24)
