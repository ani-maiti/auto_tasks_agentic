import requests

# List of European capital cities
capital_cities = [
    "Amsterdam", "Athens", "Berlin", "Brussels", "Bucharest",
    "Copenhagen", "Dublin", "Helsinki", "Istanbul", "London",
    "Madrid", "Paris", "Prague", "Rome", "Stockholm", "Vienna"
]

# Function to get weather data for a city
def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Retrieve weather data for all capital cities
weather_data = {}
for city in capital_cities:
    data = get_weather(city)
    if data:
        weather_data[city] = data['main']['temp']

# Save responses to a file
with open("weather_data.json", "w") as f:
    import json
    json.dump(weather_data, f)

print("Weather data retrieved and saved.")
```

This script retrieves the current weather data for each capital city in Europe using the OpenWeatherMap API and saves it to a JSON file. Make sure to replace `YOUR_API_KEY` with an actual API key from OpenWeatherMap.