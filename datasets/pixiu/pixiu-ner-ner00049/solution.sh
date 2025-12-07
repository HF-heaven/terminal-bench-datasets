#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
lender, PER
Borrower, PER
lender, PER
Borrower, PER
EOF
