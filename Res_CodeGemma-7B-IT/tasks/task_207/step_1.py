import os
from collections import Counter

# Get all text files in the current directory
text_files = [f for f in os.listdir('.') if f.endswith('.txt')]

# Create an empty list to store word frequencies
word_frequencies = []

# Iterate through each text file
for file in text_files:
    # Open the file and read its contents
    with open(file, 'r') as f:
        text = f.read()

    # Split the text into words
    words = text.split()

    # Add the words to the list of word frequencies
    word_frequencies.extend(words)

# Remove stop words
stop_words = ['the', 'and', 'of', 'a', 'in', 'to', 'is', 'it', 'you', 'that', 'he', 'she', 'we', 'they', 'this', 'in', 'on', 'at', 'for', 'but', 'not', 'if', 'else', 'when', 'where', 'how', 'why']
word_frequencies = [word for word in word_frequencies if word not in stop_words]

# Count the occurrences of each word
word_counts = Counter(word_frequencies)

# Get the most common words
most_common_words = word_counts.most_common(100)

# Print the top 100 words
for word, count in most_common_words:
    print(f'{word}: {count}')