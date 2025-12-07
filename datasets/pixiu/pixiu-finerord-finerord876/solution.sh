#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
He:O
has:O
previously:O
voted:O
for:O
Randall:B-PER
.:O
EOF
