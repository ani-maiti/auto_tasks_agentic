import os

# Get all text files in the current directory
files = [f for f in os.listdir() if f.endswith('.txt')]

# Create a dictionary to store the paragraphs and their counts
paragraphs = {}

# Iterate through the files and extract paragraphs
for file in files:
    with open(file, 'r') as f:
        for line in f:
            paragraph = line.strip()
            if paragraph not in paragraphs:
                paragraphs[paragraph] = 0
            paragraphs[paragraph] += 1

# Find the paragraphs that appear more than once
duplicates = [p for p, c in paragraphs.items() if c > 1]

# Create a report of the duplicates
report = f"Found {len(duplicates)} duplicate paragraphs:\n\n"
for paragraph in duplicates:
    report += f"- {paragraph}\n"

# Print the report
print(report)

# Print the largest duplicated block
largest_block = max(paragraphs.values())
for paragraph, count in paragraphs.items():
    if count == largest_block:
        print(f"\nLargest duplicated block:\n\n{paragraph}\n")