import requests

# Using OpenWeatherMap API to get weather data for Sydney
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    'q': 'Sydney',
    'appid': 'YOUR_API_KEY',  # This would normally be a real API key
    'units': 'metric'
}

try:
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
except Exception as e:
    print(f"Error: {e}")