#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Airbnb ; San Francisco ; headquarters_location
EOF
