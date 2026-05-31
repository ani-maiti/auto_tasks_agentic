import os

# Step 1: Discover all text files in the current directory
text_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print(f"Found {len(text_files)} text files.")