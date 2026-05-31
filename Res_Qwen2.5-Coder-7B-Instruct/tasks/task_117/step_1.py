import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=Berlin&appid=YOUR_API_KEY"
response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)
else:
    print(f"Failed to retrieve weather data. Status code: {response.status_code}")
```

Replace `YOUR_API_KEY` with an actual OpenWeatherMap API key. This script sends a GET request to the OpenWeatherMap API to fetch the current weather for Berlin and prints the JSON response. If the request fails, it prints an error message with the status code.