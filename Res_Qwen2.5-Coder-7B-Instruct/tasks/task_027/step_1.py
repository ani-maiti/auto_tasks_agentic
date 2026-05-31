import os

# List all files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.md')]
print(f"Found {len(files)} markdown files.")