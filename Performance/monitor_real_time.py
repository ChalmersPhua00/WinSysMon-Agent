import subprocess
import sys

def monitor_real_time(duration, interval):
    try:
        cmd = f'$samples = @(); for($i=1; $i -le {duration}; $i++) {{ $cpu = Get-Counter "\\Processor(_Total)\\% Processor Time" -MaxSamples 1; $mem = Get-Counter "\\Memory\\Available MBytes" -MaxSamples 1; $samples += "Sample $i - CPU: $([math]::Round($cpu.CounterSamples.CookedValue,2))% Memory Available: $([math]::Round($mem.CounterSamples.CookedValue,2))MB"; Start-Sleep {interval} }}; $samples'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"Real-time Performance Monitoring\nDuration: {duration} seconds\nInterval: {interval} second(s)\n```\n{result.strip()}\n```")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    duration = sys.argv[1]
    interval = sys.argv[2]
    monitor_real_time(duration, interval)