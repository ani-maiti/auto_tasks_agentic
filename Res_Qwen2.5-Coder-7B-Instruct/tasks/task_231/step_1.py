import requests
from bs4 import BeautifulSoup
from collections import Counter

# Define the URL of the documentation website
url = "https://docs.example.com"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the <title> tags
    titles = soup.find_all('title')
    
    # Extract the text from each title tag
    title_texts = [title.get_text() for title in titles]
    
    # Count the occurrences of each word in the title texts
    word_counts = Counter(word.lower() for title in title_texts for word in title.split())
    
    # Get the top 20 most common words
    top_keywords = word_counts.most_common(20)
    
    # Print the top 20 keywords
    print(top_keywords)
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")