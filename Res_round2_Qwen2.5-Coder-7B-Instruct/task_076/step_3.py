import requests

ip_response = requests.get('https://api.ipify.org?format=json')
if ip_response.status_code == 200:
    ip_data = ip_response.json()
    ip_address = ip_data['ip']
    geo_url = f"https://ipinfo.io/{ip_address}/json"
    geo_response = requests.get(geo_url)
    if geo_response.status_code == 200:
        geo_data = geo_response.json()
        print(f"Geolocation information for {ip_address}:")
        print(geo_data)
    else:
        print(f"Failed to retrieve geolocation information for {ip_address}")
else:
    print("Failed to retrieve IP address")