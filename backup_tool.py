import os
import shutil
from datetime import datetime

def create_backup(source, destination):
    """Create a backup of the source directory to the destination."""
    if not os.path.exists(source):
        print(f"Source directory {source} does not exist.")
        return

    if not os.path.exists(destination):
        os.makedirs(destination)

    # Create a timestamped backup folder
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_folder = os.path.join(destination, f"backup_{timestamp}")

    try:
        shutil.copytree(source, backup_folder)
        print(f"Backup created successfully at {backup_folder}")
    except Exception as e:
        print(f"Error creating backup: {e}")

def main():
    source = input("Enter the source directory path: ")
    destination = input("Enter the destination directory path: ")

    create_backup(source, destination)

if __name__ == "__main__":
    main()
