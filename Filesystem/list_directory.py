import os
import time
import sys

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def list_directory(dir_path, recursive, max_depth=3, current_depth=0):
    if current_depth == 0:
        print(f"# Directory Listing: {dir_path}\n")
    if current_depth > max_depth:
        return
    try:
        with os.scandir(dir_path) as it:
            entries = list(it)
    except PermissionError:
        indent = "  " * current_depth
        print(f"{indent}📁 {os.path.basename(dir_path)}/ (Access Denied)")
        return
    except FileNotFoundError:
        print(f"Error: Directory '{dir_path}' not found.")
        return
    # Sort: Directories first, then files, alphabetically
    entries.sort(key=lambda e: (not e.is_dir(), e.name.lower()))
    for entry in entries:
        indent = "  " * current_depth
        try:
            stat = entry.stat()
            mtime = time.strftime('%Y-%m-%d', time.localtime(stat.st_mtime))
            if entry.is_dir():
                print(f"{indent}📁 {entry.name}/ ({mtime})")
                if recursive:
                    list_directory(entry.path, recursive, max_depth, current_depth + 1)
            else:
                size = format_size(stat.st_size)
                print(f"{indent}📄 {entry.name} ({size}, {mtime})")
        except OSError:
            # Handle cases where file exists but stats cannot be read
            print(f"{indent}??? {entry.name} (Error reading stats)")

if __name__ == "__main__":
    dir_path = sys.argv[1]
    recursive = sys.argv[2].lower() == 'true'
    list_directory(dir_path, recursive)