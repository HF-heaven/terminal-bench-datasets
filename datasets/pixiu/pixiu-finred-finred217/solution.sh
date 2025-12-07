#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Apartment ; London ; location_of_formation
EOF
