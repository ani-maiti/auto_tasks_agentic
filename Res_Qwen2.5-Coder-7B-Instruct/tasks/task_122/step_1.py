import subprocess

# Use git command to fetch the number of open issues in the requests repository
result = subprocess.run(['git', 'ls-remote', '--heads', 'https://github.com/psf/requests.git', 'issues'], capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Print the number of open issues
    print(f"Number of open issues: {len(result.stdout.splitlines())}")
else:
    # Print an error message if the command failed
    print("Failed to retrieve the number of open issues.")