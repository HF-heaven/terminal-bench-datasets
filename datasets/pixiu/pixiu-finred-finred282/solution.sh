#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Red Hat ; IBM ; parent_organization
OpenShift ; Red Hat ; developer
Red Hat ; software ; product_or_material_produced
EOF
