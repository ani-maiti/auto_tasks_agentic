import requests
response = requests.get('https://worldtimeapi.org/api/ip')
data = response.json()
print(data['utc_datetime'])