# Define the list of modified files
modified_files = [f for f in os.listdir() if os.path.getmtime(f) >= seven_days_ago.timestamp()]

# Print the list of modified files again
for f in modified_files:
    print(f)