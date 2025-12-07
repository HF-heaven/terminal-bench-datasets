#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Borrower, PER
Lender, PER
Borrower, PER
Wall Street, LOC
EOF
