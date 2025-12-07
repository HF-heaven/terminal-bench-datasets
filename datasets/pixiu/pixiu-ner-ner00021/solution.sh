#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Borrower, PER
Lender, PER
Lender, PER
Lender, PER
EOF
