import re
from collections import defaultdict

def read_sentences(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # Split content into sentences using regex
        sentences = re.split(r'(?<=[.!?]) +', content)
        return sentences

sentence_counts = defaultdict(list)

for file in text_files:
    sentences = read_sentences(file)
    for sentence in sentences:
        sentence_counts[sentence].append(file)

# Filter out sentences that appear in only one file
duplicated_sentences = {sentence: files for sentence, files in sentence_counts.items() if len(files) > 1}

print(duplicated_sentences)