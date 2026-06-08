import json
import requests
from bs4 import BeautifulSoup
import re

# Load the saved link graph
with open('link_graph.json', 'r') as f:
    link_graph = json.load(f)

# Find page with highest degree
max_degree = 0
most_connected_page = None

for page, links in link_graph.items():
    degree = len(links)
    if degree > max_degree:
        max_degree = degree
        most_connected_page = page

print(f"Page with highest degree: {most_connected_page}")
print(f"Highest degree: {max_degree}")

# Get the actual page title for better display
try:
    response = requests.get(most_connected_page, timeout=5)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1', {'class': 'firstHeading'})
    if title:
        print(f"Page title: {title.text}")
except:
    print("Could not retrieve page title")