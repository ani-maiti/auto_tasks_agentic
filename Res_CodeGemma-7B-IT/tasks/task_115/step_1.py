import requests

api_key = "YOUR_API_KEY"
city = "Paris"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    print(f"Current weather in Paris: {temperature}°C, {description}")
else:
    print("Error retrieving weather data.")