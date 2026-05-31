import re
from collections import defaultdict

markdown_files = ['./consolidation_report.md', './command_frequency.md', './cross_reference_report.md']

urls = []

for file in markdown_files:
    with open(file, 'r') as f:
        content = f.read()
        url_pattern = r'https?://[^\s]+'
        urls.extend(re.findall(url_pattern, content))

url_counts = defaultdict(int)
for url in urls:
    domain = re.sub(r'^https?://|/$', '', url).split('/')[0]
    url_counts[domain] += 1

most_referenced_domain = max(url_counts.items(), key=lambda x: x[1])[0]

print(most_referenced_domain)