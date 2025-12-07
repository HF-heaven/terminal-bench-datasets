#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Borrower, PER
Bank, ORG
Bank, ORG
Borrower, PER
EOF
