#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Borrower, PER
Silicium de Provence, ORG
EOF
