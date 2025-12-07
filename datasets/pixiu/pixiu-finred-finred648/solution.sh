#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Deloitte ; London ; headquarters_location
Deloitte ; London ; location_of_formation
EOF
