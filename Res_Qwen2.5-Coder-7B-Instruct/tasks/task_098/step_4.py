import subprocess

result = subprocess.run(['openssl', 's_client', '-connect', 'github.com:443'], capture_output=True, text=True)
output = result.stdout
if "notAfter=" in output:
    ssl_date = output.split('notAfter=')[1].strip().split('\n')[0]
else:
    ssl_date = "Date not found"
print(f"SSL certificate expiration date for github.com: {ssl_date}")