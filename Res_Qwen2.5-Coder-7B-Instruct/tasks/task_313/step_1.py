import os
import glob

# Find all Markdown files in the current directory and subdirectories
markdown_files = glob.glob('**/*.md', recursive=True)

print(f"Found {len(markdown_files)} Markdown files.")