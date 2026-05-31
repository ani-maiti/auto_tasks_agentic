import requests
from bs4 import BeautifulSoup
import csv

# Retrieve Hacker News top stories
response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.content, "html.parser")

# Extract story titles and links
stories = []
for story in soup.find_all("a", class_="storylink"):
    title = story.text
    link = story.get("href")
    stories.append((title, link))

# Filter stories mentioning programming languages
programming_stories = []
for title, link in stories:
    if "programming" in title.lower():
        programming_stories.append((title, link))

# Generate language frequencies
language_frequencies = {}
for title, _ in programming_stories:
    for language in ["python", "javascript", "java", "c++", "c#", "php", "ruby", "swift", "go", "rust"]:
        if language in title.lower():
            language_frequencies[language] = language_frequencies.get(language, 0) + 1

# Save results to CSV
with open("hacker_news_languages.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Language", "Frequency"])
    for language, frequency in language_frequencies.items():
        writer.writerow([language, frequency])