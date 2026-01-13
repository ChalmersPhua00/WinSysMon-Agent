import subprocess
import sys

def get_top_processes_mem(count):
    try:
        cmd = f'Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First {count} Name, Id, @{{Name="MemoryMB";Expression={{[math]::Round($_.WorkingSet/1MB,2)}}}}, @{{Name="CPU%";Expression={{$_.CPU}}}}, StartTime | Format-Table -AutoSize'
        title = f"Top {count} Processes by Memory Usage"
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout
        
        print(f"{title}\n```\n{result.strip()}\n```")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    count = sys.argv[1]
    get_top_processes_mem(count)