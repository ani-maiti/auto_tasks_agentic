import requests

response = requests.get('https://worldtimeapi.org/api/ip')
if response.status_code == 200:
    print(response.json()['utc_datetime'])
else:
    print("Failed to retrieve data")