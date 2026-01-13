import subprocess
import platform
import psutil
import time

def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return f"{size:.2f} {power_labels[n]}"

def format_uptime(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{int(days)}d {int(hours)}h {int(minutes)}m {int(secs)}s"

def get_system_overview():
    try:
        uptime_seconds = time.time() - psutil.boot_time()
        cmd = 'Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, TotalPhysicalMemory, CsProcessors, CsSystemType, TimeZone | Format-List'
        stdout = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"-Hostname: {platform.node()}")
        print(f"-Platform: {platform.system()}")
        print(f"-Architecture: {platform.machine()}")
        print(f"-CPU Cores: {psutil.cpu_count()}")
        print(f"-Total Memory: {format_bytes(psutil.virtual_memory().total)}")
        print(f"-Free Memory: {format_bytes(psutil.virtual_memory().available)}")
        print(f"-System Uptime: {format_uptime(uptime_seconds)}\n")
        print(f"Windows Details\n```\n{stdout.strip()}\n```")
    except Exception as e:
        print(f"Error getting system overview: {e}")

if __name__ == "__main__":
    get_system_overview()