import subprocess
import time
import psutil

def format_uptime(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{int(days)}d {int(hours)}h {int(minutes)}m {int(secs)}s"

def get_system_uptime_info():
    try:
        cmd = 'Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object LastBootUpTime, LocalDateTime | Format-List'
        stdout = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout
        uptime_seconds = time.time() - psutil.boot_time()

        print(f"Current Uptime: {format_uptime(uptime_seconds)}\nBoot Information\n```\n{stdout.strip()}\n```")
    except Exception as e:
        print(f"Error getting system uptime: {e}")

if __name__ == "__main__":
    get_system_uptime_info()