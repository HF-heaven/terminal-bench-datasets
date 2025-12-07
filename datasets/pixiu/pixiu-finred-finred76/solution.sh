#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
program ; computer ; platform
EOF
