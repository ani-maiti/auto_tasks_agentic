from collections import Counter

# Convert defaultdict to Counter for easier sorting
domain_counter = Counter(domain_count)

# Get the top 5 most common domains
top_domains = domain_counter.most_common(5)

print(top_domains)