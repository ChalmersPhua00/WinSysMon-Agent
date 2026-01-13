import subprocess

def get_network_adapters():
    try:
        cmd = "Get-NetAdapter | Select-Object Name, InterfaceDescription, Status, LinkSpeed, MediaType, PhysicalMediaType | Format-Table -AutoSize"
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
        ip_cmd = "Get-NetIPAddress | Where-Object {$_.AddressFamily -eq 'IPv4'} | Select-Object InterfaceAlias, IPAddress, PrefixLength | Format-Table -AutoSize"
        ip_result = subprocess.run(["powershell", "-Command", ip_cmd], capture_output=True, text=True)
        
        print(f"Adapter Information\n{result.stdout}\nIP Configuration\n{ip_result.stdout}")
    except Exception as e:
        print(f"Error getting network adapters: {str(e)}")

if __name__ == "__main__":
    get_network_adapters()