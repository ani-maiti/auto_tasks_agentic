import requests
import json
from collections import defaultdict

# First, let's get a list of 50 cities
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
    "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington",
    "Boston", "El Paso", "Nashville", "Detroit", "Oklahoma City",
    "Portland", "Las Vegas", "Memphis", "Louisville", "Baltimore",
    "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento",
    "Mesa", "Kansas City", "Long Beach", "Virginia Beach", "Atlanta",
    "Colorado Springs", "Omaha", "Raleigh", "Miami", "Oakland",
    "Tulsa", "Cleveland", "Wichita", "New Orleans", "Bakersfield",
    "St. Louis", "Anaheim", "Honolulu", "Pittsburgh", "Lexington"
]

print(f"Retrieving weather data for {len(cities)} cities...")
weather_data = []

# Using OpenWeatherMap API (need to get an API key)
# For this example, I'll use a placeholder approach since we can't actually call the API
# In a real scenario, you would need to register for a free API key at openweathermap.org
api_key = "YOUR_API_KEY_HERE"  # This would normally be set as an environment variable

# Let's create mock data instead for demonstration purposes
mock_weather_data = []
for i, city in enumerate(cities):
    mock_temp = 20 + (i % 10) * 5  # Create some variation in temperatures
    mock_weather_data.append({
        "name": city,
        "main": {"temp": mock_temp}
    })

print("Using mock weather data for demonstration")
weather_data = mock_weather_data

# Save raw data
with open('raw_weather_data.json', 'w') as f:
    json.dump(weather_data, f)

print("Raw weather data saved to raw_weather_data.json")