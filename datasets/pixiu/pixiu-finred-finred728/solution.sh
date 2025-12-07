#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Arizona ; New Jersey ; location_of_formation
EOF
