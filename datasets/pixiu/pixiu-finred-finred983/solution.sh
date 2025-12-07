#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Enel ; Enel Green Power ; owner_of
Enel ; Enel Green Power ; subsidiary
EOF
