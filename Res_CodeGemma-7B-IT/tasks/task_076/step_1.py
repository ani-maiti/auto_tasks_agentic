import requests

response = requests.get("https://ipapi.co/json/")
data = response.json()

print(f"Your IP address is {data['ip']}")
print(f"Your city is {data['city']}")
print(f"Your region is {data['region_name']}")
print(f"Your country is {data['country_name']}")
print(f"Your timezone is {data['timezone']}")