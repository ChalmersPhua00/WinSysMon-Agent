import subprocess
import sys

def open_windows_settings(setting_uri):
    try:
        # Ensure the URI starts with ms-settings:
        if not setting_uri.startswith("ms-settings:"):
            setting_uri = f"ms-settings:{setting_uri}"
        print(f"Attempting to open settings page: {setting_uri}")
        # Use start command via shell to handle the URI protocol
        subprocess.run(["start", setting_uri], shell=True, check=True)
        print(f"Successfully launched settings window for: {setting_uri}")
    except Exception as e:
        print(f"Error opening settings: {e}")

if __name__ == "__main__":
    open_windows_settings(sys.argv[1])