#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
MSCI ; New York Stock Exchange ; stock_exchange
Russell 2000 ; New York Stock Exchange ; stock_exchange
EOF
