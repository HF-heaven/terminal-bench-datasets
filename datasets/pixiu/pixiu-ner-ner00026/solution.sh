#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
bank, ORG
Borrower, PER
Lender, PER
Borrower, PER
Borrower, PER
Lender, PER
Lender, PER
EOF
