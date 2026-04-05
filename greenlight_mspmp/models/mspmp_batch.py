import logging
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

# ASAP 4.2 segment identifiers
# TH = Transaction Header, TP = Transaction Patient, TD = Transaction Drug,
# TP2 = Transaction Prescriber, PHA = Pharmacy Header, TT = Transaction Trailer
ASAP_VERSION = "4.2"
SEGMENT_DELIM = "\n"
FIELD_DELIM = "*"


def _safe(val, maxlen=None):
    """Sanitize a value for ASAP 4.2 output — strip, uppercase, truncate."""
    s = str(val or "").strip().upper()
    if maxlen:
        s = s[:maxlen]
    return s


class GreenLightMSPMPBatch(models.Model):
    _name = "greenlight.mspmp.batch"
    _description = "MSPMP Daily Batch Report"
    _order = "report_date desc"

    report_date = fields.Date(required=True, default=fields.Date.today)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("generated", "Generated"),
            ("uploaded", "Uploaded"),
            ("failed", "Failed"),
        ],
        string="Status",
        default="draft",
    )
    transaction_count = fields.Integer(readonly=True)
    file_content = fields.Text("ASAP 4.2 File Content", readonly=True)
    file_name = fields.Char(readonly=True)
    upload_response = fields.Text(readonly=True)
    error_message = fields.Text(readonly=True)

    # SFTP config (should come from system parameters in production)
    sftp_host = fields.Char("SFTP Host")
    sftp_port = fields.Integer(default=22)
    sftp_user = fields.Char("SFTP Username")
    sftp_password = fields.Char("SFTP Password", groups="greenlight_pos.group_admin")

    # Pharmacy / dispensary info for the batch header
    pharmacy_name = fields.Char("Dispensary Name")
    pharmacy_dea = fields.Char("DEA Number")
    pharmacy_license = fields.Char("State License #")
    pharmacy_npi = fields.Char("NPI")
    pharmacy_address = fields.Char("Address")
    pharmacy_city = fields.Char("City")
    pharmacy_state = fields.Char("State", default="MS", size=2)
    pharmacy_zip = fields.Char("ZIP", size=10)
    pharmacy_phone = fields.Char("Phone")

    def _build_pharmacy_header(self):
        """PHA segment — pharmacy/dispensary identification."""
        self.ensure_one()
        fields_list = [
            "PHA",
            _safe(self.pharmacy_dea, 9),          # DEA number
            _safe(self.pharmacy_license, 20),      # State license
            _safe(self.pharmacy_npi, 10),           # NPI
            _safe(self.pharmacy_name, 35),          # Pharmacy name
            _safe(self.pharmacy_address, 30),       # Address
            _safe(self.pharmacy_city, 20),          # City
            _safe(self.pharmacy_state, 2),          # State
            _safe(self.pharmacy_zip, 10),           # ZIP
            _safe(self.pharmacy_phone, 10),         # Phone
        ]
        return FIELD_DELIM.join(fields_list)

    def _build_transaction_segments(self, transaction):
        """Build TH + TP + TD segments for a single transaction."""
        customer = transaction.customer_id
        employee = transaction.employee_id
        txn_date = transaction.create_date

        segments = []

        # TH — Transaction Header
        th = FIELD_DELIM.join([
            "TH",
            _safe(transaction.name, 20),                        # Rx number / reference
            _safe(txn_date.strftime("%Y%m%d") if txn_date else "", 8),  # Date dispensed
            _safe(txn_date.strftime("%Y%m%d") if txn_date else "", 8),  # Date written
            "01",                                                # New Rx indicator
            "",                                                  # Refill number
            _safe(transaction.payment_method, 2),               # Payment type
        ])
        segments.append(th)

        # TP — Transaction Patient
        tp = FIELD_DELIM.join([
            "TP",
            _safe(customer.last_name, 35),
            _safe(customer.first_name, 35),
            "",                                                  # Middle name
            _safe(customer.street, 30),
            _safe(customer.city, 20),
            _safe(customer.state, 2),
            _safe(customer.zip_code, 10),
            _safe(customer.dob.strftime("%Y%m%d") if customer.dob else "", 8),
            "01",                                                # ID qualifier (01 = state ID)
            _safe(customer.id_number, 20),
            _safe(customer.id_state, 2),
        ])
        segments.append(tp)

        # TD — Transaction Drug (one per line item)
        for line in transaction.line_ids:
            product = line.product_id
            td = FIELD_DELIM.join([
                "TD",
                _safe(product.sku, 20),                         # Product ID / NDC
                _safe(product.name, 40),                        # Product name
                str(line.quantity),                              # Quantity dispensed
                "01",                                           # Days supply
                _safe(product.cannabis_type, 15),               # Compound code / type
                f"{product.thc_percentage:.1f}",                # Strength (THC %)
                "EA",                                           # Unit of measure
                _safe(employee.name, 35),                       # Dispensing pharmacist/budtender
            ])
            segments.append(td)

        return segments

    def _build_file_trailer(self, txn_count, segment_count):
        """TT — file trailer with counts."""
        return FIELD_DELIM.join([
            "TT",
            str(txn_count),
            str(segment_count),
        ])

    def action_generate(self):
        """Generate ASAP 4.2 formatted batch file for the report date."""
        self.ensure_one()
        if self.state not in ("draft", "failed"):
            raise UserError("Can only generate from draft or failed state.")

        next_day = self.report_date + timedelta(days=1)
        transactions = self.env["greenlight.transaction"].search([
            ("state", "=", "confirmed"),
            ("create_date", ">=", f"{self.report_date} 00:00:00"),
            ("create_date", "<", f"{next_day} 00:00:00"),
        ])

        if not transactions:
            raise UserError(f"No confirmed transactions found for {self.report_date}.")

        # Build ASAP 4.2 content
        all_segments = []

        # File header
        fh = FIELD_DELIM.join([
            "FH",
            ASAP_VERSION,
            self.report_date.strftime("%Y%m%d"),
            _safe(self.pharmacy_name or "GREEN LIGHT DISPENSARY", 35),
        ])
        all_segments.append(fh)

        # Pharmacy header
        all_segments.append(self._build_pharmacy_header())

        # Transaction segments
        for txn in transactions:
            all_segments.extend(self._build_transaction_segments(txn))

        # File trailer
        all_segments.append(self._build_file_trailer(len(transactions), len(all_segments) + 1))

        file_content = SEGMENT_DELIM.join(all_segments)

        self.write({
            "state": "generated",
            "transaction_count": len(transactions),
            "file_content": file_content,
            "file_name": f"MSPMP_{self.report_date.strftime('%Y%m%d')}.dat",
            "error_message": False,
        })

        _logger.info(
            "MSPMP batch generated: %s transactions, %s segments, date=%s",
            len(transactions), len(all_segments), self.report_date,
        )

    def action_upload(self):
        """Upload generated batch file via SFTP to PMP Clearinghouse."""
        self.ensure_one()
        if self.state != "generated":
            raise UserError("Must generate the batch file before uploading.")

        if not all([self.sftp_host, self.sftp_user, self.sftp_password]):
            raise UserError(
                "SFTP credentials are incomplete. "
                "Set Host, Username, and Password before uploading."
            )

        try:
            import paramiko
        except ImportError:
            raise UserError(
                "The 'paramiko' Python package is required for SFTP upload. "
                "Install it with: pip install paramiko"
            ) from None

        transport = None
        sftp = None
        try:
            transport = paramiko.Transport((self.sftp_host, self.sftp_port or 22))
            transport.connect(username=self.sftp_user, password=self.sftp_password)
            sftp = paramiko.SFTPClient.from_transport(transport)

            # Upload the file
            remote_path = f"/{self.file_name}"
            with sftp.open(remote_path, "w") as remote_file:
                remote_file.write(self.file_content)

            self.write({
                "state": "uploaded",
                "upload_response": f"Uploaded to {self.sftp_host}:{remote_path}",
                "error_message": False,
            })

            _logger.info(
                "MSPMP batch uploaded: %s → %s:%s",
                self.file_name, self.sftp_host, remote_path,
            )

        except Exception as e:
            self.write({
                "state": "failed",
                "error_message": f"SFTP upload failed: {e}",
            })
            _logger.error("MSPMP SFTP upload failed: %s", e)
            raise UserError(f"SFTP upload failed: {e}") from e

        finally:
            if sftp:
                sftp.close()
            if transport:
                transport.close()
