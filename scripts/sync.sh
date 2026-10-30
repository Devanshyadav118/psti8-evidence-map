#!/usr/bin/env bash
# scripts/sync.sh - Quick sync script for PSTi8 vault
set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

echo "=== Syncing PSTi8 Vault with GitHub ==="
echo "Working directory: $REPO_DIR"

# Stage changes (respecting .gitignore)
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No local changes to commit."
else
    COMMIT_MSG="${1:-Auto-sync: $(date '+%Y-%m-%d %H:%M:%S')}"
    git commit -m "$COMMIT_MSG"
    echo "Committed changes: $COMMIT_MSG"
fi

# Pull any remote updates with rebase
echo "Pulling latest changes from GitHub..."
git pull --rebase origin main

# Push to remote
echo "Pushing to GitHub..."
git push origin main

echo "=== Sync complete! Repository is up to date. ==="
