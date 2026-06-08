import requests
import json
import random
from sklearn.cluster import KMeans
import numpy as np

# First, let's get a list of 100 cities
# Using a predefined list of major cities
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", 
    "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville",
    "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis", 
    "Seattle", "Denver", "Washington", "Boston", "El Paso", "Nashville", 
    "Detroit", "Oklahoma City", "Portland", "Las Vegas", "Memphis", 
    "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson", 
    "Fresno", "Sacramento", "Mesa", "Kansas City", "Atlanta", "Colorado Springs",
    "Omaha", "Raleigh", "Miami", "Long Beach", "Virginia Beach", "Oakland",
    "Minneapolis", "Tulsa", "Wichita", "Arlington", "New Orleans", "Bakersfield",
    "Tampa", "Honolulu", "Anaheim", "Santa Ana", "St. Louis", "Riverside",
    "Corpus Christi", "Lexington", "Stockton", "Henderson", "Saint Paul",
    "Cincinnati", "Pittsburgh", "Greensboro", "Anchorage", "Plano", "Lincoln",
    "Orlando", "Irvine", "Newark", "Chandler", "Laredo", "Buffalo", "Durham",
    "Madison", "Lubbock", "Garland", "Glendale", "Hialeah", "Reno", "Scottsdale",
    "Irving", "North Las Vegas", "Fremont", "Gilbert", "Boise", "Richmond",
    "Baton Rouge", "Spokane", "Des Moines", "Modesto", "Shreveport", "Tacoma",
    "Oxnard", "Fontana", "Columbus", "Akron", "Montgomery", "Moreno Valley"
]

print(f"Retrieving weather data for {len(cities)} cities...")