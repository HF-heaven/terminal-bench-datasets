#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Fast Retailing ; UNIQLO ; subsidiary
UNIQLO ; Fast Retailing ; parent_organization
UNIQLO ; Fast Retailing ; owned_by
EOF
