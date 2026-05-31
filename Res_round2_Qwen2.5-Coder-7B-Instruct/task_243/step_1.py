import requests

# List of European capital cities
capitals = [
    "Amsterdam", "Andorra la Vella", "Ankara", "Athens", "Baku",
    "Belgrade", "Berlin", "Brussels", "Bucharest", "Budapest",
    "Copenhagen", "Dublin", "Helsinki", "Istanbul", "Kiev",
    "Lisbon", "London", "Madrid", "Minsk", "Monaco",
    "Oslo", "Paris", "Prague", "Riga", "Rome",
    "San Marino", "Sofia", "Stockholm", "Tallinn", "Vienna",
    "Warsaw", "Zagreb"
]

# URL for the OpenWeatherMap API
api_url = "http://api.openweathermap.org/data/2.5/weather"

# Your API key here
api_key = "YOUR_API_KEY"

# Dictionary to store temperature data
temperatures = {}

for capital in capitals:
    params = {
        'q': capital,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' if you prefer Fahrenheit
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        temperatures[capital] = temperature
    else:
        print(f"Failed to get weather data for {capital}")

# Calculate average temperature
average_temperature = sum(temperatures.values()) / len(temperatures)

# Find the warmest capital
warmest_capital = max(temperatures, key=temperatures.get)

print(f"The warmest capital in Europe is {warmest_capital} with a temperature of {temperatures[warmest_capital]}°C")
```

Replace `"YOUR_API_KEY"` with your actual OpenWeatherMap API key. This script retrieves the current weather data for each capital city in Europe, calculates the average temperature, and prints the warmest capital.