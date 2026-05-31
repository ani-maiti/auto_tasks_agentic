import requests

url = "http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=sydney"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to retrieve weather data")
```

Replace `YOUR_API_KEY` with an actual API key from a weather service like OpenWeatherMap or WeatherAPI. This script sends a GET request to the weather API and prints the JSON response if successful. If the request fails, it prints an error message.