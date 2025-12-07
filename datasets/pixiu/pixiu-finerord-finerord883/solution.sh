#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
The:O
electorate:O
loved:O
Randall:B-PER
.:O
EOF
