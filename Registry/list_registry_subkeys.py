import subprocess
import sys

def list_registry_subkeys(key_path, max_depth):
    try:
        if max_depth > 1:
            cmd = f'Get-ChildItem -Path "Registry::{key_path}" -Recurse -Depth {max_depth - 1} -ErrorAction SilentlyContinue | Select-Object Name, Property | Format-Table -AutoSize'
        else:
            cmd = f'Get-ChildItem -Path "Registry::{key_path}" -ErrorAction SilentlyContinue | Select-Object Name, Property | Format-Table -AutoSize'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"Registry Subkeys\nParent Key: {key_path}\nMax Depth: {max_depth}\n```\n{result.strip()}\n```")
    except Exception as e:
        print(f"Error listing subkeys for {key_path}: {e}")

if __name__ == "__main__":
    list_registry_subkeys(sys.argv[1], int(sys.argv[2]))