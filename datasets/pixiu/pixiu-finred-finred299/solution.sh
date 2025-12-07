#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Lyft ; Logan Green ; chief_executive_officer
Lyft ; Logan Green ; founded_by
EOF
