import re
import json
from collections import defaultdict, Counter
from urllib.parse import urlparse

# Find all markdown files
markdown_files = [
    './schema_history.sqlite.md',
    './correlation_report.md',
    './schema_places.sqlite.md',
    './schema_accounts.db.md',
    './csv_primary_key_report.md',
    './schema_database.db.md',
    './schema_formhistory.sqlite.md'
]

# Extract outbound URLs from all markdown files
all_urls = []
for file_path in markdown_files:
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            # Match markdown links [text](url) and plain URLs
            urls = re.findall(r'\[.*?\]\((https?://[^\s)]+)\)', content)
            urls.extend(re.findall(r'(https?://[^\s<>"{}|\\^`\[\]]+)', content))
            all_urls.extend(urls)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Group URLs by domain
domain_counts = defaultdict(int)
domains = set()

for url in all_urls:
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain:
            domains.add(domain)
            domain_counts[domain] += 1
    except Exception as e:
        print(f"Error parsing URL {url}: {e}")

# Get the most referenced domains
most_referenced_domains = Counter(domain_counts).most_common(5)

# Save analysis to JSON
analysis = {
    "total_urls": len(all_urls),
    "unique_domains": len(domains),
    "domain_counts": dict(domain_counts),
    "most_referenced_domains": most_referenced_domains
}

with open('url_analysis.json', 'w') as f:
    json.dump(analysis, f, indent=2)

print("Analysis saved to url_analysis.json")
print("Most referenced domains:")
for domain, count in most_referenced_domains:
    print(f"{domain}: {count}")