import json

with open('text_files.txt', 'r') as file:
    text_files = file.readlines()

# Remove newline characters
text_files = [file.strip() for file in text_files]

print(f"Found {len(text_files)} text files.")