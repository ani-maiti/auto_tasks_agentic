import requests
import json

# Step 1: Retrieve current weather data for fifty cities
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "Fort Worth", "Cleveland", "San Francisco",
    "Charlotte", "Indianapolis", "Tampa", "San Antonio", "Seattle",
    "Denver", "Washington", "Boston", "Atlanta", "Detroit",
    "Nashville", "El Paso", "Memphis", "Baltimore", "Porland",
    "Louisville", "Sacramento", "Mesa", "Raleigh", "Orlando",
    "Macon", "Minneapolis", "Saint Paul", "Arlington", "Tucson"
]

weather_data = []
for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data.append({
            "city": city,
            "temperature": data["main"]["temp"]
        })

print(weather_data)
```

Replace `YOUR_API_KEY` with your actual OpenWeatherMap API key. This script retrieves the current temperature for each city and stores it in a list of dictionaries.