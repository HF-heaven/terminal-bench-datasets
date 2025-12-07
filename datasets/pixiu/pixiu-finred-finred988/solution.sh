#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Foxtel ; joint venture ; legal_form
Presto ; Foxtel ; owned_by
EOF
