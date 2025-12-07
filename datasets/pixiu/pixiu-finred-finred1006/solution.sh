#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Eurowings ; Lufthansa Group ; parent_organization
Lufthansa ; Eurowings ; subsidiary
Lufthansa ; Carsten Spohr ; chief_executive_officer
EOF
