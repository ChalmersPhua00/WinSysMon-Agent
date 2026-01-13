import os
import fnmatch
import datetime
import sys

def search_filesystem(pattern, search_path, recursive):
    print(f"File Search Results")
    print(f"Pattern: {pattern}")
    print(f"Path: {search_path}")
    print(f"Recursive: {recursive}")
    print(f"\n{'Size':<15} {'Modified':<20} {'File Path'}")
    print("-" * 90)
    matches = []

    try:
        if recursive:
            for root, _, files in os.walk(search_path):
                for name in files:
                    if fnmatch.fnmatch(name, pattern) or pattern.lower() in name.lower():
                        matches.append(os.path.join(root, name))
        else:
            try:
                for name in os.listdir(search_path):
                    if fnmatch.fnmatch(name, pattern) or pattern.lower() in name.lower():
                        full_path = os.path.join(search_path, name)
                        if os.path.isfile(full_path):
                            matches.append(full_path)
            except OSError:
                pass

        for filepath in matches:
            try:
                stats = os.stat(filepath)
                size = stats.st_size
                mtime = datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                # Simple size formatting
                size_str = f"{size} B"
                if size > 1024: size_str = f"{size/1024:.1f} KB"
                if size > 1024*1024: size_str = f"{size/(1024*1024):.1f} MB"
                print(f"{size_str:<15} {mtime:<20} {filepath}")
            except OSError:
                continue
    except Exception as e:
        print(f"Error searching files: {e}")

if __name__ == "__main__":
    pattern = sys.argv[1]
    search_path = sys.argv[2]
    recursive = sys.argv[3].lower() == 'true'
    search_filesystem(pattern, search_path, recursive)