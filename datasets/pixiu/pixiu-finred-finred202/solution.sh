#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Pixel ; Google ; developer
Pixel ; Google ; manufacturer
EOF
