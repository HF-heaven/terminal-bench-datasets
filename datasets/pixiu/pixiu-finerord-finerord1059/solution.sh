#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Trump:B-PER
::O
China:B-LOC
':O
just:O
destroying:O
us:O
'...:O
EOF
