#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
For:O
example:O
,:O
online:O
fashion:O
retailer:O
,:O
Boohoo:B-ORG
.:I-ORG
EOF
