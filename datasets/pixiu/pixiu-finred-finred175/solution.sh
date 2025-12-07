#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Thomson Reuters ; Reuters ; subsidiary
Thomson Reuters ; Reuters ; business_division
EOF
