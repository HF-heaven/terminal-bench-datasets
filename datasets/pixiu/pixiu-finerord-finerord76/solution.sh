#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Image:O
source:O
::O
General:B-ORG
Motors:I-ORG
.:O
EOF
