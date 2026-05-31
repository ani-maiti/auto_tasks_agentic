import requests
import json

# Define the list of cities
cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    # Add more city names here up to 50
]

# Function to get weather data for a city
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Retrieve weather data for all cities
weather_data = {}
for city in cities:
    data = get_weather(city)
    if data:
        weather_data[city] = data['main']['temp']

# Save the weather data to a file
with open('weather_data.json', 'w') as f:
    json.dump(weather_data, f)

print("Weather data retrieved and saved.")