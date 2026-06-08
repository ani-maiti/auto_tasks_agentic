import requests
import csv
from datetime import datetime
import json

# First, let's check if we can access a known government open data portal
# Using data.gov as an example
url = "https://api.data.gov/developer/resources"
try:
    response = requests.get(url, timeout=10)
    print(f"Successfully accessed data.gov API. Status code: {response.status_code}")
except Exception as e:
    print(f"Failed to access data.gov API: {e}")

# Let's try a simpler approach - check if we can get dataset info from data.gov
# We'll use the CKAN API which data.gov uses
ckan_url = "https://data.gov/api/action/package_search"
params = {"q": "climate", "rows": 5}
try:
    response = requests.get(ckan_url, params=params, timeout=10)
    if response.status_code == 200:
        data = response.json()
        print("Successfully fetched sample data from data.gov")
        print(f"Found {len(data['result']['results'])} datasets")
        # Save first dataset as example
        if data['result']['results']:
            sample_dataset = data['result']['results'][0]
            print("Sample dataset keys:", list(sample_dataset.keys()))
    else:
        print(f"API call failed with status code: {response.status_code}")
except Exception as e:
    print(f"Error accessing data.gov: {e}")