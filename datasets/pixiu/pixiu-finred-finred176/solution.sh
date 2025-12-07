#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Investec ; London ; headquarters_location
EOF
