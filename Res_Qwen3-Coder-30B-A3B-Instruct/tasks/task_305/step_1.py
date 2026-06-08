import requests
import pandas as pd
from datetime import datetime, timedelta
import time

# List of 10 cities
cities = [
    "New York", "London", "Tokyo", "Sydney", "Paris",
    "Berlin", "Moscow", "Dubai", "Toronto", "Singapore"
]

# Using OpenWeatherMap API (free tier)
API_KEY = "YOUR_API_KEY"  # This would normally be set as an environment variable
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

weather_data = []

for city in cities:
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data.append({
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description']
            })
        else:
            print(f"Error fetching data for {city}: {response.status_code}")
    except Exception as e:
        print(f"Exception for {city}: {str(e)}")
    
    # Be respectful to API rate limits
    time.sleep(1)

# Convert to DataFrame
df = pd.DataFrame(weather_data)
print(df.head())