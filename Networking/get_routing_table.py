import subprocess

def get_routing_table():
    try:
        cmd = "Get-NetRoute | Where-Object {$_.AddressFamily -eq 'IPv4'} | Select-Object DestinationPrefix, NextHop, InterfaceAlias, RouteMetric | Sort-Object RouteMetric | Format-Table -AutoSize"
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
        
        print(f"IPv4 Routing Table\n{result.stdout}")
    except Exception as e:
        print(f"Error getting routing table: {str(e)}")

if __name__ == "__main__":
    get_routing_table()