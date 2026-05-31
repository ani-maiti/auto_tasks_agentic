# Step 2: Check the error message and try again with a different API key or service
# For demonstration purposes, let's assume we have a backup API key
backup_api_key = "BACKUP_API_KEY"

weather_data = []
for city in cities:
    url = f"http://api.backupweatherapi.com/v1/current.json?key={backup_api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data.append(response.json())
    else:
        print(f"Failed to fetch weather data for {city}")

# Save weather data to a JSON file
with open("weather_data.json", "w") as f:
    json.dump(weather_data, f)

print("Weather data retrieved and saved.")