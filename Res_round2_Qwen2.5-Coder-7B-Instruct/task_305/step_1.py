import requests
from datetime import datetime

# Define the list of cities
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

# Define the API endpoint
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"

# Define the API key (replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key)
api_key = "YOUR_API_KEY"

# Function to get weather data for a given city
def get_weather_data(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(api_endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {city}")
        return None

# Fetch weather data for all cities
weather_data = {}
for city in cities:
    data = get_weather_data(city)
    if data:
        weather_data[city] = data["main"]["temp"]

# Save the dataset to CSV
with open("weather_data.csv", "w") as file:
    file.write("City,Temperature\n")
    for city, temp in weather_data.items():
        file.write(f"{city},{temp}\n")

print("Weather data saved to weather_data.csv")