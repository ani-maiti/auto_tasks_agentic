import requests

# Disable SSL verification for testing purposes
response = requests.get('https://worldtimeapi.org/api/ip', timeout=10, verify=False)
if response.status_code == 200:
    data = response.json()
    utc_time = data['utc_datetime']
    print(utc_time)
else:
    print("Failed to retrieve UTC time")