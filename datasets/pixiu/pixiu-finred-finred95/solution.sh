#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Glencore ; mining ; industry
Lonmin ; mining ; industry
EOF
