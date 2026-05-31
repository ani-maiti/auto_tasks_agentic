import os
import re
import requests
import json

# Find all Markdown files
markdown_files = [f for f in os.listdir(".") if f.endswith(".md")]

# Extract links from Markdown files
links = []
for file in markdown_files:
    with open(file, "r") as f:
        text = f.read()
        links.extend(re.findall(r"\[.+\]\((.+)\)", text))

# Group links by domain
domains = {}
for link in links:
    domain = link.split("//")[-1].split("/")[0]
    if domain not in domains:
        domains[domain] = 0
    domains[domain] += 1

# Determine the most referenced domains
top_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)[:3]

# Retrieve homepage titles for top domains
titles = {}
for domain, _ in top_domains:
    try:
        response = requests.get("https://" + domain)
        titles[domain] = response.text
    except requests.exceptions.RequestException:
        titles[domain] = "N/A"

# Save results to JSON
data = {"domains": top_domains, "titles": titles}
with open("results.json", "w") as f:
    json.dump(data, f)