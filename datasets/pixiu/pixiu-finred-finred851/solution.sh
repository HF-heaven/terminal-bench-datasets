#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Prime Video ; Amazon ; developer
Prime Video ; Amazon ; founded_by
Prime Video ; Amazon ; parent_organization
EOF
