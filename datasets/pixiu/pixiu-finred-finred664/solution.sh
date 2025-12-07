#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Telstra ; Foxtel ; owner_of
Foxtel ; Telstra ; owned_by
EOF
