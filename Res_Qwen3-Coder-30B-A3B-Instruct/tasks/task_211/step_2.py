# Analyze collected titles for duplicates
titles_only = [title for _, title in page_titles]
title_counts = Counter(titles_only)

# Find duplicate titles
duplicate_titles = {title: count for title, count in title_counts.items() if count > 1}

print("Duplicate titles found:")
for title, count in duplicate_titles.items():
    print(f"  '{title}' appears {count} times")

# Generate report
print("\n--- REPORT ---")
print(f"Total pages crawled: {len(page_titles)}")
print(f"Unique titles: {len(set(titles_only))}")
print(f"Duplicate titles: {len(duplicate_titles)}")

# Show some sample data
print("\nSample of collected titles:")
for i, (url, title) in enumerate(page_titles[:10]):
    print(f"  {i+1}. {title}")

# Save results to file
with open('crawl_report.txt', 'w') as f:
    f.write("Website Crawl Report\n")
    f.write("====================\n\n")
    f.write(f"Total pages crawled: {len(page_titles)}\n")
    f.write(f"Unique titles: {len(set(titles_only))}\n")
    f.write(f"Duplicate titles: {len(duplicate_titles)}\n\n")
    
    if duplicate_titles:
        f.write("Duplicate titles:\n")
        for title, count in duplicate_titles.items():
            f.write(f"  '{title}' appears {count} times\n")
        f.write("\n")
    
    f.write("All page titles:\n")
    for url, title in page_titles:
        f.write(f"  {title}\n")

print("\nReport saved to crawl_report.txt")