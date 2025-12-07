#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
HSBC Finance ; HSBC ; parent_organization
EOF
