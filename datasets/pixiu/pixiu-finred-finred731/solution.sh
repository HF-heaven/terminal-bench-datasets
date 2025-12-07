#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
SYRIZA ; Alexis Tsipras ; chairperson
SYRIZA ; Athens ; headquarters_location
EOF
