# Step 2: Define the list of cities and retrieve weather forecasts
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
    # Add more cities as needed
]

weather_data = []
for city in cities:
    url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data.append(response.json())
    else:
        print(f"Failed to fetch weather data for {city}")

# Save weather data to a JSON file
with open("weather_data.json", "w") as f:
    json.dump(weather_data, f)

print("Weather data retrieved and saved.")