import wmi

def list_processes():
    c = wmi.WMI()
    
    print(f"{'PID':<10} {'Name':<30} {'PPID':<20} {'CommandLine'}")
    print("-" * 90)
    
    for process in c.Win32_Process():
        pid = process.ProcessId
        name = process.Name
        ppid = process.ParentProcessId
        cmd = process.CommandLine if process.CommandLine else ""
        # Truncate long command lines for cleaner output
        if len(cmd) > 40:
            cmd = cmd[:37] + "..."
        print(f"{pid:<10} {name:<30} {ppid:<20} {cmd}")

if __name__ == "__main__":
    list_processes()