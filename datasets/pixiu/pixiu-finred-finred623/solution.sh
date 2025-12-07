#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
British Airways ; International Airlines Group ; owned_by
British Airways ; International Airlines Group ; parent_organization
EOF
