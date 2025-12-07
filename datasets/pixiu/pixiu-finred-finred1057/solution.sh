#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Glencore ; London Stock Exchange ; stock_exchange
Glencore ; mining ; industry
Xstrata ; Glencore ; owned_by
EOF
