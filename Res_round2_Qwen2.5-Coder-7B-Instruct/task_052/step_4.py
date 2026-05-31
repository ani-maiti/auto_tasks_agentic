import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=New%20York&appid=YOUR_API_KEY"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    print(f"Current temperature in New York: {temperature} Kelvin")
else:
    print("Failed to retrieve weather data")
```

Replace `YOUR_API_KEY` with an actual OpenWeatherMap API key.