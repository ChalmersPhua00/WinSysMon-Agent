import subprocess
import sys

def read_registry_key(key_path):
    try:
        cmd = f'Get-ItemProperty -Path "Registry::{key_path}" -ErrorAction Stop | Format-List'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"Registry Key: {key_path}\n```\n{result.strip()}\n```")
    except Exception as e:
        print(f"Error reading registry key {key_path}: {e}")

if __name__ == "__main__":
    read_registry_key(sys.argv[1])