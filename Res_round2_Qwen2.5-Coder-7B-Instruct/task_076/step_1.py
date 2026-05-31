import requests

response = requests.get('https://api.ipify.org?format=json')
if response.status_code == 200:
    data = response.json()
    ip_address = data['ip']
    print(f"Current public IP address: {ip_address}")
else:
    print("Failed to retrieve IP address")