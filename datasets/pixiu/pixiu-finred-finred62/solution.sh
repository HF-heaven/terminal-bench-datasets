#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
FedEx ; FedEx Ground ; subsidiary
FedEx Ground ; FedEx ; parent_organization
EOF
