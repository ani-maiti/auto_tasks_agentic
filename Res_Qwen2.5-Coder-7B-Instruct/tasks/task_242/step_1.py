import requests
from bs4 import BeautifulSoup
import csv
from collections import Counter

# Step 1: Retrieve metadata for the top fifty most starred Python repositories on GitHub
url = "https://github.com/search?q=language:python+stars:>1000&sort=stars&order=desc"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

repositories = []
for item in soup.find_all('li', class_='repo-list-item'):
    repo_name = item.find('a', class_='v-align-middle').text.strip()
    stars = int(item.find('span', class_='Counter').text.strip().replace(',', ''))
    repositories.append((repo_name, stars))

top_50_repositories = sorted(repositories, key=lambda x: x[1], reverse=True)[:50]

# Save repository names to a CSV file
with open('top_50_python_repos.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Repository Name'])
    for repo in top_50_repositories:
        writer.writerow([repo[0]])

print("Top 50 Python repositories retrieved and saved to top_50_python_repos.csv")