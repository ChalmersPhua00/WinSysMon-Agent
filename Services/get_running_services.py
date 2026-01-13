import subprocess
import sys

def get_running_services(limit):
    try:
        cmd = f'Get-Service | Where-Object {{$_.Status -eq "Running"}} | Select-Object -First {limit} Name, DisplayName, Status | Sort-Object DisplayName | Format-Table -AutoSize'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"Running Services\nLimit: {limit}\n{result.strip()}")
    except Exception as e:
        print(f"Error getting running services: {e}")

if __name__ == "__main__":
    limit = sys.argv[1]
    get_running_services(limit)