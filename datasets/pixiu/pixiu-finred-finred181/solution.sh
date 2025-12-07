#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Intel ; Mobileye ; subsidiary
Mobileye ; Intel ; parent_organization
Mobileye ; Jerusalem ; headquarters_location
Mobileye ; Intel ; legal_form
EOF
