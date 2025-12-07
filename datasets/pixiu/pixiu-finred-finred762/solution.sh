#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Areva ; France ; parent_organization
Areva ; France ; owned_by
EOF
