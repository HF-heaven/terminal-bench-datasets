#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
You:O
need:O
less:O
funding:O
::O
Alley:B-ORG
NYC:I-ORG
EOF
