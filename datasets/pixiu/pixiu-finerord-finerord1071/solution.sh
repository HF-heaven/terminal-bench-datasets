#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Clinton:B-PER
will:O
turn:O
over:O
email:O
...:O
EOF
