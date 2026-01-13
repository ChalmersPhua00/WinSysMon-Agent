import subprocess
import sys
import platform

def get_cpu_usage(duration):
    try:
        # CPU Info
        cpu_model = platform.processor()
        # Get core count via PowerShell for accuracy regarding logical processors
        cpu_count_cmd = "(Get-CimInstance Win32_Processor).NumberOfLogicalProcessors"
        cpu_count = subprocess.run(["powershell", "-Command", cpu_count_cmd], capture_output=True, text=True).stdout.strip()
        # Overall Usage
        cmd_overall = f'Get-Counter "\\Processor(_Total)\\% Processor Time" -SampleInterval 1 -MaxSamples {duration} | Select-Object -ExpandProperty CounterSamples | Select-Object CookedValue | Measure-Object -Property CookedValue -Average -Maximum -Minimum | Format-List'
        overall = subprocess.run(["powershell", "-Command", cmd_overall], capture_output=True, text=True).stdout
        # Per Core
        cmd_core = 'Get-Counter "\\Processor(*)\\% Processor Time" -MaxSamples 1 | Select-Object -ExpandProperty CounterSamples | Where-Object {$_.InstanceName -ne "_total"} | Select-Object InstanceName, CookedValue | Format-Table -AutoSize'
        core = subprocess.run(["powershell", "-Command", cmd_core], capture_output=True, text=True).stdout

        print(f"CPU Model: {cpu_model}")
        print(f"Cores: {cpu_count}")
        print(f"Monitoring Duration: {duration} seconds\n")
        print(f"Overall CPU Usage Statistics\n{overall.strip()}\n")
        print(f"Per-Core Usage (Current)\n{core.strip()}")
    except Exception as e:
        print(f"Error getting CPU usage: {e}")

if __name__ == "__main__":
    duration = sys.argv[1]
    get_cpu_usage(duration)