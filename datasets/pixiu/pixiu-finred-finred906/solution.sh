#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Standard Chartered ; London ; location_of_formation
Standard Chartered ; London ; headquarters_location
EOF
