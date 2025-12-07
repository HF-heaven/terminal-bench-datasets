#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Mandiant ; FireEye ; parent_organization
FireEye ; Mandiant ; subsidiary
EOF
