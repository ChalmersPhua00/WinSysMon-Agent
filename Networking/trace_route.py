import subprocess
import sys

def trace_route(host):
    try:
        cmd = f"tracert {host}"
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)

        print(f"Traceroute Results\nTarget: {host}\n{result.stdout}")
    except Exception as e:
        print(f"Error tracing route: {str(e)}")

if __name__ == "__main__":
    trace_route(sys.argv[1])
