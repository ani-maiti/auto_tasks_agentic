# Check if the file counts dictionary is empty
if not file_counts:
    print("No image files found.")
    exit(1)

# Find the extension with the highest count
most_common_extension = max(file_counts, key=file_counts.get)

# Print the most common extension
print(f"The most common image extension is {most_common_extension}")