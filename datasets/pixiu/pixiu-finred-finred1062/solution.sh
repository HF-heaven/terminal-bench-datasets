#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Goldman Sachs ; New York Stock Exchange ; stock_exchange
EOF
