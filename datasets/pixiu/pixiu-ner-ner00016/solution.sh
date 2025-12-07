#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Lender, PER
Borrower, PER
EOF
