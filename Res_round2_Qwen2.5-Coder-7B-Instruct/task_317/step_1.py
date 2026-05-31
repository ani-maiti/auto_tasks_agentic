import requests
from bs4 import BeautifulSoup
import json

# Define the URL of the website to crawl
url = 'https://example.com'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the title of the page
    title = soup.title.string
    
    # Print the title to verify it was extracted correctly
    print(f'Title: {title}')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
```

This code will send a GET request to the specified URL and parse the HTML content to extract the page title. It then prints the title to verify that it was extracted correctly. If the request fails, it will print an error message with the status code.