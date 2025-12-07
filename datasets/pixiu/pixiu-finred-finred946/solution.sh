#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Finns Party ; Timo Soini ; chairperson
Finns Party ; Timo Soini ; founded_by
EOF
