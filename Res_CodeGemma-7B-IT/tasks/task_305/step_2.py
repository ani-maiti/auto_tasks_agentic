# Import necessary libraries
import requests
import pandas as pd

# Define the list of cities
cities = ["New York", "London", "Paris", "Tokyo", "Sydney", "Toronto", "Mexico City", "Cairo", "Mumbai", "Delhi"]

# Create an empty list to store the weather data
weather_data = []

# Loop through the list of cities
for city in cities:
    # Construct the API endpoint URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Extract the temperature data from the response
    temperature = response.json()["main"]["temp"]

    # Append the temperature data to the list
    weather_data.append({"city": city, "temperature": temperature})

# Create a DataFrame from the weather data
df = pd.DataFrame(weather_data)

# Calculate the temperature range for each city
df["temperature_range"] = df["temperature"].max() - df["temperature"].min()

# Find the city with the largest temperature range
city_with_largest_range = df["city"][df["temperature_range"].idxmax()]

# Save the DataFrame to a CSV file
df.to_csv("weather_data.csv", index=False)

# Generate a report with the city with the largest temperature range
print(f"The city with the largest temperature range is: {city_with_largest_range}")