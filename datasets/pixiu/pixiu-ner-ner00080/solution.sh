#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Union Bank, ORG
California, LOC
Bank, ORG
Delaware, ORG
Borrower, PER
EOF
