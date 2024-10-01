#!/bin/bash

LOG_DIR="/var/log"
DAYS_OLD=30

# Find and remove log files older than specified days
find $LOG_DIR -type f -name "*.log" -mtime +$DAYS_OLD -exec rm -f {} \;

# Log cleanup completion
echo "Old log files removed from $LOG_DIR older than $DAYS_OLD days."
