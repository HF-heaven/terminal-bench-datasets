#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
GE Capital ; General Electric ; owned_by
GE Capital ; General Electric ; parent_organization
General Electric ; GE Capital ; owner_of
EOF
