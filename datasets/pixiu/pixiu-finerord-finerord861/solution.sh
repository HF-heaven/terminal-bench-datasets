#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
It:O
's:O
so:O
uncertain:O
now:O
,:O
":O
McPhail:B-PER
says:O
.:O
EOF
