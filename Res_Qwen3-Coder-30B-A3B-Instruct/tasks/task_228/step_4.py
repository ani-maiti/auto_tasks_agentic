import json
from collections import defaultdict

# Create mock weather data for 20 major cities
mock_weather_data = [
    {"name": "New York", "main": {"temp": 18.0}, "continent": "North America"},
    {"name": "London", "main": {"temp": 12.0}, "continent": "Europe"},
    {"name": "Tokyo", "main": {"temp": 22.0}, "continent": "Asia"},
    {"name": "Sydney", "main": {"temp": 19.0}, "continent": "Australia"},
    {"name": "Paris", "main": {"temp": 16.0}, "continent": "Europe"},
    {"name": "Berlin", "main": {"temp": 14.0}, "continent": "Europe"},
    {"name": "Moscow", "main": {"temp": 8.0}, "continent": "Europe"},
    {"name": "Dubai", "main": {"temp": 35.0}, "continent": "Asia"},
    {"name": "Singapore", "main": {"temp": 28.0}, "continent": "Asia"},
    {"name": "Toronto", "main": {"temp": 15.0}, "continent": "North America"},
    {"name": "Mexico City", "main": {"temp": 20.0}, "continent": "North America"},
    {"name": "São Paulo", "main": {"temp": 22.0}, "continent": "South America"},
    {"name": "Cairo", "main": {"temp": 26.0}, "continent": "Africa"},
    {"name": "Johannesburg", "main": {"temp": 17.0}, "continent": "Africa"},
    {"name": "Seoul", "main": {"temp": 21.0}, "continent": "Asia"},
    {"name": "Bangkok", "main": {"temp": 30.0}, "continent": "Asia"},
    {"name": "Istanbul", "main": {"temp": 18.0}, "continent": "Europe"},
    {"name": "Rome", "main": {"temp": 20.0}, "continent": "Europe"},
    {"name": "Madrid", "main": {"temp": 23.0}, "continent": "Europe"},
    {"name": "Athens", "main": {"temp": 24.0}, "continent": "Europe"}
]

# Save mock data to JSON file
with open('weather_data.json', 'w') as f:
    json.dump(mock_weather_data, f, indent=2)

print("Created mock weather data for 20 cities saved to weather_data.json")

# Calculate average temperature by continent
continent_temps = defaultdict(list)
for data in mock_weather_data:
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