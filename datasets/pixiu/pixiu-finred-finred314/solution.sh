#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Honda City ; Honda ; brand
Honda Accord ; Honda ; brand
Honda City ; Honda ; manufacturer
Honda Accord ; Honda ; manufacturer
EOF
