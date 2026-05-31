import requests
import json

# Step 1: Retrieve weather forecasts for one hundred cities
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"] * 20  # Example list of cities
weather_data = []

for city in cities:
    url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data.append(response.json())
    else:
        print(f"Failed to fetch weather data for {city}")

# Save the weather data to a JSON file
with open("weather_data.json", "w") as f:
    json.dump(weather_data, f)

print("Weather data retrieved and saved to weather_data.json")
```

This code retrieves weather forecasts for a list of cities and saves them to a JSON file. You need to replace `YOUR_API_KEY` with an actual API key from WeatherAPI or another weather service provider.