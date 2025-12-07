#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Global 500 ; Fortune ; creator
EOF
