#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Viacom ; CBS ; owned_by
Viacom ; CBS ; subsidiary
Viacom ; CBS ; parent_organization
EOF
