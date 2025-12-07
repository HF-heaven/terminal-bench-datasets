#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Louis Vuitton ; LVMH ; parent_organization
LVMH ; Louis Vuitton ; owner_of
Louis Vuitton ; LVMH ; owned_by
EOF
