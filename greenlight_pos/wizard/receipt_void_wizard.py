from odoo import models, fields
from odoo.exceptions import UserError


class ReceiptVoidWizard(models.TransientModel):
    _name = "greenlight.receipt.void.wizard"
    _description = "Receipt Void Wizard"

    receipt_id = fields.Many2one("greenlight.receipt", required=True, ondelete="cascade")
    reason = fields.Text("Reason", required=True)

    def action_confirm_void(self):
        self.ensure_one()
        if not self.reason or not self.reason.strip():
            raise UserError("Please provide a reason for voiding this receipt.")
        receipt = self.receipt_id
        receipt.void_reason = self.reason.strip()
        receipt.action_void()
        return {"type": "ir.actions.act_window_close"}
