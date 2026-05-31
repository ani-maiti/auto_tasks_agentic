import requests
from datetime import datetime

# Define the list of cities
cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Jose"
]

# Define the API endpoint
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"

# Define the API key (replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key)
api_key = "YOUR_API_KEY"

# Define the parameters for the API request
params = {
    "appid": api_key,
    "units": "metric"  # Use 'imperial' for Fahrenheit
}

# Initialize an empty dictionary to store the weather data
weather_data = {}

# Loop through the list of cities and fetch the weather data
for city in cities:
    params["q"] = city
    response = requests.get(api_endpoint, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_data[city] = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"]
        }
    else:
        print(f"Failed to fetch weather data for {city}")

# Save the weather data to a CSV file
with open("weather_data.csv", "w") as f:
    f.write("City,Temperature,Humidity\n")
    for city, data in weather_data.items():
        f.write(f"{city},{data['temperature']},{data['humidity']}\n")

print("Weather data saved to weather_data.csv")
```

This code will fetch the current weather data for the specified list of cities using the OpenWeatherMap API and save it to a CSV file named `weather_data.csv`.