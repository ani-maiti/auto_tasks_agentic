import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Define the URL of the documentation site to crawl
url = 'https://docs.python.org/3/'

# Step 2: Send an HTTP GET request to the URL
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 5: Find all the pages within the documentation site
    pages = [a['href'] for a in soup.find_all('a', href=True)]
    
    # Step 6: Limit the number of pages to crawl to 200
    pages = pages[:200]
    
    # Step 7: Initialize a list to store the extracted code examples
    code_examples = []
    
    # Step 8: Loop through each page and extract code examples
    for page in pages:
        page_url = url + page
        page_response = requests.get(page_url)
        if page_response.status_code == 200:
            page_soup = BeautifulSoup(page_response.text, 'html.parser')
            code_snippets = page_soup.find_all('code')
            for snippet in code_snippets:
                code_examples.append((page_url, snippet.text.strip()))
else:
    print(f"Failed to retrieve the documentation site. Status code: {response.status_code}")