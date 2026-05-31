# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from collections import Counter

# Define the website URL
url = "https://news.ycombinator.com/"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all article titles
article_titles = []
for title in soup.find_all("a", class_="storylink"):
    article_titles.append(title.text)

# Extract keywords from article titles
keywords = []
for title in article_titles:
    # Split the title into words and extract keywords
    words = title.lower().split()
    keywords.extend(words)

# Generate frequency statistics for keywords
keyword_counts = Counter(keywords)

# Save the results to a CSV file
with open("news_keywords.csv", "w") as f:
    for keyword, count in keyword_counts.items():
        f.write(f"{keyword},{count}\n")