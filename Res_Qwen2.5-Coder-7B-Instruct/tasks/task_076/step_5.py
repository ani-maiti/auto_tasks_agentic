import requests

response = requests.get('https://api.ipify.org?format=json')
public_ip = response.json()['ip']
geo_response = requests.get(f'https://ipinfo.io/{public_ip}/json')
geo_info = geo_response.json()
print(json.dumps(geo_info, indent=2))