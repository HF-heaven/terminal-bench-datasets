#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Blinkx:B-ORG
Plc:I-ORG
,:O
Boohoo:B-ORG
.:I-ORG
EOF
