#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Buick ; General Motors ; parent_organization
Chevrolet Camaro ; General Motors ; manufacturer
Buick ; General Motors ; owned_by
Chevrolet Camaro ; Chevrolet ; brand
EOF
