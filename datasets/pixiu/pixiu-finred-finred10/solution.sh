#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
BG Group ; Royal Dutch Shell ; parent_organization
EOF
