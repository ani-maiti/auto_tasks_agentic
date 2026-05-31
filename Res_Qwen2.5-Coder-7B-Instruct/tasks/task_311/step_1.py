import os

# Step 1: Discover all log files
log_files = [f for f in os.listdir('.') if f.endswith('.log')]
print(f"Found {len(log_files)} log files.")