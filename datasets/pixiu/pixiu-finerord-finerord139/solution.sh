#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Fundamental:O
company:O
data:O
provided:O
by:O
Capital:B-ORG
IQ:I-ORG
.:O
EOF
