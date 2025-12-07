#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
iZettle ; PayPal ; parent_organization
EOF
