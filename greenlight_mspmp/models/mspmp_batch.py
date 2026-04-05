from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError


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

        # TODO: Implement ASAP 4.2 format generation
        # See docs/shared-compliance/mspmp-reporting.md
        lines = [f"# ASAP 4.2 Batch - {self.report_date} - {len(transactions)} transactions"]
        lines.append("# TODO: Full ASAP 4.2 format implementation")

        self.write({
            "state": "generated",
            "transaction_count": len(transactions),
            "file_content": "\n".join(lines),
            "file_name": f"MSPMP_{self.report_date.strftime('%Y%m%d')}.dat",
        })

    def action_upload(self):
        """Upload generated batch file via SFTP."""
        self.ensure_one()
        if self.state != "generated":
            raise UserError("Must generate the batch file before uploading.")

        # TODO: Implement SFTP upload using paramiko
        # See docs/shared-compliance/mspmp-reporting.md
        raise UserError("SFTP upload not yet implemented. Upload the file manually.")
