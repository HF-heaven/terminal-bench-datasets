#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Nordstrom Rack ; Nordstrom ; parent_organization
EOF
