import csv
from collections import Counter
import re

# Read titles from file
with open('titles.txt', 'r') as f:
    titles = [line.strip() for line in f.readlines() if line.strip()]

# Function to extract keywords
def extract_keywords(title):
    # Convert to lowercase and remove punctuation
    title = re.sub(r'[^\w\s]', '', title.lower())
    # Split into words and filter out common stop words
    words = title.split()
    stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can'}
    return [word for word in words if word not in stop_words and len(word) > 2]

# Extract all keywords
all_keywords = []
for title in titles:
    keywords = extract_keywords(title)
    all_keywords.extend(keywords)

# Count frequencies
keyword_freq = Counter(all_keywords)

# Save to CSV
with open('keyword_frequency.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Keyword', 'Frequency'])
    for keyword, freq in keyword_freq.most_common():
        writer.writerow([keyword, freq])

print(f"Collected {len(titles)} titles")
print(f"Found {len(keyword_freq)} unique keywords")
print("Saved results to keyword_frequency.csv")