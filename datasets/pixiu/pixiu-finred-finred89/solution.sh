#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Airbus Group ; Airbus ; subsidiary
Airbus ; Airbus Group ; parent_organization
EOF
