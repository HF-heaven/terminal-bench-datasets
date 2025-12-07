#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
National Geographic Partners ; joint venture ; legal_form
National Geographic Partners ; National Geographic ; subsidiary
EOF
