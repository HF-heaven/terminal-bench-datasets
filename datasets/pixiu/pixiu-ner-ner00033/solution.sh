#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Borrower, PER
Saint Auban, LOC
Saint Auban, LOC
France, LOC
EOF
