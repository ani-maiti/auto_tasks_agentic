import subprocess

result = subprocess.run(['openssl', 's_client', '-connect', 'github.com:443'], capture_output=True, text=True)
ssl_date = result.stdout.split('notAfter=')[1].split('\n')[0]
print(f"SSL certificate expiration date for github.com: {ssl_date}")