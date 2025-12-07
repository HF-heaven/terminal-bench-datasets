#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Come ; Boston ; location_of_formation
EOF
