#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Foxtel ; Telstra ; owned_by
Telstra ; Foxtel ; owner_of
EOF
