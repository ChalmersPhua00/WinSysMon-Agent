import subprocess
import sys

def launch_system_tool(tool_name):
    tools = {
        "taskmgr": "taskmgr.exe",
        "eventvwr": "eventvwr.msc",
        "services": "services.msc",
        "control": "control.exe",
        "regedit": "regedit.exe",
        "compmgmt": "compmgmt.msc",
        "sysdm": "sysdm.cpl",
        "resmon": "resmon.exe",
        "perfmon": "perfmon.msc"
    }
    tool_cmd = tools.get(tool_name.lower())
    if not tool_cmd:
        print(f"Tool '{tool_name}' not found in safe list. Available: {', '.join(tools.keys())}")
        return
    try:
        print(f"Launching {tool_name} ({tool_cmd})...")
        subprocess.Popen(tool_cmd, shell=True)
        print(f"Successfully launched {tool_name}.")
    except Exception as e:
        print(f"Error launching tool: {e}")

if __name__ == "__main__":
    launch_system_tool(sys.argv[1])