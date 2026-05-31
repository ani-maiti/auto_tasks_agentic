import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Crawl the public government open data portal
url = "https://example.gov/opendata"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
else:
    print("Failed to retrieve the webpage.")
    exit(1)