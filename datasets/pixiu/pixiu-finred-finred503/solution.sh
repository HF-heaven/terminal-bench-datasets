#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
iShares ; BlackRock ; operator
EOF
