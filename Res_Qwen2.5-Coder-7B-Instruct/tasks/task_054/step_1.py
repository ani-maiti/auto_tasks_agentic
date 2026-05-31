import requests

response = requests.get('https://worldtimeapi.org/api/ip')
if response.status_code == 200:
    data = response.json()
    utc_time = data['utc_datetime']
    print(f"Current UTC Time: {utc_time}")
else:
    print("Failed to retrieve UTC time")