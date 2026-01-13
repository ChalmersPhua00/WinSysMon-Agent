import subprocess
import sys

def get_startup_services(limit):
    try:
        cmd = f'Get-WmiObject -Class Win32_Service | Where-Object {{$_.StartMode -eq "Auto"}} | Select-Object -First {limit} Name, DisplayName, State, StartMode | Sort-Object DisplayName | Format-Table -AutoSize'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"Automatic Startup Services\nLimit: {limit}\n{result.strip()}")
    except Exception as e:
        print(f"Error getting startup services: {e}")

if __name__ == "__main__":
    limit = sys.argv[1]
    get_startup_services(limit)