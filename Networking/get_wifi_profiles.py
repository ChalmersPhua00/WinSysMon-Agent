import subprocess

def get_wifi_profiles():
    try:
        cmd = "netsh wlan show profiles"
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        
        print(f"WiFi Profiles\n{result.stdout}")
    except Exception as e:
        print(f"Error getting WiFi profiles: {str(e)}")

if __name__ == "__main__":
    get_wifi_profiles()