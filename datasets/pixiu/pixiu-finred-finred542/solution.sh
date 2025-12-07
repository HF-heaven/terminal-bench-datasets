#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Petrobras ; New York Stock Exchange ; stock_exchange
EOF
