import requests
from bs4 import BeautifulSoup
import json

# Step 1: Define the target URL
target_url = "https://docs.python.org/3/"

# Step 2: Fetch the webpage content
response = requests.get(target_url)

# Step 3: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Extract the title
title = soup.title.string

# Step 5: Print the extracted title
print(f"Extracted Title: {title}")