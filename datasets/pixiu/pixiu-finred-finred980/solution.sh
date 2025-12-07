#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Answer ; Spotify ; distributed_by
EOF
