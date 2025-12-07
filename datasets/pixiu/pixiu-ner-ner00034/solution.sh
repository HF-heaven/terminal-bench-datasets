#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Frank Wouters, PER
CEO, LOC
Lender, PER
138 Bartlett Street Marlboro, LOC
Massachusetts, LOC
EOF
