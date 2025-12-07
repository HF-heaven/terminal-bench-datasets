#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Rosneft ; Igor Sechin ; chief_executive_officer
Rosneft ; Igor Sechin ; director_/_manager
EOF
