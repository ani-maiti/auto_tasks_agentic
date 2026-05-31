import os
import re

# Get a list of text files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.txt')]

# Initialize a set to store unique words
unique_words = set()

# Iterate over files and extract unique words
for file in files:
    with open(file, 'r') as f:
        text = f.read()
        words = re.findall(r'\b\w+\b', text)
        unique_words.update(words)

# Print the number of unique words
print(len(unique_words))