#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
VAST ; Seattle ; location_of_formation
EOF
