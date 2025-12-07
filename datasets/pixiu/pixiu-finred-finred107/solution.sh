#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Wanda Group ; Dalian ; location_of_formation
Wanda Group ; conglomerate ; industry
EOF
