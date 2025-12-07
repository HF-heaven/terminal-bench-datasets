#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Apple Inc ; NASDAQ ; stock_exchange
EOF
