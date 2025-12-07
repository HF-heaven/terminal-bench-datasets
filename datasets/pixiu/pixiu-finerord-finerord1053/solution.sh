#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Donor:O
Motivation:O
Northern:B-LOC
California:I-LOC
.:O
EOF
