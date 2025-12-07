#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Openreach ; BT Group ; parent_organization
EOF
