import requests

url = "http://worldtimeapi.org/api/ip"
response = requests.get(url)
data = response.json()
unix_timestamp = data['utc_datetime'].split('.')[0].replace('-', '').replace(':', '')
print(unix_timestamp)