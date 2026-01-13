import subprocess

def get_system_info_registry():
    try:
        system_keys = [
            {
                "name": "Windows Version",
                "path": "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
                "values": ["ProductName", "ReleaseId", "CurrentBuild", "UBR"]
            },
            {
                "name": "Computer Info",
                "path": "HKLM\\SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ComputerName",
                "values": ["ComputerName"]
            },
            {
                "name": "Processor Info",
                "path": "HKLM\\HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0",
                "values": ["ProcessorNameString", "~MHz"]
            }
        ]
        
        print("System Information from Registry\n")
        for key_info in system_keys:
            print(f"{key_info['name']}")
            for value_name in key_info['values']:
                try:
                    cmd = f'Get-ItemPropertyValue -Path "Registry::{key_info["path"]}" -Name "{value_name}" -ErrorAction SilentlyContinue'
                    result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout
                    if result.strip():
                        print(f"-{value_name}: {result.strip()}")
                except:
                    print(f"-{value_name}: *Not available*")
            print()
    except Exception as e:
        print(f"Error getting system info from registry: {e}")

if __name__ == "__main__":
    get_system_info_registry()