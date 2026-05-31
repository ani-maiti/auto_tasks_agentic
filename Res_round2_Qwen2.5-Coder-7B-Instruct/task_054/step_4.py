import requests

# Use a different public API to avoid potential issues with the first one
response = requests.get('http://worldtimeapi.org/api/ip', timeout=10)
if response.status_code == 200:
    data = response.json()
    utc_time = data['utc_datetime']
    print(utc_time)
else:
    print("Failed to retrieve UTC time")