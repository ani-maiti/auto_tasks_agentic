import requests
import json

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

weather_data = {}

for city in cities:
    url = f"http://api.weatherapi.com/v1/forecast.json?key=YOUR_API_KEY&q={city}&days=7"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data[city] = response.json()
    else:
        print(f"Failed to fetch weather data for {city}")

with open("weather_data.json", "w") as file:
    json.dump(weather_data, file, indent=4)

print("Weather data saved to weather_data.json")