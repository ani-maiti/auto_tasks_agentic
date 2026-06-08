import requests
import csv
from collections import Counter
import re

# Get the top 100 story IDs
response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
story_ids = response.json()[:100]

# Fetch the stories
stories = []
for story_id in story_ids:
    story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
    story = story_response.json()
    if story and 'title' in story:
        stories.append(story['title'])

# Define comprehensive company names to look for
companies = [
    "Apple", "Microsoft", "Google", "Amazon", "Facebook", "Tesla", 
    "Netflix", "Twitter", "Uber", "Airbnb", "Spotify", "Slack",
    "Adobe", "Salesforce", "Oracle", "IBM", "Intel", "AMD",
    "NVIDIA", "Samsung", "Sony", "LG", "Cisco", "HP",
    "Dell", "Lenovo", "Qualcomm", "T-Mobile", "Verizon", "AT&T",
    "Meta", "Snapchat", "Pinterest", "LinkedIn", "GitHub", "Dropbox",
    "Shopify", "Square", "PayPal", "Stripe", "Zoom", "VMware",
    "Twitter", "Reddit", "Tumblr", "Quora", "Medium", "Wikipedia",
    "Mozilla", "Canonical", "Red Hat", "SUSE", "Debian", "Ubuntu"
]

# Count mentions
company_counts = Counter()
for story in stories:
    title = story.lower()
    for company in companies:
        # Use word boundaries to match whole words only
        pattern = r'\b' + re.escape(company.lower()) + r'\b'
        matches = re.findall(pattern, title)
        if matches:
            company_counts[company] += len(matches)

# Get top 10 companies
top_companies = company_counts.most_common(10)

# Save to CSV
with open('company_mentions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company', 'Mentions'])
    writer.writerows(top_companies)

print("Top 10 companies mentioned:")
for company, count in top_companies:
    print(f"{company}: {count}")

# Show all companies and their counts for verification
print("\nAll company counts:")
for company, count in company_counts.most_common():
    if count > 0:
        print(f"{company}: {count}")