#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Pipistrel ; Ivo Boscarol ; chief_executive_officer
Pipistrel ; Ivo Boscarol ; founded_by
EOF
