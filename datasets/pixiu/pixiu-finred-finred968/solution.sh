#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Deezer ; Paris ; headquarters_location
Raise ; music streaming ; distribution_format
EOF
