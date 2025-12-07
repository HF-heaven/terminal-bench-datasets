#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Air India ; Mumbai ; headquarters_location
Air India ; Mumbai ; location_of_formation
EOF
