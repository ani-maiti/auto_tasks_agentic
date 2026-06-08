import requests

# Using OpenWeatherMap API to get weather data for New York
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    'q': 'New York',
    'appid': 'YOUR_API_KEY',  # This would normally be your API key
    'units': 'metric'
}

try:
    response = requests.get(url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        temperature = data['main']['temp']
        print(f"Current temperature in New York: {temperature}°C")
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")
        
except Exception as e:
    print(f"Failed to fetch weather data: {e}")