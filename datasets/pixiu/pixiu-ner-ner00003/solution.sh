#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Borrower, PER
France, LOC
EOF
