#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Bill Gates ; Microsoft ; owner_of
EOF
