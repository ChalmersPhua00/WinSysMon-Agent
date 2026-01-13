import subprocess
import sys

def list_services(status_filter, startup_type_filter, limit):
    try:
        conditions = []
        # Map status filter
        if status_filter.lower() != "all":
            status_map = {
                "running": "Running",
                "stopped": "Stopped",
                "paused": "Paused"
            }
            val = status_map.get(status_filter.lower(), "Running")
            conditions.append(f"$_.Status -eq '{val}'")
        # Map startup type filter
        if startup_type_filter.lower() != "all":
            startup_map = {
                "automatic": "Automatic",
                "manual": "Manual",
                "disabled": "Disabled"
            }
            val = startup_map.get(startup_type_filter.lower(), "Automatic")
            conditions.append(f"$_.StartType -eq '{val}'")
        where_clause = ""
        if conditions:
            where_clause = f"| Where-Object {{ {' -and '.join(conditions)} }}"
        cmd = f'Get-Service {where_clause} | Select-Object -First {limit} Name, DisplayName, Status, StartType | Sort-Object DisplayName | Format-Table -AutoSize'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout
        
        print(f"Status Filter: {status_filter}")
        print(f"Startup Type Filter: {startup_type_filter}")
        print(f"Limit: {limit}\n")
        print(f"```\n{result.strip()}\n```")
    except Exception as e:
        print(f"Error listing services: {e}")

if __name__ == "__main__":
    status = sys.argv[1]
    startup = sys.argv[2]
    limit = sys.argv[3]
    list_services(status, startup, limit)