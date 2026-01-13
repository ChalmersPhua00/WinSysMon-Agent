import subprocess
import sys

def get_service_details(service_name):
    try:
        # Basic Info
        cmd_basic = f'Get-Service -Name "{service_name}" -ErrorAction Stop | Select-Object * | Format-List'
        basic_info = subprocess.run(["powershell", "-Command", cmd_basic], capture_output=True, text=True).stdout
        # WMI Info (Using Get-CimInstance as modern replacement for Get-WmiObject, or fallback to WmiObject logic)
        # The original code used Get-WmiObject.
        cmd_wmi = f'Get-WmiObject -Class Win32_Service -Filter "Name=\'{service_name}\'" | Select-Object Name, DisplayName, Description, PathName, StartMode, StartName, State, ProcessId, ServiceType | Format-List'
        wmi_info = subprocess.run(["powershell", "-Command", cmd_wmi], capture_output=True, text=True).stdout
        # Dependencies
        cmd_dep = f'Get-Service -Name "{service_name}" | Select-Object -ExpandProperty ServicesDependedOn | Select-Object Name, Status | Format-Table -AutoSize'
        dependencies = subprocess.run(["powershell", "-Command", cmd_dep], capture_output=True, text=True).stdout

        print(f"Service Details: {service_name}\n")
        print(f"Basic Information\n```\n{basic_info.strip()}\n```\n")
        print(f"Extended Information\n```\n{wmi_info.strip()}\n```\n")
        print(f"Dependencies\n```\n{dependencies.strip()}\n```")
    except Exception as e:
        print(f"Error getting details for {service_name}: {e}")

if __name__ == "__main__":
    get_service_details(sys.argv[1])