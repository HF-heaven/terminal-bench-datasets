#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
DirecTV ; AT ; owned_by
Sling TV ; Dish Network ; parent_organization
EOF
