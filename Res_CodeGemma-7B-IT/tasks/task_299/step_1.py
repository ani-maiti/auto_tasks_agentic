import os
import re
import json
from collections import defaultdict

# Get all Markdown files in the current directory
markdown_files = [f for f in os.listdir('.') if f.endswith('.md')]

# Extract outbound URLs from each Markdown file
urls = []
for file in markdown_files:
    with open(file, 'r') as f:
        for line in f:
            urls.extend(re.findall(r'\[.+?\]\((.+?)\)', line))

# Group URLs by domain
domain_urls = defaultdict(list)
for url in urls:
    domain = url.split('/')[2]
    domain_urls[domain].append(url)

# Retrieve page titles for the most referenced domains
page_titles = {}
for domain, url_list in domain_urls.items():
    # TODO: Implement a function to retrieve page titles for a given domain
    page_titles[domain] = get_page_title(domain)

# Save the analysis to JSON
analysis = {
    'urls': urls,
    'domain_urls': domain_urls,
    'page_titles': page_titles
}
with open('analysis.json', 'w') as f:
    json.dump(analysis, f)

# Generate a report
report = f"""
## Markdown Analysis Report

**Total URLs:** {len(urls)}

**Most Referenced Domains:**

| Domain | URL Count | Page Title |
|---|---|---|
| {max(domain_urls, key=len)} | {len(domain_urls[max(domain_urls, key=len)])} | {page_titles[max(domain_urls, key=len)]} |

**Note:** This report is based on the analysis of the Markdown files in the current directory. The page titles are retrieved from the domain's website, which may not always be accurate.
"""
print(report)