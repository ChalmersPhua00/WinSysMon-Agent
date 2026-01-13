import subprocess
import sys

def get_environment_vars():
    try:
        cmd = f'Get-ChildItem Env: | Sort-Object Name | Format-Table Name, Value -AutoSize'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(result.strip())
    except Exception as e:
        print(f"Error getting environment variables: {e}")

if __name__ == "__main__":
    get_environment_vars()