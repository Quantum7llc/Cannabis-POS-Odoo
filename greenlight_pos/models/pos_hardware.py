from odoo import models, fields, api


class GreenLightPOSStation(models.Model):
    _name = "greenlight.pos.station"
    _description = "POS Station / Register"
    _order = "name"

    name = fields.Char("Station Name", required=True)
    code = fields.Char(
        "Station Code",
        help="Short identifier, e.g., REG-01.",
    )
    location = fields.Char(
        "Location",
        help="Physical location within the dispensary.",
    )
    is_active = fields.Boolean("Active", default=True)
    device_ids = fields.One2many("greenlight.pos.device", "station_id", string="Devices")
    device_count = fields.Integer(compute="_compute_device_count", store=True)
    notes = fields.Text("Notes")

    @api.depends("device_ids")
    def _compute_device_count(self):
        for rec in self:
            rec.device_count = len(rec.device_ids)


class GreenLightPOSDevice(models.Model):
    _name = "greenlight.pos.device"
    _description = "POS Peripheral Device"
    _order = "station_id, device_type"

    name = fields.Char("Device Name", required=True)
    station_id = fields.Many2one(
        "greenlight.pos.station",
        required=True,
        ondelete="cascade",
        string="Station",
    )
    device_type = fields.Selection(
        [
            ("receipt_printer", "Receipt Printer"),
            ("label_printer", "Label Printer"),
            ("barcode_scanner", "Barcode Scanner"),
            ("cash_drawer", "Cash Drawer"),
            ("customer_display", "Customer Display"),
            ("scale", "Scale"),
        ],
        required=True,
        string="Device Type",
    )
    connection_type = fields.Selection(
        [
            ("network", "Network (TCP/IP)"),
            ("usb", "USB"),
            ("bluetooth", "Bluetooth"),
            ("serial", "Serial"),
        ],
        required=True,
        default="network",
        string="Connection Type",
    )
    ip_address = fields.Char("IP Address")
    port = fields.Integer("Port")
    serial_number = fields.Char("Serial Number")
    manufacturer = fields.Char("Manufacturer")
    model_name = fields.Char("Model")
    settings_json = fields.Text(
        "Settings (JSON)",
        help="Device-specific configuration as JSON.",
    )
    is_active = fields.Boolean("Active", default=True)
    last_seen = fields.Datetime("Last Seen", readonly=True)
    status = fields.Selection(
        [
            ("online", "Online"),
            ("offline", "Offline"),
            ("error", "Error"),
            ("unknown", "Unknown"),
        ],
        default="unknown",
        readonly=True,
    )
