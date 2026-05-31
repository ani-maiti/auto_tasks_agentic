import subprocess

# Use git command to fetch contributors from the requests GitHub repository
result = subprocess.run(['git', 'shortlog', '-sne'], capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Print the number of contributors
    print("Number of contributors:", len(result.stdout.splitlines()))
else:
    # Print an error message if the command failed
    print("Failed to retrieve contributors:", result.stderr)