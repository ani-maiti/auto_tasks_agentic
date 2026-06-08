import json
import requests

# Extracting the current weather data for Sydney from the response
url = "https://wttr.in/Sydney?format=j1"
response = requests.get(url)
data = response.json()

# Get current weather conditions
current_weather = data['current_condition'][0]

print("Current weather in Sydney:")
print(f"Temperature: {current_weather['temp_C']}°C")
print(f"Feels like: {current_weather['FeelsLikeC']}°C")
print(f"Weather: {current_weather['weatherDesc'][0]['value']}")
print(f"Humidity: {current_weather['humidity']}%")
print(f"Wind Speed: {current_weather['windspeedKmph']} km/h")
print(f"Pressure: {current_weather['pressure']} hPa")