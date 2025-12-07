#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Platts ; Global ; parent_organization
Platts ; Global ; owned_by
EOF
