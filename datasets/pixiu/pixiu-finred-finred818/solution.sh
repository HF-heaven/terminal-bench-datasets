#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Gameloft ; Vivendi ; owned_by
Gameloft ; Vivendi ; parent_organization
Vivendi ; Gameloft ; subsidiary
EOF
