#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Producers ; London ; location_of_formation
EOF
