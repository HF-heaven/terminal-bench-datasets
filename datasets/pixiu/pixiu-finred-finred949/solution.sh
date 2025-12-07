#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
WorldPay ; Advent International ; parent_organization
EOF
