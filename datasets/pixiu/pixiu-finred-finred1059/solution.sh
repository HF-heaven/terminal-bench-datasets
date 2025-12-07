#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Lonmin ; London ; headquarters_location
Lonmin ; London Stock Exchange ; stock_exchange
EOF
