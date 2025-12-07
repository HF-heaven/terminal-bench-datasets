#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
bank, ORG
EOF
