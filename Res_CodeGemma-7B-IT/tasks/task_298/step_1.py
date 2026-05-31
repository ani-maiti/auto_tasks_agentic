# Import necessary libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define function to scrape weather data for a city
def get_weather_data(city):
    url = f"https://www.weather.gov/climate/monthly-averages?city={city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # ... (Scrape data from the webpage)
    return weather_data

# Get weather data for largest cities in each US state
cities = {
    "Alabama": "Birmingham",
    "Alaska": "Anchorage",
    # ... (Map of US states and their largest cities)
}
weather_data_list = []
for state, city in cities.items():
    weather_data = get_weather_data(city)
    weather_data["state"] = state
    weather_data_list.append(weather_data)

# Concatenate data for all states
weather_df = pd.concat(weather_data_list)

# Normalize temperature data
weather_df["mean_temp"] = (weather_df["mean_temp"] - 32) * (5/9)

# Compute regional averages
regional_averages = weather_df.groupby("region")["mean_temp"].mean()

# Save dataset to CSV
weather_df.to_csv("weather_data.csv", index=False)

# Generate report
print("Regional Weather Data Report")
print(regional_averages)

# Print warmest region
warmest_region = regional_averages.idxmax()
print(f"Warmest region: {warmest_region}")