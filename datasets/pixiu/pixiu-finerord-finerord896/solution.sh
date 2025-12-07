#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Black:B-PER
suggests:O
EOF
