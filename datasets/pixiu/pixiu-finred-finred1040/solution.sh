#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Boeing ; McDonnell Douglas ; subsidiary
EOF
