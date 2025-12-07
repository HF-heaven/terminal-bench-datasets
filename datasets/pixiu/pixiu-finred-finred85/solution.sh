#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
SABMiller ; London ; headquarters_location
EOF
