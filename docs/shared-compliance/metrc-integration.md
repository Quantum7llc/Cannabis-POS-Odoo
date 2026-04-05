# Metrc Integration Specification

**Marijuana Enforcement Tracking Reporting Compliance** — Mississippi seed-to-sale system.

API access obtained 2026-04-05. Both Rust and Odoo versions must implement the same Metrc endpoints.

## Configuration

Each facility/license has its own Metrc config:
- `facility_license` — State-issued license number
- `api_key` — Vendor API key (encrypted at rest)
- `user_key` — User/facility API key
- `environment` — `sandbox` or `production`
- `base_url` — `https://sandbox-api-ms.metrc.com` (sandbox) or `https://api-ms.metrc.com` (production)
- `auto_sync` — Whether to automatically push sales
- `sync_interval_minutes` — Default 15

## Required Endpoints

### Outbound (POS -> Metrc)
- `POST /sales/v2/receipts` — Report completed sales
- `PUT /sales/v2/receipts/{id}` — Update/void sales
- `POST /packages/v2/adjust` — Inventory adjustments

### Inbound (Metrc -> POS)
- `GET /packages/v2/active` — Sync active package inventory
- `GET /packages/v2/{id}` — Individual package details
- `GET /labtests/v2/results?packageId={id}` — Lab test results

### Webhook Events (if available)
- `package.updated`
- `transfer.received`

## Sync Status Tracking

Every transaction must track its Metrc sync status:
- `pending` — Not yet reported
- `synced` — Successfully reported to Metrc
- `failed` — Report attempted but failed (retry needed)
- `skipped` — Not applicable (e.g., accessory-only sale)

## Audit Trail

Every Metrc API call must be logged with:
- Direction (outbound/inbound)
- Endpoint and method
- Request/response bodies
- Success/failure status
- Duration in milliseconds
- Associated transaction ID and package tag

## Package Tags

Metrc package tags follow the format: `1A4000000000000000012345` (24 characters). Each product in inventory should be linked to its Metrc package tag for traceability.
