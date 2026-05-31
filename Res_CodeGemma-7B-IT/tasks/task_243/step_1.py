# Import necessary libraries
import requests
import json

# Define the API endpoint and headers
url = "https://api.openweathermap.org/data/2.5/weather"
headers = {"Accept": "application/json"}

# Define the list of European capital cities
cities = [
    "London",
    "Paris",
    "Berlin",
    "Madrid",
    "Rome",
    "Vienna",
    "Prague",
    "Copenhagen",
    "Dublin",
    "Helsinki",
    "Athens",
    "Budapest",
    "Dublin",
    "Lisbon",
    "Oslo",
    "Warsaw",
    "Lisbon",
    "Prague",
    "Rome",
    "Sofia",
    "Stockholm",
    "Bratislava",
    "Ljubljana",
    "Vaduz",
    "Chisinau",
    "Nicosia",
    "San Marino",
    "Valletta",
    "Andorra la Vella",
]

# Initialize variables for average temperature and city count
total_temp = 0
city_count = 0

# Loop through each city
for city in cities:
    # Construct the API request parameters
    params = {"q": city, "appid": "YOUR_API_KEY", "units": "metric"}

    # Send the API request and store the response
    response = requests.get(url, headers=headers, params=params)

    # Check for successful response
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)

        # Extract the current temperature
        temp = data["main"]["temp"]

        # Update average temperature and city count
        total_temp += temp
        city_count += 1

        # Print the city and temperature
        print(f"{city}: {temp:.2f}°C")

# Calculate and print the average temperature
average_temp = total_temp / city_count
print(f"\nAverage temperature in European capital cities: {average_temp:.2f}°C")