import subprocess
import sys

def read_registry_value(key_path, value_name):
    try:
        cmd = f'Get-ItemPropertyValue -Path "Registry::{key_path}" -Name "{value_name}" -ErrorAction Stop'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"Key: {key_path}\nValue Name: {value_name}\nValue: {result.strip()}")
    except Exception as e:
        print(f"Error reading registry value {value_name} from {key_path}: {e}")

if __name__ == "__main__":
    read_registry_value(sys.argv[1], sys.argv[2])