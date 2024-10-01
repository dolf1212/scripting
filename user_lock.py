#!/bin/bash

# List of users to lock
USERS=("user1" "user2" "user3")

for user in "${USERS[@]}"; do
    echo "Locking down $user..."
    # Disable login shell
    usermod -s /sbin/nologin $user
    # Expire password
    passwd -l $user
    echo "$user has been locked down."
done

echo "User lockdown completed."
