#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
DirecTV ; AT ; owned_by
EOF
