#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Amlin ; insurance ; industry
Hiscox ; insurance ; industry
EOF
