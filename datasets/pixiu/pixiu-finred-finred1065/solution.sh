#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
eBay ; NASDAQ ; stock_exchange
EOF
