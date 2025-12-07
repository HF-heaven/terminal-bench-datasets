#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Trulia ; Zillow ; parent_organization
EOF
