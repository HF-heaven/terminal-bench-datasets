#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
BANK, ORG
BORROWER, PER
EOF
