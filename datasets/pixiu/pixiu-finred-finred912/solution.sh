#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Alcoa ; Klaus Kleinfeld ; director_/_manager
Klaus Kleinfeld ; chief executive officer ; position_held
EOF
