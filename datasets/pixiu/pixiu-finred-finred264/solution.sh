#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Yelp ; Jeremy Stoppelman ; chief_executive_officer
Yelp ; Jeremy Stoppelman ; founded_by
EOF
