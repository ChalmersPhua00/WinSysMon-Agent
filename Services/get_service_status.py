import subprocess
import sys

def get_service_status(service_name):
    try:
        cmd = f'Get-Service -Name "{service_name}" -ErrorAction Stop | Select-Object Name, DisplayName, Status, StartType | Format-List'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"Service Status: {service_name}\n```\n{result.strip()}\n```")
    except Exception as e:
        print(f"Error getting status for {service_name}: {e}")

if __name__ == "__main__":
    get_service_status(sys.argv[1])