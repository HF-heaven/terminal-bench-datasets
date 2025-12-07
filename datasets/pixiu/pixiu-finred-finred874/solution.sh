#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Telefónica Deutschland ; Telefónica ; parent_organization
Telefónica ; Telefónica Deutschland ; subsidiary
EOF
