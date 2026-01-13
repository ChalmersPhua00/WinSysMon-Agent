import os
import subprocess
import sys

def open_folder_in_explorer(path):
    try:
        path = os.path.abspath(path)
        if not os.path.exists(path):
            print(f"Error: Path not found: {path}")
            return
        print(f"Opening folder: {path}")
        os.startfile(path)
        print("Successfully launched Explorer.")
    except Exception as e:
        print(f"Error opening folder: {e}")

if __name__ == "__main__":
    open_folder_in_explorer(sys.argv[1])