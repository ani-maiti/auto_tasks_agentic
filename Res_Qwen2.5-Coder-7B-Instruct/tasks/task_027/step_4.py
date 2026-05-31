import os

# List all files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.md')]

if len(files) == 0:
    print("No markdown files found. Exiting.")
else:
    # Initialize counter for headings
    heading_count = 0
    
    # Process each markdown file
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Count headings using regular expression
            import re
            headings = re.findall(r'^(#{1,6})\s.*$', content, re.MULTILINE)
            heading_count += len(headings)
    
    print(f"Total number of headings: {heading_count}")