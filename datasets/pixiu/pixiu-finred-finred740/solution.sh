#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Lyft ; San Francisco ; headquarters_location
EOF
