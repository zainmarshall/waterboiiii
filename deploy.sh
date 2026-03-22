#!/usr/bin/env bash
# Auto-deploy: pull latest changes, rebuild only if something changed, restart.
# Add to cron on your Pi:  */30 * * * * /path/to/waterboiiii/deploy.sh >> /var/log/waterboiiii-deploy.log 2>&1

set -euo pipefail
cd "$(dirname "$0")"

# Fetch latest
git fetch origin master

LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/master)

if [ "$LOCAL" = "$REMOTE" ]; then
    echo "$(date): No changes, skipping."
    exit 0
fi

echo "$(date): Changes detected, deploying..."
git pull origin master
docker compose build --no-cache
docker compose up -d
echo "$(date): Deploy complete."
