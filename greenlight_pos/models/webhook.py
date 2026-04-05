import hashlib
import hmac
import json
import logging
import time

import requests

from odoo import models, fields, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class GreenLightWebhook(models.Model):
    _name = "greenlight.webhook"
    _description = "Outbound Webhook Configuration"
    _order = "name"

    name = fields.Char("Webhook Name", required=True)
    url = fields.Char("Endpoint URL", required=True)
    secret = fields.Char(
        "Signing Secret",
        help="HMAC-SHA256 secret for payload signing. Sent as X-Webhook-Signature header.",
    )
    event_types = fields.Text(
        "Event Types (JSON)",
        required=True,
        default='["sale.created"]',
        help='JSON array of event types, e.g., ["sale.created", "inventory.adjusted"].',
    )
    is_active = fields.Boolean("Active", default=True)
    delivery_ids = fields.One2many("greenlight.webhook.delivery", "webhook_id", string="Deliveries")
    delivery_count = fields.Integer(compute="_compute_delivery_count")
    last_delivery_at = fields.Datetime("Last Delivery", readonly=True)
    last_success = fields.Boolean("Last Delivery OK", readonly=True)

    @api.depends("delivery_ids")
    def _compute_delivery_count(self):
        for rec in self:
            rec.delivery_count = len(rec.delivery_ids)

    def _get_event_types_list(self):
        """Parse the event_types JSON field into a Python list."""
        self.ensure_one()
        try:
            result = json.loads(self.event_types or "[]")
            if not isinstance(result, list):
                return []
            return result
        except (json.JSONDecodeError, TypeError):
            return []

    def _sign_payload(self, payload_str):
        """Generate HMAC-SHA256 signature for the payload."""
        self.ensure_one()
        if not self.secret:
            return ""
        return hmac.new(
            self.secret.encode("utf-8"),
            payload_str.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

    def trigger(self, event_type, payload):
        """
        Fire this webhook for the given event type.
        Posts to the URL with HMAC-SHA256 signature and records delivery.

        :param event_type: str, e.g., "sale.created"
        :param payload: dict, the event payload
        """
        Delivery = self.env["greenlight.webhook.delivery"]
        for rec in self:
            if not rec.is_active:
                continue
            if event_type not in rec._get_event_types_list():
                continue

            payload_str = json.dumps(payload, default=str, ensure_ascii=False)
            signature = rec._sign_payload(payload_str)

            headers = {
                "Content-Type": "application/json",
                "X-Webhook-Event": event_type,
                "X-Webhook-Signature": f"sha256={signature}" if signature else "",
                "User-Agent": "GreenLightPOS/19.0",
            }

            start = time.time()
            response_status = 0
            response_body = ""
            success = False

            try:
                resp = requests.post(
                    rec.url,
                    data=payload_str,
                    headers=headers,
                    timeout=10,
                )
                response_status = resp.status_code
                response_body = resp.text[:5000]  # cap stored response
                success = 200 <= resp.status_code < 300
            except requests.RequestException as exc:
                response_body = str(exc)[:5000]
                _logger.warning(
                    "Webhook %s delivery failed for %s: %s",
                    rec.name, event_type, exc,
                )

            duration_ms = int((time.time() - start) * 1000)

            Delivery.sudo().create({
                "webhook_id": rec.id,
                "event_type": event_type,
                "payload": payload_str,
                "response_status": response_status,
                "response_body": response_body,
                "success": success,
                "duration_ms": duration_ms,
            })

            rec.last_delivery_at = fields.Datetime.now()
            rec.last_success = success

    @api.model
    def trigger_event(self, event_type, payload):
        """
        Class-level convenience: find all active webhooks subscribed to
        this event type and trigger them.

        Usage:
            self.env['greenlight.webhook'].trigger_event('sale.created', {...})
        """
        webhooks = self.search([("is_active", "=", True)])
        webhooks.trigger(event_type, payload)


class GreenLightWebhookDelivery(models.Model):
    _name = "greenlight.webhook.delivery"
    _description = "Webhook Delivery Log"
    _order = "create_date desc"

    webhook_id = fields.Many2one(
        "greenlight.webhook",
        required=True,
        ondelete="cascade",
        string="Webhook",
    )
    event_type = fields.Char("Event Type", required=True)
    payload = fields.Text("Request Payload")
    response_status = fields.Integer("HTTP Status")
    response_body = fields.Text("Response Body")
    success = fields.Boolean("Success")
    duration_ms = fields.Integer("Duration (ms)")
