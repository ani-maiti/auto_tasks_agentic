import os
import re
import csv

# Get the current directory
cwd = os.getcwd()

# Find all HTML files in the current directory tree
html_files = []
for root, _, files in os.walk(cwd):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

# Extract all hyperlinks from the HTML files
links = []
for html_file in html_files:
    with open(html_file, "r") as f:
        for line in f:
            match = re.search(r'<a\s+href="([^"]+)">', line)
            if match:
                links.append(match.group(1))

# Group links by domain
domains = {}
for link in links:
    domain = link.split("//")[1].split("/")[0]
    domains[domain] = domains.get(domain, 0) + 1

# Identify the most referenced domains
top_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)[:10]

# Save the analysis to CSV
with open("top_domains.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Domain", "References"])
    for domain, references in top_domains:
        writer.writerow([domain, references])

# Print the top ten domains
print("Top 10 Domains:")
for domain, references in top_domains:
    print(f"- {domain}: {references}")