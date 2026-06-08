import os
import re
from collections import Counter

# Find all text files
text_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            text_files.append(os.path.join(root, file))

print(f"Found {len(text_files)} text files")

# Read all text files and build word frequency counter
word_counter = Counter()
stop_words = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
    'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 
    'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
    'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'i',
    'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
}

for file_path in text_files[:5]:  # Process first 5 files for testing
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            # Remove punctuation and split into words
            words = re.findall(r'\b[a-zA-Z]+\b', content)
            # Filter out stop words
            filtered_words = [word for word in words if word not in stop_words]
            word_counter.update(filtered_words)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Get top 100 most common words
top_words = word_counter.most_common(100)

# Print results
print("Top 100 most common words (excluding stop words):")
for i, (word, count) in enumerate(top_words, 1):
    print(f"{i:3d}. {word:<15} ({count})")

# Save to file
with open('word_frequency_report.txt', 'w') as f:
    f.write("Word Frequency Report\n")
    f.write("=" * 30 + "\n")
    for i, (word, count) in enumerate(top_words, 1):
        f.write(f"{i:3d}. {word:<15} ({count})\n")

print("\nReport saved to word_frequency_report.txt")