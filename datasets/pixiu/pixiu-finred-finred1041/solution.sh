#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
NBCUniversal ; Comcast ; parent_organization
NBCUniversal ; Comcast ; owned_by
Comcast ; NBCUniversal ; subsidiary
NBCUniversal ; Comcast ; founded_by
EOF
