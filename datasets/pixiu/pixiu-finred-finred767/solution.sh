#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Secret City ; Foxtel ; distributed_by
EOF
