import os
import requests
import json
from collections import defaultdict

# Check if API key is available
api_key = os.getenv('OPENWEATHER_API_KEY')
if not api_key:
    print("Error: OPENWEATHER_API_KEY environment variable not set")
    print("Please set your API key as an environment variable:")
    print("export OPENWEATHER_API_KEY='your_api_key_here'")
    exit(1)

# List of 20 major cities with their countries and continents
cities = [
    {"name": "New York", "country": "US", "continent": "North America"},
    {"name": "London", "country": "GB", "continent": "Europe"},
    {"name": "Tokyo", "country": "JP", "continent": "Asia"},
    {"name": "Sydney", "country": "AU", "continent": "Australia"},
    {"name": "Paris", "country": "FR", "continent": "Europe"},
    {"name": "Berlin", "country": "DE", "continent": "Europe"},
    {"name": "Moscow", "country": "RU", "continent": "Europe"},
    {"name": "Dubai", "country": "AE", "continent": "Asia"},
    {"name": "Singapore", "country": "SG", "continent": "Asia"},
    {"name": "Toronto", "country": "CA", "continent": "North America"},
    {"name": "Mexico City", "country": "MX", "continent": "North America"},
    {"name": "São Paulo", "country": "BR", "continent": "South America"},
    {"name": "Cairo", "country": "EG", "continent": "Africa"},
    {"name": "Johannesburg", "country": "ZA", "continent": "Africa"},
    {"name": "Seoul", "country": "KR", "continent": "Asia"},
    {"name": "Bangkok", "country": "TH", "continent": "Asia"},
    {"name": "Istanbul", "country": "TR", "continent": "Europe"},
    {"name": "Rome", "country": "IT", "continent": "Europe"},
    {"name": "Madrid", "country": "ES", "continent": "Europe"},
    {"name": "Athens", "country": "GR", "continent": "Europe"}
]

# Function to get weather data for a city
def get_weather_data(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get data for {city_name}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data for {city_name}: {e}")
        return None

# Retrieve weather data for all cities
weather_data = []
for city in cities:
    data = get_weather_data(city["name"])
    if data:
        # Add continent info to the data
        data["continent"] = city["continent"]
        weather_data.append(data)
        print(f"Retrieved data for {city['name']}")
    else:
        print(f"Could not retrieve data for {city['name']}")

# Save all responses to JSON file
with open('weather_data.json', 'w') as f:
    json.dump(weather_data, f, indent=2)

print(f"Saved weather data for {len(weather_data)} cities to weather_data.json")

# Calculate average temperature by continent
continent_temps = defaultdict(list)
for data in weather_data:
    continent = data["continent"]
    temp = data["main"]["temp"]
    continent_temps[continent].append(temp)

# Compute averages
continent_averages = {}
for continent, temps in continent_temps.items():
    avg_temp = sum(temps) / len(temps)
    continent_averages[continent] = round(avg_temp, 2)

# Find the warmest continent
warmest_continent = max(continent_averages, key=continent_averages.get)
warmest_temp = continent_averages[warmest_continent]

print("\nAverage temperatures by continent:")
for continent, avg_temp in continent_averages.items():
    print(f"{continent}: {avg_temp}°C")

print(f"\nWarmest continent: {warmest_continent} with average temperature {warmest_temp}°C")