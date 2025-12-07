#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Union Bank, ORG
California, LOC
UNION BANK, ORG
CALIFORNIA, LOC
EOF
