import requests
import json

# List of ten major cities
cities = [
    "New York", "London", "Tokyo", "Paris", "Sydney",
    "Dubai", "Moscow", "Rio de Janeiro", "Cairo", "Mumbai"
]

# OpenWeatherMap API key (using a free tier key)
api_key = "YOUR_API_KEY_HERE"

# Store raw responses
raw_responses = {}

# Retrieve weather data for each city
for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        raw_responses[city] = response.json()
        print(f"Retrieved data for {city}")
    except Exception as e:
        print(f"Error retrieving data for {city}: {e}")

# Save raw responses to files
for city, data in raw_responses.items():
    with open(f"{city}_weather.json", "w") as f:
        json.dump(data, f, indent=2)

print("All raw responses saved.")