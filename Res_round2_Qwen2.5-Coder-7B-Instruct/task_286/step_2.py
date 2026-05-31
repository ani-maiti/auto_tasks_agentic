with open('log_files.txt', 'r') as f:
    log_files = f.read().splitlines()
print(f"Found {len(log_files)} log files.")