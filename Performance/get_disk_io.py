import subprocess

def get_disk_io():
    try:
        cmd_total = 'Get-Counter "\\PhysicalDisk(_Total)\\Disk Reads/sec", "\\PhysicalDisk(_Total)\\Disk Writes/sec", "\\PhysicalDisk(_Total)\\Disk Read Bytes/sec", "\\PhysicalDisk(_Total)\\Disk Write Bytes/sec", "\\PhysicalDisk(_Total)\\% Disk Time" | Select-Object -ExpandProperty CounterSamples | Select-Object Path, CookedValue | Format-Table -AutoSize'
        total = subprocess.run(["powershell", "-Command", cmd_total], capture_output=True, text=True).stdout
        cmd_disk = 'Get-Counter "\\PhysicalDisk(*)\\% Disk Time" | Select-Object -ExpandProperty CounterSamples | Where-Object {$_.InstanceName -ne "_total"} | Select-Object InstanceName, CookedValue | Format-Table -AutoSize'
        disk = subprocess.run(["powershell", "-Command", cmd_disk], capture_output=True, text=True).stdout
        
        print(f"Overall Disk I/O\n{total.strip()}\n\nPer-Disk Usage\n{disk.strip()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_disk_io()