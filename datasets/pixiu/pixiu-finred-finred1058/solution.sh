#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Wipro ; Azim Premji ; founded_by
Wipro ; Azim Premji ; owned_by
Wipro ; Azim Premji ; director_/_manager
EOF
