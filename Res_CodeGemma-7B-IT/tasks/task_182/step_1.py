import os

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
            # Check if the line starts with a heading level
            if line.startswith("#"):
                # Increment the count for the corresponding heading level
                heading_counts[line[0]] += 1

# Print the heading counts
print(heading_counts)