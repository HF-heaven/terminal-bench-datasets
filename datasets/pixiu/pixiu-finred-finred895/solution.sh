#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Huggies ; Kimberly-Clark ; owned_by
Huggies ; Kimberly-Clark ; parent_organization
EOF
