import os
import re

# Get all Markdown files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.md')]

# Create a dictionary to store headings and their locations
headings = {}

# Iterate through each file
for file in files:
    # Open the file and read its contents
    with open(file, 'r') as f:
        contents = f.read()

    # Find all headings in the file
    matches = re.findall(r'## (.*?)\n', contents)

    # Add the headings to the dictionary, along with the file name
    for heading in matches:
        if heading in headings:
            headings[heading].append(file)
        else:
            headings[heading] = [file]

# Create a report of duplicated headings
report = []
for heading, files in headings.items():
    if len(files) > 1:
        report.append((heading, files))

# Save the report to a CSV file
with open('heading_report.csv', 'w') as f:
    f.write('Heading,File(s)\n')
    for heading, files in report:
        f.write(f'{heading},{", ".join(files)}\n')

print('Report saved to heading_report.csv')