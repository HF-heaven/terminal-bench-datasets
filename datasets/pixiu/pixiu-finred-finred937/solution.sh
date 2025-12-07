#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
SABMiller ; Anheuser-Busch InBev ; parent_organization
SABMiller ; Anheuser-Busch InBev ; owned_by
EOF
