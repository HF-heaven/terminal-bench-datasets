#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
amex ; American Express ; operator
EOF
