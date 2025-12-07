#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Borrower, PER
United States, LOC
Borrower, PER
United States, LOC
EOF
