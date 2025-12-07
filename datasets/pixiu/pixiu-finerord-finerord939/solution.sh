#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Scout:O
Finch:B-PER
is:O
all:O
grown:O
up:O
,:O
indeed:O
.:O
EOF
