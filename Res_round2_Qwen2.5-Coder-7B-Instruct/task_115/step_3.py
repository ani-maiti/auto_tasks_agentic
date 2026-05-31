import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=YOUR_API_KEY"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"Current temperature in Paris: {temperature}K")
    print(f"Weather description: {description}")
else:
    print("Failed to retrieve weather data")
```

Replace `YOUR_API_KEY` with an actual OpenWeatherMap API key.