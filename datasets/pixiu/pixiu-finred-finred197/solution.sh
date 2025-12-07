#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Red Hat ; IBM ; parent_organization
Ansible ; Red Hat ; developer
Ansible ; Red Hat ; owned_by
EOF
