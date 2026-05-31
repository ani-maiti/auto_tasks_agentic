# Filter out non-text files and count word frequencies
import os
from collections import Counter
import re

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        words = re.findall(r'\b\w+\b', content.lower())
        return Counter(words)

all_text_files = [f for f in os.listdir('.') if f.endswith('.txt')]
word_counts = Counter()

for file in all_text_files:
    word_counts += count_words(file)

# Exclude stop words
with open('stop_words.txt', 'r') as stop_words_file:
    stop_words = set(stop_words_file.read().split())

filtered_word_counts = {word: count for word, count in word_counts.items() if word not in stop_words}

# Get the top 100 words
top_100_words = filtered_word_counts.most_common(100)

# Save the top 100 words to a file
with open('top_100_words.txt', 'w') as output_file:
    for word, count in top_100_words:
        output_file.write(f'{word}: {count}\n')

print("Top 100 words saved to 'top_100_words.txt'")