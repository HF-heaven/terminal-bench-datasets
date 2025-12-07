#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
LaFerrari ; Ferrari ; brand
LaFerrari ; Ferrari ; manufacturer
EOF
