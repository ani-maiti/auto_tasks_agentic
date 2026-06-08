import requests

# Using OpenWeatherMap API to get weather data for Tokyo
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    'q': 'Tokyo',
    'appid': 'b6907d289e10d714a6e88b30761fae22',  # Using a sample API key for demonstration
    'units': 'metric'
}

try:
    response = requests.get(url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        temperature = data['main']['temp']
        print(f"Current temperature in Tokyo: {temperature}°C")
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")
        
except Exception as e:
    print(f"Failed to fetch weather data: {e}")