#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Xandr ; advertising ; industry
Xandr ; WarnerMedia ; owned_by
EOF
