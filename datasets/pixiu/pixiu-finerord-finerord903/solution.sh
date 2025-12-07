#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Shorten:B-PER
has:O
appeared:O
three:O
times:O
.:O
EOF
