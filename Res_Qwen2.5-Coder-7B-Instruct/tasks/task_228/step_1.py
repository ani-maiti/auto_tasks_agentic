import requests
import json

cities = [
    "New York", "London", "Tokyo", "Sydney", "Paris",
    "Berlin", "Rome", "Oslo", "Istanbul", "Mumbai",
    "Delhi", "Shanghai", "Seoul", "Bangkok", "Cairo",
    "Sao Paulo", "Mexico City", "Dhaka", "Karachi"
]

weather_data = []

for city in cities:
    url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data.append(response.json())
    else:
        print(f"Failed to get weather data for {city}")

with open("weather_data.json", "w") as f:
    json.dump(weather_data, f)

print("Weather data saved to weather_data.json")
```

Replace `YOUR_API_KEY` with your actual WeatherAPI key. This script retrieves current weather data for twenty major cities and saves it to a JSON file.