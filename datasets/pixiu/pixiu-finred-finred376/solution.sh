#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Product ; Spotify ; distributed_by
EOF
