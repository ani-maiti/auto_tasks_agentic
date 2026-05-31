# Step 2: Read the list of text files and store them in a Python list
with open('text_files.txt', 'r') as file:
    text_files = [line.strip() for line in file.readlines()]
print(f"Found {len(text_files)} text files.")