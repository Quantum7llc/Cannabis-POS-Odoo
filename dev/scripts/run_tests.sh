#!/bin/bash
# Run Odoo tests for a specific module
# Usage: ./dev/scripts/run_tests.sh greenlight_exchange
#
# This runs inside the Docker container against a test database.

MODULE=${1:-greenlight_exchange}
DB_NAME="test_${MODULE}"
CONTAINER=${CONTAINER:-greenlight-odoo}

echo "Running tests for module: $MODULE"
docker exec $CONTAINER \
    odoo --test-enable \
    --stop-after-init \
    -d "$DB_NAME" \
    -i "$MODULE" \
    --addons-path=/mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons \
    --log-level=test 2>&1 | grep -E "(TEST|ERROR|FAIL|OK|test_)"

echo ""
echo "Test database '$DB_NAME' preserved for inspection."
