#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
GMC ; Detroit ; headquarters_location
EOF
