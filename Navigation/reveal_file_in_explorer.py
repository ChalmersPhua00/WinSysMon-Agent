import os
import subprocess
import sys

def reveal_file_in_explorer(path):
    try:
        path = os.path.abspath(path)
        if not os.path.exists(path):
            print(f"Error: File not found: {path}")
            return
        print(f"Revealing file: {path}")
        subprocess.Popen(f'explorer /select,"{path}"')
        print("Successfully launched Explorer with file selected.")
    except Exception as e:
        print(f"Error revealing file: {e}")

if __name__ == "__main__":
    reveal_file_in_explorer(sys.argv[1])