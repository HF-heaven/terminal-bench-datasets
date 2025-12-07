#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Bank, ORG
Borrower, PER
EOF
