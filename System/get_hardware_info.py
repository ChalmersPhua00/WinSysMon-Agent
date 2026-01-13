import subprocess
import sys

def get_hardware_info(category):
    try:
        if category == "all" or category == "cpu":
            cmd = 'Get-WmiObject -Class Win32_Processor | Select-Object Name, Manufacturer, MaxClockSpeed, NumberOfCores, NumberOfLogicalProcessors, Architecture | Format-List'
            result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout
            print(f"CPU Information\n```\n{result.strip()}\n```\n")
        if category == "all" or category == "memory":
            cmd = 'Get-WmiObject -Class Win32_PhysicalMemory | Select-Object Manufacturer, Capacity, Speed, MemoryType, FormFactor | Format-Table -AutoSize'
            result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout
            print(f"Memory Information\n```\n{result.strip()}\n```\n")
        if category == "all" or category == "disk":
            cmd = 'Get-WmiObject -Class Win32_DiskDrive | Select-Object Model, Size, MediaType, InterfaceType | Format-Table -AutoSize'
            result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout
            print(f"Disk Information\n```\n{result.strip()}\n```\n")
        if category == "all" or category == "network":
            cmd = 'Get-WmiObject -Class Win32_NetworkAdapter | Where-Object {$_.NetConnectionStatus -eq 2} | Select-Object Name, MACAddress, Speed, AdapterType | Format-Table -AutoSize'
            result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout
            print(f"Network Adapters\n```\n{result.strip()}\n```")
    except Exception as e:
        print(f"Error getting hardware info: {e}")

if __name__ == "__main__":
    get_hardware_info(sys.argv[1])