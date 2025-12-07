#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Tunisair ; Tunis ; headquarters_location
Tunisair ; Tunis ; location_of_formation
EOF
