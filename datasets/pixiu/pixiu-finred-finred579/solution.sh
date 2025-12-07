#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Mark Cuban ; Dallas Mavericks ; owner_of
Dallas Mavericks ; Mark Cuban ; owned_by
EOF
