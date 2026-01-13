import wmi

def disk_usage():
    c = wmi.WMI()

    print(f"{'Drive':<10} {'Size (GB)':<10} {'Free (GB)'}")
    print("-" * 30)

    for disk in c.Win32_LogicalDisk():
        # Skip drives with no size (eg. empty CD-ROM)
        if not disk.Size:
            continue
        # Convert bytes to GB
        size_gb = float(disk.Size) / (1024**3)
        free_gb = float(disk.FreeSpace) / (1024**3)
        print(f"{disk.DeviceID:10} {size_gb:<10.2f} {free_gb:<10.2f}")

if __name__ == "__main__":
    disk_usage()