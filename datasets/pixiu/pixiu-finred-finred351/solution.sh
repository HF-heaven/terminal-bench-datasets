#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Indian Railways ; India ; owned_by
Indian Railways ; India ; location_of_formation
EOF
