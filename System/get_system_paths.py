import os

def get_system_paths():
    try:
        path_info = {
            "systemRoot": os.environ.get("SystemRoot", "N/A"),
            "programFiles": os.environ.get("ProgramFiles", "N/A"),
            "programFilesX86": os.environ.get("ProgramFiles(x86)", "N/A"),
            "userProfile": os.environ.get("USERPROFILE", "N/A"),
            "appData": os.environ.get("APPDATA", "N/A"),
            "localAppData": os.environ.get("LOCALAPPDATA", "N/A"),
            "temp": os.environ.get("TEMP", "N/A"),
            "winDir": os.environ.get("windir", "N/A")
        }
        path_env = os.environ.get("PATH", "").split(';')
        path_env_display = "\n".join(path_env[:20]) if path_env else "N/A"
        
        print("Important Directories")
        for key, value in path_info.items():
            # Convert camelCase key to Title Case for display
            display_key = key.replace("X86", " (x86)").replace("appData", "AppData").replace("winDir", "Windows Directory").replace("systemRoot", "System Root").replace("programFiles", "Program Files").replace("userProfile", "User Profile").replace("localAppData", "Local AppData").replace("temp", "Temp")
            print(f"-{display_key}: {value}")
        print(f"\nPATH Environment (First 20 entries)\n```\n{path_env_display}\n```")
    except Exception as e:
        print(f"Error getting system paths: {e}")

if __name__ == "__main__":
    get_system_paths()