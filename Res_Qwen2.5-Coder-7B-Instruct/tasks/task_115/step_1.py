import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=YOUR_API_KEY"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Weather in Paris: {weather}, Temperature: {temperature}K")
else:
    print("Failed to retrieve weather data.")
```

Replace `YOUR_API_KEY` with an actual OpenWeatherMap API key. This script sends a GET request to the OpenWeatherMap API to fetch the current weather for Paris and prints it out. If the request fails, it prints an error message.