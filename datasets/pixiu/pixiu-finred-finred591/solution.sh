#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Celgene ; NASDAQ ; stock_exchange
EOF
