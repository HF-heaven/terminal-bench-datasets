#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Infiniti ; Nissan ; owned_by
Infiniti ; Nissan ; parent_organization
EOF
