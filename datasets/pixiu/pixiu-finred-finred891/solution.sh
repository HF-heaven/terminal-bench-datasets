#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Bridgewater Associates ; Ray Dalio ; founded_by
Bridgewater Associates ; Ray Dalio ; director_/_manager
EOF
