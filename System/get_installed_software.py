import subprocess

def get_installed_software():
    try:
        cmd = r'''$paths = @("HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*", "HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*")
        Get-ItemProperty $paths | Where-Object { $_.DisplayName } | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Sort-Object DisplayName | Format-Table -AutoSize'''
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout

        print(result.strip())
    except Exception as e:
        print(f"Error getting installed software: {e}")

if __name__ == "__main__":
    get_installed_software()