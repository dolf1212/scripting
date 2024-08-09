import os

def get_size(start_path='.'):
    """Get the total size of the specified directory and all its subdirectories."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def print_directory_size(start_path='.'):
    """Print the size of each subdirectory and the total size of the given directory."""
    print(f"Calculating disk usage for: {start_path}")
    total_size = get_size(start_path)
    print(f"Total size of '{start_path}': {convert_size(total_size)}")

    print("\nSubdirectory sizes:")
    for dirpath, dirnames, _ in os.walk(start_path):
        for d in dirnames:
            dir_size = get_size(os.path.join(dirpath, d))
            print(f"{os.path.join(dirpath, d)}: {convert_size(dir_size)}")

def convert_size(size_bytes):
    """Convert bytes to a more readable format (KB, MB, GB, etc.)."""
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def main():
    directory = input("Enter the directory path to analyze: ")
    print_directory_size(directory)

if __name__ == "__main__":
    main()
