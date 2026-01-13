import subprocess
import sys

def get_active_connections(protocol):
    try:
        protocol_filter = ""
        if protocol.lower() != "all":
            protocol_filter = f"-Protocol {protocol.upper()}"
        cmd = f"Get-NetTCPConnection {protocol_filter} | Where-Object {{$_.State -eq 'Established'}} | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess | Format-Table -AutoSize"
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
        
        print(f"Active Network Connections\nProtocol: {protocol}\n{result.stdout}")
    except Exception as e:
        print(f"Error getting active connections: {str(e)}")

if __name__ == "__main__":
    get_active_connections(sys.argv[1])