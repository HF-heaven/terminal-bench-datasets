#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Goldman Sachs ; Lloyd Blankfein ; chief_executive_officer
Lloyd Blankfein ; Goldman Sachs ; employer
EOF
