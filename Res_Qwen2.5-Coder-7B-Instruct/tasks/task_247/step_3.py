import os
from collections import defaultdict

readability_scores = defaultdict(float)

for file_path in text_files:
    with open(file_path, 'r') as file:
        content = file.read()
        # Placeholder for readability score calculation
        readability_score = len(content.split()) / 100  # Simplified example
        readability_scores[file_path] = readability_score

sorted_files = sorted(readability_scores.items(), key=lambda x: x[1])
easiest_file = sorted_files[0][0]
print(f"The easiest file to read is: {easiest_file}")