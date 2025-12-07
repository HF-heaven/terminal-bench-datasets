#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
John Lewis Partnership ; John Lewis ; founded_by
John Lewis Partnership ; John Lewis ; subsidiary
EOF
