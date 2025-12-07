#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Dubai World ; Dubai ; location_of_formation
Dubai World ; Dubai ; headquarters_location
EOF
