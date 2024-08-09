import os
import time
from datetime import datetime, timedelta

def delete_files_by_extension(directory, extension):
    """Delete all files with the given extension in the specified directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

def delete_files_older_than_days(directory, days):
    """Delete all files older than the specified number of days in the given directory."""
    now = time.time()
    cutoff = now - (days * 86400)  # 86400 seconds in a day

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getmtime(file_path) < cutoff:
                os.remove(file_path)
                print(f"Deleted: {file_path}")

def delete_empty_folders(directory):
    """Delete all empty folders in the specified directory."""
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Deleted empty folder: {dir_path}")

def main():
    directory = input("Enter the directory path: ")

    print("Choose an option:")
    print("1. Delete files by extension")
    print("2. Delete files older than a specified number of days")
    print("3. Delete empty folders")
    print("4. Perform all of the above")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        extension = input("Enter the file extension (e.g., .txt): ")
        delete_files_by_extension(directory, extension)
    elif choice == '2':
        days = int(input("Enter the number of days: "))
        delete_files_older_than_days(directory, days)
    elif choice == '3':
        delete_empty_folders(directory)
    elif choice == '4':
        extension = input("Enter the file extension (e.g., .txt): ")
        delete_files_by_extension(directory, extension)

        days = int(input("Enter the number of days: "))
        delete_files_older_than_days(directory, days)

        delete_empty_folders(directory)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
