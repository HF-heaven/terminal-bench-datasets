#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
| hdfc ; HDFC Bank ; owned_by
hdfc ; HDFC Bank ; operator
EOF
