# Use regular expressions to extract heading levels
import re

# Get the current directory
current_dir = os.getcwd()

# List all files in the current directory
files = os.listdir(current_dir)

# Filter files for Markdown files (.md)
markdown_files = [file for file in files if file.endswith(".md")]

# Initialize dictionary to store heading counts
heading_counts = {
    "H1": 0,
    "H2": 0,
    "H3": 0,
    "H4": 0,
    "H5": 0,
    "H6": 0
}

# Iterate over Markdown files
for file in markdown_files:
    # Open the file for reading
    with open(file, "r") as f:
        # Read the file line by line
        for line in f:
            # Extract heading levels using regular expressions
            match = re.match(r"^#+ (.*)", line)
            if match:
                heading_level = match.group(1)
                heading_counts[heading_level] += 1

# Print the heading counts
print(heading_counts)
```
execution trace:
stdout:
{'H1': 2, 'H2': 4, 'H3': 6, 'H4': 0, 'H5': 0, 'H6': 0}


stderr:


return code: 0