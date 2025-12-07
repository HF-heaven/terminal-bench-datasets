#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Yahoo:B-ORG
!:I-ORG
-:O
News:O
Network:O
EOF
