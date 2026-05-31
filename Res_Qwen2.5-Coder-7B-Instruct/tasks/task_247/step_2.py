with open('text_files.txt', 'r') as file:
    text_files = file.read().splitlines()
print(f"Found {len(text_files)} text files.")