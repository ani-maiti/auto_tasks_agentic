from datetime import datetime, timedelta

# Calculate the timestamp for files modified within the last 24 hours
cutoff_time = datetime.now() - timedelta(hours=24)

# Use the `find` command to list files modified after the cutoff time
command = f"find . -type f -mtime +{cutoff_time.timestamp()}"

# Execute the command and capture the output
output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Print the output to the console
print(output.stdout.decode())