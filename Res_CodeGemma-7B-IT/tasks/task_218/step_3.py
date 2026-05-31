# Print the top ten domains
top_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)[:10]

for domain, references in top_domains:
    print(f"- {domain}: {references}")