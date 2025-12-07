#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Airbus ; Toulouse ; headquarters_location
EOF
