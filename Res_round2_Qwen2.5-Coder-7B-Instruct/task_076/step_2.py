import requests

url = f"https://ipinfo.io/{ip_address}/json"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Geolocation information for {ip_address}:")
    print(data)
else:
    print(f"Failed to retrieve geolocation information for {ip_address}")