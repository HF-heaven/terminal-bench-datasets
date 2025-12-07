#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Biocon ; Kiran Mazumdar-Shaw ; director_/_manager
Biocon ; Kiran Mazumdar-Shaw ; founded_by
EOF
