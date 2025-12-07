#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Vodafone ; ONO ; subsidiary
Vodafone ; London ; headquarters_location
EOF
