#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Larry Page ; Google ; employer
EOF
