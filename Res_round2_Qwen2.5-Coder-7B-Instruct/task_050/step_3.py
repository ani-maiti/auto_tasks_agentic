import subprocess

result = subprocess.run(['du', '-sh', '.'], capture_output=True, text=True)
stdout = result.stdout.strip()
print("Total disk usage:", stdout.split()[0])