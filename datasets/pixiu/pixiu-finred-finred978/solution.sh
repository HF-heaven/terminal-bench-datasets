#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Magic Quadrant ; Gartner ; creator
Magic Quadrant ; Gartner ; owned_by
EOF
