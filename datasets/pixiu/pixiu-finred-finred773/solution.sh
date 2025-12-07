#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Wella ; Coty ; parent_organization
Wella ; Coty ; owned_by
EOF
