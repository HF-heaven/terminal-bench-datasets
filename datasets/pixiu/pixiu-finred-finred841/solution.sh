#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Berkshire Hathaway ; Phillips 66 ; owner_of
Phillips 66 ; Berkshire Hathaway ; owned_by
EOF
