import os
import re

# Get all Markdown files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.md')]

# Initialize variables to track the file with the most headings and its count
max_headings = 0
max_headings_file = None

# Iterate over each Markdown file
for filename in files:
    # Read the file contents
    with open(filename, 'r') as f:
        content = f.read()

    # Count the number of headings
    headings_count = len(re.findall(r'#{1,6}', content))

    # Update the maximum heading count and file name
    if headings_count > max_headings:
        max_headings = headings_count
        max_headings_file = filename

# Print the file with the most headings
print(f"File with the most headings: {max_headings_file}")