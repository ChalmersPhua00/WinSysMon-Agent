import os
import sys

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Path '{file_path}' does not exist.")
        return
    if os.path.isdir(file_path):
        print(f"Error: '{file_path}' is a directory, not a file.")
        return
    if os.path.getsize(file_path) > 1024 * 1024: # 1MB limit
        print("Error: File too large (>1MB).")
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"\nFile Content: {file_path}\n```\n{content}\n```")

if __name__ == "__main__":
    read_file(sys.argv[1])