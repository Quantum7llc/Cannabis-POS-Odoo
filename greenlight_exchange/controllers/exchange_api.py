import json
from odoo import http
from odoo.http import request, Response


class ExchangeRateController(http.Controller):
    """REST-style API for exchange rates.

    Demonstrates Odoo controller patterns:
    - Route decorators with auth modes
    - JSON response formatting
    - Query parameter handling
    - Error handling

    Works on both Community and Enterprise.
    """

    @http.route("/api/exchange/pairs", type="http", auth="public", methods=["GET"], csrf=False)
    def get_pairs(self):
        """GET /api/exchange/pairs — list all active currency pairs with latest rate."""
        pairs = request.env["greenlight.currency.pair"].sudo().search([("is_active", "=", True)])
        data = []
        for pair in pairs:
            data.append({
                "id": pair.id,
                "name": pair.name,
                "base": pair.base_currency,
                "quote": pair.quote_currency,
                "latest_rate": pair.latest_rate,
                "latest_date": str(pair.latest_date) if pair.latest_date else None,
            })
        return Response(
            json.dumps({"pairs": data}),
            content_type="application/json",
            status=200,
        )

    @http.route("/api/exchange/rates/<string:pair_name>", type="http", auth="public", methods=["GET"], csrf=False)
    def get_rates(self, pair_name, limit="30", **kwargs):
        """GET /api/exchange/rates/USD/GBP?limit=30 — rate history for a pair."""
        # pair_name comes as "USD" due to slash routing; reconstruct from path
        # Handle both /USD/GBP and /USD-GBP formats
        pair_name = pair_name.upper().replace("-", "/")

        pair = request.env["greenlight.currency.pair"].sudo().search(
            [("name", "=", pair_name)], limit=1
        )
        if not pair:
            return Response(
                json.dumps({"error": f"Pair '{pair_name}' not found"}),
                content_type="application/json",
                status=404,
            )

        rates = request.env["greenlight.exchange.rate"].sudo().search(
            [("pair_id", "=", pair.id)],
            order="rate_date desc",
            limit=int(limit),
        )
        data = []
        for r in rates:
            data.append({
                "date": str(r.rate_date),
                "rate": r.rate,
                "open": r.open_rate,
                "high": r.high_rate,
                "low": r.low_rate,
                "close": r.close_rate,
                "change_pct": r.change_pct,
                "source": r.source,
            })
        return Response(
            json.dumps({"pair": pair_name, "rates": data}),
            content_type="application/json",
            status=200,
        )

    @http.route("/api/exchange/health", type="http", auth="none", methods=["GET"], csrf=False)
    def health_check(self):
        """GET /api/exchange/health — simple health check."""
        return Response(
            json.dumps({"status": "ok", "module": "greenlight_exchange"}),
            content_type="application/json",
            status=200,
        )
