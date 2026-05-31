# Print the top 3 most referenced domains and their titles
for domain, title in zip(top_domains, titles.values()):
    print(f"{domain}: {title}")