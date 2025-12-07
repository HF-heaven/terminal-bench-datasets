#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Vivendi ; Universal Music Group ; subsidiary
Universal Music Group ; Vivendi ; owned_by
Universal Music Group ; Vivendi ; parent_organization
EOF
