import requests

# List of major cities worldwide
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    # Add more cities as needed
]

# Function to fetch weather data for a city
def fetch_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Fetch weather data for all cities
weather_data = {}
for city in cities:
    data = fetch_weather(city)
    if data:
        weather_data[city] = data

print(weather_data)
```

This code snippet fetches weather data for a list of major cities using the OpenWeatherMap API. You need to replace `"YOUR_API_KEY"` with your actual API key. The fetched data is stored in a dictionary where the keys are city names and the values are the corresponding weather data.