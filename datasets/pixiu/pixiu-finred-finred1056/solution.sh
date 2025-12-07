#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
SoftBank ; Tokyo Stock Exchange ; stock_exchange
SoftBank ; Tokyo ; headquarters_location
EOF
