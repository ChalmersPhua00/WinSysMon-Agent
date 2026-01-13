import subprocess

def get_dns_info():
    try:
        dns_cmd = "Get-DnsClientServerAddress | Where-Object {$_.AddressFamily -eq 2} | Select-Object InterfaceAlias, ServerAddresses | Format-Table -AutoSize"
        dns_res = subprocess.run(["powershell", "-Command", dns_cmd], capture_output=True, text=True)
        cache_cmd = "Get-DnsClientCache | Select-Object -First 20 Name, Type, Status, Section, TimeToLive | Format-Table -AutoSize"
        cache_res = subprocess.run(["powershell", "-Command", cache_cmd], capture_output=True, text=True)
        
        print(f"DNS Servers\n{dns_res.stdout}\nDNS Cache (First 20 entries)\n{cache_res.stdout}")
    except Exception as e:
        print(f"Error getting DNS info: {str(e)}")

if __name__ == "__main__":
    get_dns_info()