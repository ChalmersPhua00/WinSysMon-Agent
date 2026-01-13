import os
import sys

def change_working_directory(path):
    try:
        os.chdir(path)
        print(f"CD to: {os.getcwd()}")
    except Exception as e:
        print(f"Error changing directory: {e}")

if __name__ == "__main__":
    change_working_directory(sys.argv[1])