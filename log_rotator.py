import os
import glob

def rotate_logs(directory, extension, max_logs):
    """Rotate log files in the specified directory, keeping only the most recent ones."""
    log_files = sorted(glob.glob(os.path.join(directory, f"*{extension}")), key=os.path.getmtime)

    if len(log_files) > max_logs:
        logs_to_delete = log_files[:-max_logs]
        for log_file in logs_to_delete:
            os.remove(log_file)
            print(f"Deleted: {log_file}")

def main():
    directory = input("Enter the directory containing log files: ")
    extension = input("Enter the log file extension (e.g., .log): ")
    max_logs = int(input("Enter the maximum number of logs to keep: "))

    rotate_logs(directory, extension, max_logs)

if __name__ == "__main__":
    main()
