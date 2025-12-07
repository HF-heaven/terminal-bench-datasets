#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Uniper ; Fortum ; owned_by
Fortum ; Uniper ; owner_of
EOF
