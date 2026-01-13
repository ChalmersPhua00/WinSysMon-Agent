import subprocess

def get_installed_programs_registry():
    try:
        locations = [
            "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall",
            "HKLM\\SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall",
            "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall"
        ]
        
        print("Installed Programs from Registry\n")
        for location in locations:
            cmd = f'Get-ChildItem -Path "Registry::{location}" -ErrorAction SilentlyContinue | Get-ItemProperty | Where-Object {{$_.DisplayName}} | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Sort-Object DisplayName | Format-Table -AutoSize'
            result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout
            if result.strip():
                print(f"{location}\n```\n{result.strip()}\n```\n")
            else:
                print(f"{location}\n*No entries or access denied*\n")
    except Exception as e:
        print(f"Error getting installed programs: {e}")

if __name__ == "__main__":
    get_installed_programs_registry()