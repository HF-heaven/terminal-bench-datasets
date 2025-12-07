#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
58 ; California ; location_of_formation
EOF
