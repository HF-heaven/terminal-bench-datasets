#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Chrysler Sebring ; Chrysler ; manufacturer
Chrysler Sebring ; Chrysler ; brand
EOF
