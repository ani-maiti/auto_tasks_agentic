# Import necessary libraries
import requests
import json

# Define a list of major cities
cities = ["London", "Paris", "Tokyo", "New York", "Sydney", "Toronto", "Berlin", "Rome", "Seoul", "Mexico City"]

# Function to retrieve weather forecast for a given city
def get_weather_forecast(city):
    api_key = "YOUR_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/forecast"

    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    return response.json()

# Function to calculate forecast variability for a given city
def calculate_forecast_variability(forecast):
    temperatures = [day["main"]["temp"] for day in forecast["list"][:7]]
    return max(temperatures) - min(temperatures)

# Create a dictionary to store city and variability data
city_variabilities = {}

# Iterate over cities and retrieve weather data
for city in cities:
    forecast = get_weather_forecast(city)
    variability = calculate_forecast_variability(forecast)
    city_variabilities[city] = variability

# Find the city with the highest variability
most_variable_city = max(city_variabilities, key=city_variabilities.get)

# Print the city with the highest variability
print(f"City with the highest variability: {most_variable_city}")

# Save the data to a JSON file
with open("weather_variabilities.json", "w") as f:
    json.dump(city_variabilities, f)