#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Keio ; Tokyo ; location_of_formation
Begin ; Tokyo ; location_of_formation
EOF
