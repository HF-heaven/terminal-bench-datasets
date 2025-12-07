#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Whopper ; Burger King ; manufacturer
EOF
