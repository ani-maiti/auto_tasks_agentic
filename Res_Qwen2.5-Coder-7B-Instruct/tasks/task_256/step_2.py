# Step 2: Read content from all text files and store them in a dictionary
file_contents = {}
for file in text_files:
    with open(file, 'r') as f:
        content = f.read()
        file_contents[file] = content

print("Read contents from all text files.")