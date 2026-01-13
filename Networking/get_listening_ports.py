import subprocess
import sys

def get_listening_ports(protocol):
    try:
        output = ""
        if protocol.lower() in ["all", "tcp"]:
            cmd = "Get-NetTCPConnection | Where-Object {$_.State -eq 'Listen'} | Select-Object LocalAddress, LocalPort, OwningProcess | Sort-Object LocalPort | Format-Table -AutoSize"
            result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
            output += f"TCP Listening Ports\n{result.stdout}"
        if protocol.lower() in ["all", "udp"]:
            cmd = "Get-NetUDPEndpoint | Select-Object LocalAddress, LocalPort, OwningProcess | Sort-Object LocalPort | Format-Table -AutoSize"
            result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
            output += f"UDP Listening Ports\n{result.stdout}"
        
        print(output)
    except Exception as e:
        print(f"Error getting listening ports: {str(e)}")

if __name__ == "__main__":
    get_listening_ports(sys.argv[1])