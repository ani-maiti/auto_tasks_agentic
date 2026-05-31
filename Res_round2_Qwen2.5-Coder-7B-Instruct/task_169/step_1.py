import os

# List all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Filter out non-text files
text_files = [f for f in files if f.endswith('.txt')]

print(f"Text files found: {text_files}")