import requests

# Using OpenWeatherMap API to get weather data for London
# Note: We need a valid API key for this to work properly
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    'q': 'London',
    'appid': 'b6907d289e10d714a6e88b30761fae22',  # Using a sample API key for demonstration
    'units': 'metric'
}

try:
    response = requests.get(url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        print("Current weather in London:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print(f"Error: {data['message']}")
        
except Exception as e:
    print(f"Error occurred: {e}")