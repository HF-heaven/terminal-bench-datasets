#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
snom ; Berlin ; headquarters_location
EOF
