#!/bin/bash
# Reset the Odoo database and reinstall modules
# Usage: ./dev/scripts/reset_db.sh [module_name]

MODULE=${1:-greenlight_exchange}
DB_NAME=${DB_NAME:-odoo}
CONTAINER=${CONTAINER:-greenlight-odoo}
DB_CONTAINER=${DB_CONTAINER:-greenlight-odoo-db}

echo "Dropping database $DB_NAME..."
docker exec $DB_CONTAINER psql -U odoo -c "DROP DATABASE IF EXISTS $DB_NAME;" postgres
docker exec $DB_CONTAINER psql -U odoo -c "CREATE DATABASE $DB_NAME OWNER odoo;" postgres

echo "Restarting Odoo with module install: $MODULE..."
docker restart $CONTAINER

echo "Done. Odoo will install $MODULE on startup."
echo "Access at http://localhost:8069"
