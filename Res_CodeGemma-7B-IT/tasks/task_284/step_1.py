# Import libraries
import os
import re
import pandas as pd

# Define a function to extract information from a Markdown file
def extract_info(filename):
    with open(filename, 'r') as f:
        text = f.read()
    headings = re.findall(r'#+ (.*)', text)
    tables = re.findall(r'|.*|', text, re.DOTALL)
    code_blocks = re.findall(r'```(.*?)```', text, re.DOTALL)
    return headings, tables, code_blocks

# Get all Markdown files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.md')]

# Extract information from each file and store it in a list of dictionaries
data = []
for filename in files:
    headings, tables, code_blocks = extract_info(filename)
    data.append({
        'filename': filename,
        'headings': headings,
        'tables': tables,
        'code_blocks': code_blocks
    })

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Find duplicate sections across files
duplicates = df['headings'].apply(lambda x: set(x).intersection(set(df['headings'].sum())))

# Identify the most duplicated section title
most_duplicated_section = duplicates.apply(lambda x: list(x)[0])

# Generate a report
report = f"""
## Markdown Content Inventory Report

**Number of files:** {len(files)}

**Duplicate sections:** {len(duplicates)}

**Most duplicated section:** {most_duplicated_section[0]}
"""

# Save the report to a file
with open('report.txt', 'w') as f:
    f.write(report)

# Print the most duplicated section title
print(most_duplicated_section[0])