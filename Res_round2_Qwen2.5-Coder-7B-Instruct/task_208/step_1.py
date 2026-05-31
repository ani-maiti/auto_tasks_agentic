import requests

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

api_key = "YOUR_API_KEY_HERE"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

responses = {}

for city in cities:
    url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        responses[city] = response.json()
    else:
        print(f"Failed to get weather data for {city}")

print("Weather data retrieved.")