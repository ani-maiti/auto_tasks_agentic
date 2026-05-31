import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Define the URL of the news website to crawl
url = "https://news.example.com"

# Step 2: Send an HTTP GET request to the website
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 5: Find all article title elements (assuming <h2> tags for simplicity)
    article_titles = soup.find_all('h2')
    
    # Step 6: Collect up to one hundred article titles
    collected_titles = [title.text.strip() for title in article_titles[:100]]
    
    # Step 7: Save the collected titles to a CSV file
    with open('article_titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title'])
        for title in collected_titles:
            writer.writerow([title])
    
    print("Article titles saved to article_titles.csv")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
```

This code will send an HTTP GET request to the specified news website, parse the HTML content, extract up to one hundred article titles, and save them to a CSV file named `article_titles.csv`. If the request fails, it will print an error message with the status code.