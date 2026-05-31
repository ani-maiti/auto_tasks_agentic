import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import csv

# Step 1: Retrieve the latest one hundred Hacker News stories
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = []
for item in soup.find_all('tr', class_='athing'):
    link = item.find('a', class_='storylink')
    if link:
        stories.append(link['href'])

# Step 2: Extract all external domains
domains = []
for story in stories[:100]:  # Limit to the first 100 stories
    if re.match(r'https?://', story):
        domain = re.sub(r'https?://(www\.)?', '', story.split('/')[0])
        domains.append(domain)

# Step 3: Rank domains by frequency
domain_counts = Counter(domains)

# Step 4: Save the analysis to CSV
with open('hn_domains.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Domain', 'Frequency'])
    for domain, count in domain_counts.most_common():
        writer.writerow([domain, count])

# Step 5: Print the top twenty domains
print("Top twenty domains:")
for domain, count in domain_counts.most_common(20):
    print(f"{domain}: {count}")
```

This script retrieves the latest one hundred Hacker News stories, extracts all external domains, ranks them by frequency, saves the analysis to a CSV file, and prints the top twenty domains.