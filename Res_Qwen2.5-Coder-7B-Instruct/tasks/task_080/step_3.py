import json
import subprocess

response = subprocess.run(['curl', '-s', 'https://api.github.com/repos/psf/requests'], capture_output=True, text=True)
data = json.loads(response.stdout)
forks_count = data['forks_count']
print(f"The number of forks for the requests GitHub repository is: {forks_count}")