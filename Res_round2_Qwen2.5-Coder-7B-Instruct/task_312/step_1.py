import requests
import json

# Define the city for which we want to fetch data
city = "New York"

# Step 1: Fetch weather data from OpenWeatherMap API
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
weather_response = requests.get(weather_url)

if weather_response.status_code == 200:
    weather_data = weather_response.json()
else:
    weather_data = {}

# Step 2: Fetch timezone data from WorldTimeAPI
timezone_url = f"http://worldtimeapi.org/api/timezone/{weather_data['sys']['country']}/{weather_data['sys']['sunrise']}"
timezone_response = requests.get(timezone_url)

if timezone_response.status_code == 200:
    timezone_data = timezone_response.json()
else:
    timezone_data = {}

# Step 3: Fetch geolocation data from Google Maps Geocoding API
geolocation_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key=YOUR_API_KEY"
geolocation_response = requests.get(geolocation_url)

if geolocation_response.status_code == 200:
    geolocation_data = geolocation_response.json()
else:
    geolocation_data = {}

# Step 4: Merge all data into a unified record
unified_record = {
    "city": city,
    "weather": weather_data,
    "timezone": timezone_data,
    "geolocation": geolocation_data
}

# Step 5: Save the dataset to JSON
with open("city_data.json", "w") as json_file:
    json.dump(unified_record, json_file, indent=4)

print("Data saved to city_data.json")
```

Replace `YOUR_API_KEY` with actual API keys for OpenWeatherMap and Google Maps Geocoding. This script fetches weather, timezone, and geolocation data for a specified city, merges it into a unified record, saves it to a JSON file, and prints a confirmation message.