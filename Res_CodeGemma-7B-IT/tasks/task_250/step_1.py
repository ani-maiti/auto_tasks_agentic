from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set the number of stories to retrieve
num_stories = 100

# Create an empty list to store the stories
stories = []

# Iterate over the top stories
for i in range(1, num_stories + 1):
    # Get the story URL
    story_url = f"https://news.ycombinator.com/item?id={i}"

    # Retrieve the story HTML
    response = requests.get(story_url)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the domain from the story URL
    domain = soup.find("a", class_="hnuser").text.split(".")[-2]

    # Add the story to the list
    stories.append({
        "domain": domain,
    })

# Create a DataFrame from the stories
df = pd.DataFrame(stories)

# Group the stories by domain and count the number of stories per domain
df = df.groupby("domain").size().reset_index(name="count")

# Sort the domains by frequency in descending order
df = df.sort_values(by="count", ascending=False)

# Print the top 20 domains
print(df.head(20))

# Save the analysis to CSV
df.to_csv("hacker_news_domains.csv", index=False)