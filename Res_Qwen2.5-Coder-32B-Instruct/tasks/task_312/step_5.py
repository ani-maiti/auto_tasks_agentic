import requests

city_name = "New York"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=YOUR_API_KEY"
geolocation_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=YOUR_API_KEY"

weather_response = requests.get(weather_url)
geolocation_response = requests.get(geolocation_url)

print("Weather response status:", weather_response.status_code)
print("Geolocation response status:", geolocation_response.status_code)