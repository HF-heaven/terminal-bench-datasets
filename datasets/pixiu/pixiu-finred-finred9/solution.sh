#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Frozen ; single ; distribution_format
EOF
