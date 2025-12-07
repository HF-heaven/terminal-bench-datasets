#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Com:I-ORG
's:O
listed:O
peers:O
.:O
EOF
