#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Redmi ; Xiaomi ; parent_organization
Redmi ; Xiaomi ; manufacturer
EOF
