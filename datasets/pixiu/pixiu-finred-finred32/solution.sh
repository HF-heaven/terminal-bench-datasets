#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Twitter ; San Francisco ; headquarters_location
EOF
