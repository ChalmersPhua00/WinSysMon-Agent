import subprocess

def get_network_io():
    try:
        cmd_total = 'Get-Counter "\\Network Interface(*)\\Bytes Total/sec" | Select-Object -ExpandProperty CounterSamples | Where-Object {$_.CookedValue -gt 0} | Select-Object InstanceName, CookedValue | Format-Table -AutoSize'
        total = subprocess.run(["powershell", "-Command", cmd_total], capture_output=True, text=True).stdout
        cmd_detail = 'Get-Counter "\\Network Interface(*)\\Bytes Received/sec", "\\Network Interface(*)\\Bytes Sent/sec" | Select-Object -ExpandProperty CounterSamples | Where-Object {$_.CookedValue -gt 0} | Select-Object InstanceName, Path, CookedValue | Format-Table -AutoSize'
        detail = subprocess.run(["powershell", "-Command", cmd_detail], capture_output=True, text=True).stdout
        
        print(f"Total Network Traffic\n```\n{total.strip()}\n```\nDetailed Network Statistics\n```\n{detail.strip()}\n```")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_network_io()