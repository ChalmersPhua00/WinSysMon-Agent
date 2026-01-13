import os
import sys

def find_large_files(search_path, size_threshold_mb):
    print(f"Large Files (>{size_threshold_mb}MB)")
    print(f"Search Path: {search_path}")

    threshold_bytes = int(size_threshold_mb) * 1024 * 1024
    results = []

    for root, _, files in os.walk(search_path):
        for name in files:
            try:
                filepath = os.path.join(root, name)
                size = os.path.getsize(filepath)
                if size > threshold_bytes:
                    results.append((filepath, size))
            except OSError:
                continue

    # Sort by size descending
    results.sort(key=lambda x: x[1], reverse=True)
    print(f"\n{'Size (MB)':<15} {'File Path'}")
    print("-" * 80)

    for filepath, size in results:
        size_mb = size / (1024 * 1024)
        print(f"{size_mb:<15.2f} {filepath}")

if __name__ == "__main__":
    find_large_files(sys.argv[1], sys.argv[2])