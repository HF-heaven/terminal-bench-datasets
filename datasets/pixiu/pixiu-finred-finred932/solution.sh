#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
LVMH ; Bernard Arnault ; director_/_manager
LVMH ; Bernard Arnault ; chief_executive_officer
EOF
