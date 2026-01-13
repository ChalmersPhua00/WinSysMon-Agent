import subprocess

def get_system_performance():
    try:
        cmd_perf = 'Get-Counter "\\Processor(_Total)\\% Processor Time", "\\Memory\\Available MBytes", "\\PhysicalDisk(_Total)\\% Disk Time", "\\System\\Processor Queue Length", "\\System\\Context Switches/sec" | Select-Object -ExpandProperty CounterSamples | Select-Object Path, CookedValue | Format-Table -AutoSize'
        perf = subprocess.run(["powershell", "-Command", cmd_perf], capture_output=True, text=True).stdout
        cmd_uptime = 'Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object LastBootUpTime, @{Name="UptimeHours";Expression={(Get-Date) - $_.LastBootUpTime | Select-Object -ExpandProperty TotalHours}} | Format-List'
        uptime = subprocess.run(["powershell", "-Command", cmd_uptime], capture_output=True, text=True).stdout
        
        print(f"Key Performance Indicators\n```\n{perf.strip()}\n```\nSystem Uptime\n```\n{uptime.strip()}\n```")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_system_performance()