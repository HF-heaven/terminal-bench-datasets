#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
MoneyGram ; Dallas ; headquarters_location
EOF
