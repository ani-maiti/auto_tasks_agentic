import os

# Step 2: Discover all text files in the current directory
text_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print(f"Found {len(text_files)} text files.")

# Step 3: Read content from all text files and store them in a dictionary
file_contents = {}
for file in text_files:
    with open(file, 'r') as f:
        content = f.read()
        file_contents[file] = content

print("Read contents from all text files.")