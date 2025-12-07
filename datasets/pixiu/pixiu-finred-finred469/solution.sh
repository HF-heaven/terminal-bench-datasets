#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Jamf ; Minneapolis ; headquarters_location
EOF
