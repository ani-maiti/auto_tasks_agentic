# Define the list of text files again
text_files = [f for f in files if f.endswith('.txt')]

total_chars = sum(len(open(file).read()) for file in text_files)
print(f"Total number of characters across all text files: {total_chars}")