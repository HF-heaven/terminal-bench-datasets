#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Covestro ; Bayer ; owned_by
EOF
