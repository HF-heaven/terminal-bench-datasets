#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Zillow ; NASDAQ ; stock_exchange
EOF
