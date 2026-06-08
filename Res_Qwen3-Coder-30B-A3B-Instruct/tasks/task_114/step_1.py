import requests

# Using OpenWeatherMap API to get weather data for London
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    'q': 'London',
    'appid': 'YOUR_API_KEY',  # This would normally be stored securely
    'units': 'metric'
}

try:
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
except Exception as e:
    print(f"Error: {e}")