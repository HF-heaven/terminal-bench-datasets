#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
FireEye ; NASDAQ ; stock_exchange
CyberArk ; NASDAQ ; stock_exchange
EOF
