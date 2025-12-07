#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Unilever ; Dove ; owner_of
Unilever ; Cornetto ; owner_of
EOF
