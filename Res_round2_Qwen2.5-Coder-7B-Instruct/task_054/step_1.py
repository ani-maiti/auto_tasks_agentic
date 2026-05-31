import requests

response = requests.get('https://worldtimeapi.org/api/ip')
if response.status_code == 200:
    data = response.json()
    utc_time = data['utc_datetime']
    print(utc_time)
else:
    print("Failed to retrieve UTC time")