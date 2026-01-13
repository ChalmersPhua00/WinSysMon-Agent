import subprocess
import sys

def get_ram_usage():
    try:
        # Summary via WMI/CIM
        cmd_summary = 'Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory | Format-List'
        summary_out = subprocess.run(["powershell", "-Command", cmd_summary], capture_output=True, text=True).stdout
        total_kb = 0
        free_kb = 0
        for line in summary_out.splitlines():
            if "TotalVisibleMemorySize" in line:
                parts = line.split(":")
                if len(parts) > 1: total_kb = int(parts[1].strip())
            if "FreePhysicalMemory" in line:
                parts = line.split(":")
                if len(parts) > 1: free_kb = int(parts[1].strip())

        if total_kb > 0:
            total_gb = total_kb / (1024*1024)
            free_gb = free_kb / (1024*1024)
            used_gb = total_gb - free_gb
            percent = (used_gb / total_gb) * 100
            print(f"-Total RAM: {total_gb:.2f} GB")
            print(f"-Used RAM: {used_gb:.2f} GB")
            print(f"-Free RAM: {free_gb:.2f} GB")
            print(f"-RAM Usage Percentage: {percent:.2f}%\n")

        # Detailed Counters
        cmd_counters = 'Get-Counter "\\Memory\\Available MBytes", "\\Memory\\Committed Bytes", "\\Memory\\Pool Nonpaged Bytes", "\\Memory\\Pool Paged Bytes" | Select-Object -ExpandProperty CounterSamples | Select-Object Path, CookedValue | Format-Table -AutoSize'
        counters = subprocess.run(["powershell", "-Command", cmd_counters], capture_output=True, text=True).stdout
        # Top Processes
        cmd_proc = 'Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10 Name, @{Name="MemoryMB";Expression={[math]::Round($_.WorkingSet/1MB,2)}} | Format-Table -AutoSize'
        procs = subprocess.run(["powershell", "-Command", cmd_proc], capture_output=True, text=True).stdout

        print(f"Detailed Committed Bytes (Virtual Memory) Counters\n{counters.strip()}\n")
        print(f"Top 10 Processes by RAM Usage\n{procs.strip()}")
    except Exception as e:
        print(f"Error getting RAM usage: {e}")

if __name__ == "__main__":
    get_ram_usage()