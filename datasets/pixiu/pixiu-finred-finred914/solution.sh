#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
AmazonFresh ; retail ; industry
AmazonFresh ; Amazon ; parent_organization
EOF
