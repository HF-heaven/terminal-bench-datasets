#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Lloyd Blankfein ; Goldman Sachs ; employer
Goldman Sachs ; Lloyd Blankfein ; chief_executive_officer
Lloyd Blankfein ; chief executive officer ; position_held
EOF
