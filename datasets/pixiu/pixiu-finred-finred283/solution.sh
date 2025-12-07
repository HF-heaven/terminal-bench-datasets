#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
OfficeMax ; Office Depot ; parent_organization
EOF
