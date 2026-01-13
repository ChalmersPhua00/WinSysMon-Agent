import subprocess

def get_startup_programs_registry():
    try:
        locations = [
            "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
            "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
            "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
            "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce"
        ]

        print("Startup Programs from Registry\n")
        for location in locations:
            cmd = f'Get-ItemProperty -Path "Registry::{location}" -ErrorAction SilentlyContinue | Format-List'
            result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True).stdout
            if result.strip():
                print(f"{location}\n```\n{result.strip()}\n```\n")
            else:
                print(f"{location}\n*No entries or access denied*\n")
    except Exception as e:
        print(f"Error getting startup programs: {e}")

if __name__ == "__main__":
    get_startup_programs_registry()