#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
John Cleese ; Monty Python ; member_of
EOF
