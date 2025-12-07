#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
McPhail:B-PER
is:O
unsure:O
who:O
he:O
will:O
vote:O
for:O
.:O
EOF
