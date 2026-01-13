import subprocess
import sys

def search_registry_keys(search_term, hive):
    try:
        cmd = f'Get-ChildItem -Path "Registry::{hive}\\" -Recurse -ErrorAction SilentlyContinue | Where-Object {{$_.Name -like "*{search_term}*"}} | Select-Object Name -First 20 | Format-Table -AutoSize'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"Search term: \"{search_term}\"\nHive: {hive}\nLimit: 20 results\n```\n{result.strip()}\n```")
    except Exception as e:
        print(f"Error searching registry keys: {e}")

if __name__ == "__main__":
    search_registry_keys(sys.argv[1], sys.argv[2])