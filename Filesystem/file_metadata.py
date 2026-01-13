import os
import datetime
import sys

def file_metadata(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Path '{file_path}' does not exist.")
    else:
        stats = os.stat(file_path)
        created = datetime.datetime.fromtimestamp(stats.st_ctime)
        modified = datetime.datetime.fromtimestamp(stats.st_mtime)
        accessed = datetime.datetime.fromtimestamp(stats.st_atime)
        # Format size
        size = stats.st_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                break
            size /= 1024
        size_str = f"{size:.2f} {unit}"
        print(f"\nPath: {file_path}")
        print(f"- Type:       {'Directory' if os.path.isdir(file_path) else 'File'}")
        print(f"- Size:       {size_str}")
        print(f"- Created:    {created}")
        print(f"- Modified:   {modified}")
        print(f"- Accessed:   {accessed}")

if __name__ == "__main__":
    file_metadata(sys.argv[1])