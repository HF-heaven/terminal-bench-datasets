#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Buick ; General Motors ; parent_organization
Buick ; General Motors ; owned_by
EOF
