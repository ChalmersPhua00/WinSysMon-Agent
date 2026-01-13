import subprocess
import sys

def get_performance_counters(counter_name):
    try:
        if counter_name:
            cmd = f'Get-Counter "{counter_name}" | Select-Object -ExpandProperty CounterSamples | Select-Object Path, CookedValue, RawValue | Format-List'
            title = f"Performance Counter: {counter_name}"
        else:
            cmd = 'Get-Counter -ListSet * | Select-Object CounterSetName, Description | Sort-Object CounterSetName | Format-Table -AutoSize'
            title = "Available Performance Counter Categories"
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(f"{title}\n```\n{result.strip()}\n```")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    counter_name = sys.argv[1]
    get_performance_counters(counter_name)