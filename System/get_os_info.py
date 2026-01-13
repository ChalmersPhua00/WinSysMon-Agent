import subprocess

def get_os_info():
    try:
        cmd_info = 'Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, WindowsBuildLabEx, WindowsInstallationType, WindowsRegisteredOwner, TimeZone, BootupState, ThermalState, PowerPlatformRole | Format-List'
        info = subprocess.run(["powershell", "-Command", cmd_info], capture_output=True, text=True).stdout
        cmd_hotfix = 'Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10 HotFixID, Description, InstalledOn | Format-Table -AutoSize'
        hotfix = subprocess.run(["powershell", "-Command", cmd_hotfix], capture_output=True, text=True).stdout

        print(f"System Details\n```\n{info.strip()}\n```\nRecent Updates\n```\n{hotfix.strip()}\n```")
    except Exception as e:
        print(f"Error getting OS info: {e}")

if __name__ == "__main__":
    get_os_info()