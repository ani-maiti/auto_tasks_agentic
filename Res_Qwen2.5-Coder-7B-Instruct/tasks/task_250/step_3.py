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
        href = link['href']
        if not href.startswith('item?id='):
            stories.append(href)

# Limit to the latest 100 stories
stories = stories[:100]

print(f"Retrieved {len(stories)} stories.")

# Step 2: Extract all external domains
domains = [re.sub(r'https?://([^/?]+).*', r'\1', story) for story in stories]
print(f"Extracted {len(domains)} domains.")

# Step 3: Rank domains by frequency
domain_counts = Counter(domains)
top_domains = domain_counts.most_common(20)

print("Top 20 domains:")
for domain, count in top_domains:
    print(f"{domain}: {count}")

# Step 4: Save the analysis to CSV
with open('hn_domain_analysis.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Domain', 'Count'])
    writer.writerows(top_domains)

print("Analysis saved to hn_domain_analysis.csv")

# Step 5: Print the top twenty domains
print("Top 20 domains:")
for domain, count in top_domains:
    print(f"{domain}: {count}")