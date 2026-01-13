import subprocess
import sys

def ping_host(host, count):
    try:
        cmd = f"ping -n {count} {host}"
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)

        print(f"Target: {host}\nCount: {count}\n{result.stdout}")
    except Exception as e:
        print(f"Error pinging host: {str(e)}")

if __name__ == "__main__":
    ping_host(sys.argv[1], sys.argv[2])