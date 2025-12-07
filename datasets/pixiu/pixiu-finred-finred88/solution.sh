#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
News Corp ; Rupert Murdoch ; founded_by
News Corp ; Rupert Murdoch ; director_/_manager
EOF
