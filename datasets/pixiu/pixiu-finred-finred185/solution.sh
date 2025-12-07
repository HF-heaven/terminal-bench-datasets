#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Asda ; Leeds ; location_of_formation
Asda ; Leeds ; headquarters_location
EOF
