#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
United Airlines ; United Airlines Holdings ; parent_organization
United Airlines Holdings ; United Airlines ; subsidiary
United Airlines ; United Airlines Holdings ; owned_by
EOF
