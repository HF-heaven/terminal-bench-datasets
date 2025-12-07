#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
British Land ; London ; headquarters_location
Apartment ; London ; location_of_formation
EOF
