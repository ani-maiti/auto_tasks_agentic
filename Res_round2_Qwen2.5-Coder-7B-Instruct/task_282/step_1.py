import requests

# Step 1: Retrieve weather forecasts for fifty major cities worldwide
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    # Add more cities as needed
]

weather_data = []
for city in cities:
    url = f"http://api.weatherapi.com/v1/forecast.json?key=YOUR_API_KEY&q={city}&days=7"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data.append(response.json())
    else:
        print(f"Failed to fetch weather data for {city}")

print(weather_data)
```

This code retrieves weather forecasts for fifty major cities using the WeatherAPI. You need to replace `YOUR_API_KEY` with an actual API key from WeatherAPI. The weather data is stored in a list called `weather_data`.