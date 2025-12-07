#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Facebook Inc ; NASDAQ ; stock_exchange
EOF
