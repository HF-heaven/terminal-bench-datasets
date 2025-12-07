#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Evian ; Danone ; parent_organization
Evian ; Danone ; owned_by
EOF
