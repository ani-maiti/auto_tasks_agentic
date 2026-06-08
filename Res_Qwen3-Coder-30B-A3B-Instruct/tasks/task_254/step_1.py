import requests
import json
from statistics import stdev

# List of 10 major cities
cities = [
    "New York", "London", "Tokyo", "Paris", "Sydney",
    "Dubai", "Moscow", "Toronto", "Singapore", "Seoul"
]

# OpenWeatherMap API key (using a free tier key)
api_key = "YOUR_API_KEY_HERE"

# Store weather data
weather_data = {}

# Fetch weather data for each city
for city in cities:
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # Extract temperature data for next 7 days
            temps = [entry['main']['temp'] for entry in data['list'][:8]]  # 8 entries = 2 days
            variability = stdev(temps) if len(temps) > 1 else 0
            
            weather_data[city] = {
                'temperatures': temps,
                'variability': variability
            }
        else:
            print(f"Error fetching data for {city}: {data}")
            
    except Exception as e:
        print(f"Exception for {city}: {str(e)}")

# Save data to JSON file
with open('weather_forecast_data.json', 'w') as f:
    json.dump(weather_data, f, indent=2)

# Find city with highest variability
if weather_data:
    max_var_city = max(weather_data, key=lambda x: weather_data[x]['variability'])
    print(f"City with highest forecast variability: {max_var_city}")
    print(f"Variability score: {weather_data[max_var_city]['variability']:.2f}")
else:
    print("No data available")