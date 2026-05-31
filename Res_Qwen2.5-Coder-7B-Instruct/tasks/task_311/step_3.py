import os

# Step 3: Search subdirectories for log files
log_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.log'):
            log_files.append(os.path.join(root, file))
print(f"Found {len(log_files)} log files.")