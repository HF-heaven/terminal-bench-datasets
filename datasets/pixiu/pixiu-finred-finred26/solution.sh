#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
phd ; Google ; operator
EOF
