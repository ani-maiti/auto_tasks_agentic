total_chars = sum(len(open(file).read()) for file in text_files)
print(f"Total number of characters across all text files: {total_chars}")