import requests
from bs4 import BeautifulSoup
import json

# Step 1: Define the URL of the documentation website to crawl
url = "https://docs.python.org/3/"

# Step 2: Send a GET request to the website
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 5: Extract the title of the page
    title = soup.title.string
    
    # Step 6: Print the extracted title
    print(f"Title: {title}")
else:
    print("Failed to retrieve the webpage.")
```

This code snippet sends a GET request to the Python documentation website and prints the title of the page. This helps us verify that we can successfully fetch the website and proceed with further steps.