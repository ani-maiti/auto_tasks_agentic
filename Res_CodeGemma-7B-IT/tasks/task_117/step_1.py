import requests

# Get the current weather for Berlin using the OpenWeatherMap API
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Berlin&appid=YOUR_API_KEY")

# Print the weather information
print(response.json())