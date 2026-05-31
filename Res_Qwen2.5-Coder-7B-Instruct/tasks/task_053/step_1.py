import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid=YOUR_API_KEY&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    print(f"The current temperature in Tokyo is {temperature}°C")
else:
    print("Failed to retrieve weather data")
```

Replace `YOUR_API_KEY` with your actual OpenWeatherMap API key. This script sends a request to the OpenWeatherMap API to get the current weather for Tokyo and prints the temperature in Celsius. If the request fails, it prints an error message.