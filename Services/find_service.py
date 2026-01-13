import subprocess
import sys

def find_service(search_term):
    try:
        cmd = f'Get-Service | Where-Object {{$_.Name -like "*{search_term}*" -or $_.DisplayName -like "*{search_term}*"}} | Select-Object Name, DisplayName, Status, StartType | Sort-Object DisplayName | Format-Table -AutoSize'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"Search term: \"{search_term}\"\n```\n{result.strip()}\n```")
    except Exception as e:
        print(f"Error searching services: {e}")

if __name__ == "__main__":
    find_service(sys.argv[1])