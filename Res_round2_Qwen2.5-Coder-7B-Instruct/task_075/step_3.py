import requests

response = requests.get('https://api.ipify.org?format=json')
print("The current public IP address is:", response.json()['ip'])