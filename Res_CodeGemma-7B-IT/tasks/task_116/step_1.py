import requests

api_key = "YOUR_API_KEY"
city_name = "Sydney"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    print(f"Current weather in {city_name}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Weather description: {weather_data['weather'][0]['description']}")
else:
    print(f"Error retrieving weather data: {response.status_code}")