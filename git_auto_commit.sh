#!/bin/bash

# Reuse existing SSH agent session
export SSH_AUTH_SOCK=$(ls /tmp/ssh-*/agent.* 2>/dev/null | head -n 1)

# Navigate to your project directory
cd ~/HR_Database || exit

# Get the current timestamp
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Add all changes
git add .

# Commit with a timestamp message
git commit -m "Auto-commit: $TIMESTAMP"

# Push to the remote GitHub repository
git push origin main

