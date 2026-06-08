import json

# Load all the saved JSON files and extract temperature data
cities_temperatures = {}

for city in ["New York", "London", "Tokyo", "Paris", "Sydney", 
             "Dubai", "Moscow", "Rio de Janeiro", "Cairo", "Mumbai"]:
    with open(f"{city}_weather.json", "r") as f:
        data = json.load(f)
        temp = data['main']['temp']
        cities_temperatures[city] = temp
        print(f"{city}: {temp}°C")

# Find warmest and coldest cities
warmest_city = max(cities_temperatures, key=cities_temperatures.get)
coldest_city = min(cities_temperatures, key=cities_temperatures.get)

print(f"\nWarmest city: {warmest_city} ({cities_temperatures[warmest_city]}°C)")
print(f"Coldest city: {coldest_city} ({cities_temperatures[coldest_city]}°C)")