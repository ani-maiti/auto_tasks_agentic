import requests

response = requests.get('https://api.ipify.org?format=json')
public_ip = response.json()['ip']
geo_response = requests.get(f'https://ipinfo.io/{public_ip}/json')
print(geo_response.json())