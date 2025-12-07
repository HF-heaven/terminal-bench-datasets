#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Facebook ; Mark Zuckerberg ; founded_by
Facebook ; Mark Zuckerberg ; creator
EOF
