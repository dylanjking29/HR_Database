#!/bin/bash

# Start the SSH agent and add the key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

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

