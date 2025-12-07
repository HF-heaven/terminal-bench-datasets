#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Millions ; Chicago ; location_of_formation
EOF
