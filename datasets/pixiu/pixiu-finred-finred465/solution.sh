#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
G4S ; London ; headquarters_location
betfair ; London ; headquarters_location
Smiths Group ; London ; headquarters_location
EOF
