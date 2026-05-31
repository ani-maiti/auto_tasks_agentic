import subprocess

result = subprocess.run(['ls', '-d', '*'], capture_output=True, text=True)
directories = [line for line in result.stdout.split('\n') if line.endswith('/')]
print("Number of directories:", len(directories))