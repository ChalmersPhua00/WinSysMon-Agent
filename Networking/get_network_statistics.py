import subprocess

def get_network_statistics():
    try:
        adapter_cmd = "Get-NetAdapterStatistics | Select-Object Name, BytesReceived, BytesSent, PacketsReceived, PacketsSent | Format-Table -AutoSize"
        adapter_res = subprocess.run(["powershell", "-Command", adapter_cmd], capture_output=True, text=True)
        proto_cmd = "netstat -s"
        proto_res = subprocess.run(proto_cmd, capture_output=True, text=True, shell=True)
        
        print(f"Adapter Statistics\n{adapter_res.stdout}\nProtocol Statistics\n{proto_res.stdout}")
    except Exception as e:
        print(f"Error getting network statistics: {str(e)}")

if __name__ == "__main__":
    get_network_statistics()