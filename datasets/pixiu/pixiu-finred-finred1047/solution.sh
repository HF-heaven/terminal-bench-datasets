#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
PayPal ; eBay ; owned_by
eBay ; PayPal ; owner_of
eBay ; PayPal ; subsidiary
eBay ; corporation ; legal_form
EOF
