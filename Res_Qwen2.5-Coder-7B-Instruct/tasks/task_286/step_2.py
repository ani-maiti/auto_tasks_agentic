with open('log_files.txt', 'r') as file:
    log_files = file.read().splitlines()
print(f"Found {len(log_files)} log files.")