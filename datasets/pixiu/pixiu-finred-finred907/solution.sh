#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Games Workshop ; London ; location_of_formation
EOF
