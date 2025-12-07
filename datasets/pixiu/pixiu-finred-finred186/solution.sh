#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Boeing ; Dennis Muilenburg ; chief_executive_officer
Dennis Muilenburg ; Boeing ; employer
EOF
