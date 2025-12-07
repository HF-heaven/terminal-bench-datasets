#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
JANA Partners ; Barry Rosenstein ; founded_by
Barry Rosenstein ; JANA Partners ; employer
EOF
