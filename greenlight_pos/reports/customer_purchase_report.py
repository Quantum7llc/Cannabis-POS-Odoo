from odoo import api, models


class CustomerPurchaseReport(models.AbstractModel):
    """Custom report model for patient purchase history with MMCEU tracking.

    Collects all transactions for each customer and computes per-line
    MMCEU values for Mississippi compliance reporting.
    """
    _name = "report.greenlight_pos.report_customer_purchase_document"
    _description = "Customer Purchase History Report Data"

    @api.model
    def _get_report_values(self, docids, data=None):
        customers = self.env["greenlight.customer"].browse(docids)
        results = []
        for customer in customers:
            transactions = self.env["greenlight.transaction"].search([
                ("customer_id", "=", customer.id),
                ("state", "=", "confirmed"),
            ], order="create_date asc")

            txn_data = []
            grand_total = 0.0
            grand_mmceu = 0.0
            grand_grams = 0.0

            for txn in transactions:
                lines = []
                txn_mmceu = 0.0
                txn_grams = 0.0
                for line in txn.line_ids:
                    mmceu = self._calculate_mmceu(
                        line.cannabis_type,
                        line.weight_grams * line.quantity,
                        line.product_id.thc_percentage,
                    )
                    grams = line.weight_grams * line.quantity
                    lines.append({
                        "product": line.product_id.name,
                        "cannabis_type": line.cannabis_type or "accessory",
                        "quantity": line.quantity,
                        "weight_grams": grams,
                        "unit_price": line.unit_price,
                        "subtotal": line.subtotal,
                        "mmceu": mmceu,
                    })
                    txn_mmceu += mmceu
                    txn_grams += grams
                txn_data.append({
                    "transaction": txn,
                    "lines": lines,
                    "mmceu_total": txn_mmceu,
                    "grams_total": txn_grams,
                })
                grand_total += txn.total
                grand_mmceu += txn_mmceu
                grand_grams += txn_grams

            results.append({
                "customer": customer,
                "transactions": txn_data,
                "grand_total": grand_total,
                "grand_mmceu": grand_mmceu,
                "grand_grams": grand_grams,
                "transaction_count": len(transactions),
            })

        return {
            "doc_ids": docids,
            "doc_model": "greenlight.customer",
            "docs": customers,
            "results": results,
        }

    @staticmethod
    def _calculate_mmceu(cannabis_type, weight_grams, thc_pct):
        """MMCEU calculation matching greenlight.purchase.limit logic."""
        if cannabis_type == "flower":
            return weight_grams / 3.5
        elif cannabis_type in ("concentrate", "infused"):
            return weight_grams * thc_pct / 100.0
        return 0.0
