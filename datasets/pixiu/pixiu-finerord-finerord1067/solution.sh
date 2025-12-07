#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Trump:B-PER
slips:O
in:O
Rasmussen:B-LOC
poll:O
EOF
