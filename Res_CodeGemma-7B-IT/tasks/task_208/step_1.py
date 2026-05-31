# Import necessary libraries
import requests

# Define the API endpoint and city names
api_url = "https://api.openweathermap.org/data/2.5/weather"
cities = ["London", "New York City", "Tokyo", "Sydney", "Paris", "Berlin", "Rome", "Toronto", "Mexico City", "Cape Town"]

# Create an empty list to store responses
responses = []

# Loop through the cities and make API requests
for city in cities:
    params = {"q": city, "appid": "YOUR_API_KEY"}
    response = requests.get(api_url, params=params)
    responses.append(response.json())

# Print the raw responses
for response in responses:
    print(response)