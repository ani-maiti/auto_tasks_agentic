import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Weather in London: {weather}")
    print(f"Temperature: {temperature} Kelvin")
else:
    print("Failed to retrieve weather data")
```

Replace `YOUR_API_KEY` with an actual OpenWeatherMap API key. This script sends a GET request to the OpenWeatherMap API to fetch the current weather for London and prints the weather description and temperature. If the request fails, it prints an error message.