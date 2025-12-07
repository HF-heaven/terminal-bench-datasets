#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Lafarge ; LafargeHolcim ; parent_organization
EOF
