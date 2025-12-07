#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Mimecast ; NASDAQ ; stock_exchange
EOF
