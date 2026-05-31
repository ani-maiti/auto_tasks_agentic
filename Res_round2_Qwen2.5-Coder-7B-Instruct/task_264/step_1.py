import requests
from bs4 import BeautifulSoup
import json

# Step 1: Define the URL of the documentation site to crawl
url = "https://example.com/docs"  # Replace with the actual documentation site URL

# Step 2: Send an HTTP GET request to the URL
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 5: Find all internal links on the page
    internal_links = [a['href'] for a in soup.find_all('a', href=True) if url in a['href']]
    
    # Step 6: Print the collected internal links
    print("Collected internal links:", internal_links)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
```

This code will send an HTTP GET request to the specified documentation site, parse the HTML content, find all internal links, and print them. If the request fails, it will print an error message with the status code.