import requests
import json

cities = [
    "New York", "London", "Tokyo", "Sydney", "Paris",
    "Berlin", "Rome", "Oslo", "Istanbul", "Mumbai",
    "Delhi", "Shanghai", "Seoul", "Bangkok", "Cairo",
    "Doha", "São Paulo", "Mexico City", "Copenhagen"
]

weather_data = []

for city in cities:
    url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data.append(response.json())
    else:
        print(f"Failed to fetch weather data for {city}")

with open("weather_data.json", "w") as file:
    json.dump(weather_data, file)

print("Weather data saved to weather_data.json")