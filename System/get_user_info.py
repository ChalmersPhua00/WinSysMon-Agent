import subprocess

def get_user_info():
    try:
        cmd_users = 'Get-WmiObject -Class Win32_UserAccount | Select-Object Name, FullName, Description, Disabled, LocalAccount, SID | Format-Table -AutoSize'
        users = subprocess.run(["powershell", "-Command", cmd_users], capture_output=True, text=True).stdout
        cmd_current = 'whoami /all'
        current = subprocess.run(cmd_current, capture_output=True, text=True, shell=True).stdout
        
        print(f"Current User Details\n```\n{current.strip()}\n```\nAll User Accounts\n```\n{users.strip()}\n```")
    except Exception as e:
        print(f"Error getting user info: {e}")

if __name__ == "__main__":
    get_user_info()