import glob
import re
from collections import defaultdict

# Find all text files in the current directory
text_files = glob.glob("*.txt")

# Create a dictionary to store sentence counts
sentence_counts = defaultdict(int)

# Iterate over each text file
for filename in text_files:
    with open(filename, "r") as f:
        # Read the file contents
        text = f.read()

        # Split the text into sentences
        sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s", text)

        # Count the occurrences of each sentence
        for sentence in sentences:
            sentence_counts[sentence] += 1

# Create a list of duplicated sentences
duplicated_sentences = [sentence for sentence, count in sentence_counts.items() if count > 1]

# Create a report of duplicated sentences
report = {
    "total_files": len(text_files),
    "total_sentences": len(sentences),
    "duplicated_sentences": duplicated_sentences,
}

# Save the report to a JSON file
import json
with open("sentence_duplicates.json", "w") as f:
    json.dump(report, f)

# Print the report
print(report)