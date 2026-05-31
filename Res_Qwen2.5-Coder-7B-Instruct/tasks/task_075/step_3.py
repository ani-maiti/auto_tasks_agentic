import subprocess

result = subprocess.run(['curl', 'ifconfig.me'], capture_output=True, text=True)
stdout = result.stdout.strip()
print("The current public IP address is:", stdout)