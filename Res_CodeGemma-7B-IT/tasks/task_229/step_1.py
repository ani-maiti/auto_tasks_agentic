import requests
from bs4 import BeautifulSoup
import pandas as pd

# Retrieve Hacker News front page
response = requests.get('https://news.ycombinator.com/')

# Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract company mentions
companies = []
for story in soup.find_all('a', class_='hnuser'):
    for company in story.text.split():
        if company.startswith('@'):
            companies.append(company[1:])

# Count company mentions
company_counts = pd.Series(companies).value_counts()

# Generate ranked report
report = company_counts.to_frame(name='count')
report['rank'] = report.index.rank(method='first', ascending=False)

# Save to CSV
report.to_csv('hacker_news_companies.csv', index=False)

print('Hacker News company report generated successfully.')