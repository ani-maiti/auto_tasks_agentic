import glob

# Step 2: Discover all log files again, this time using glob
log_files = glob.glob('*.log')
print(f"Found {len(log_files)} log files.")