#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
LexisNexis ; RELX Group ; owned_by
LexisNexis ; RELX Group ; parent_organization
EOF
