#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Viatris ; Mylan ; subsidiary
Mylan ; Viatris ; parent_organization
EOF
