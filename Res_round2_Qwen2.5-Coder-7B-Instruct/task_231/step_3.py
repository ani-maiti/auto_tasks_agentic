import socket

# Set a timeout for DNS resolution
socket.setdefaulttimeout(10)

# Define the URL of the documentation website
url = 'https://docs.python.org/3/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <title> tags
    titles = soup.find_all('title')
    
    # Extract text from each title tag
    title_texts = [title.get_text() for title in titles]
    
    # Count the occurrences of each word in the titles
    word_counts = Counter(word for title in title_texts for word in title.split())
    
    # Get the top 20 most common words
    top_keywords = word_counts.most_common(20)
    
    # Print the top 20 keywords
    for keyword, count in top_keywords:
        print(f"{keyword}: {count}")
else:
    print("Failed to retrieve the webpage.")