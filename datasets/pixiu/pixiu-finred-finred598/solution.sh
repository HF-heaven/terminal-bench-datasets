#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Gmail ; Google ; developer
Gmail ; Google ; owned_by
EOF
