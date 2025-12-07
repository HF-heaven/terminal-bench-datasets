#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
PayPal ; NASDAQ ; stock_exchange
EOF
