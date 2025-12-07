#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Scott Farquhar ; Atlassian ; employer
Atlassian ; Scott Farquhar ; founded_by
EOF
