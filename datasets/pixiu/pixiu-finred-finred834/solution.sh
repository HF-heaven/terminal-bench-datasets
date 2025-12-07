#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
GoPro ; NASDAQ ; stock_exchange
EOF
