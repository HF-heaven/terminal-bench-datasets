#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
WorldPay ; London ; headquarters_location
EOF
