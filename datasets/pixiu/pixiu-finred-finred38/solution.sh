#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
SABMiller ; Anheuser-Busch InBev ; parent_organization
SABMiller ; beer ; product_or_material_produced
SABMiller ; Anheuser-Busch InBev ; owned_by
EOF
