#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Roomba ; iRobot ; owned_by
iRobot ; Roomba ; owner_of
Roomba ; iRobot ; manufacturer
EOF
