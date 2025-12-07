#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Bandhan Bank ; Kolkata ; headquarters_location
Bandhan Bank ; Finance ; industry
EOF
