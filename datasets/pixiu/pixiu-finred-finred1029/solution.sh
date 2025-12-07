#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Chrysler Executive ; Chrysler ; brand
Chrysler Executive ; Chrysler ; manufacturer
EOF
