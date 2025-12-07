#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Borrower, PER
Borrower, PER
Borrower, PER
Borrower, PER
Lender, PER
Borrower, PER
Borrower, PER
Borrower, PER
EOF
