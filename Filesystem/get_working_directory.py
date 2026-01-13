import os
import sys

def get_working_directory():
    try:
        print(os.getcwd())
    except Exception as e:
        print(f"Error getting working directory: {e}")

if __name__ == "__main__":
    get_working_directory()