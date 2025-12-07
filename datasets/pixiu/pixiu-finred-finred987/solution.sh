#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Nescafé ; Nestlé ; owned_by
Nescafé ; Nestlé ; manufacturer
EOF
