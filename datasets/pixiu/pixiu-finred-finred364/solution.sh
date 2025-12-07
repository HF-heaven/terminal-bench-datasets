#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
grocery ; Walmart ; operator
EOF
