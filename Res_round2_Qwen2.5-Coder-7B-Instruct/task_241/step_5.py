from collections import defaultdict

# Initialize the dictionary to store resolution counts
resolution_counts = defaultdict(int)

# Count the occurrences of each resolution
for image_path in image_files:
    with Image.open(image_path) as img:
        width, height = img.size
        resolution_key = f"{width}x{height}"
        resolution_counts[resolution_key] += 1

# Find the most common resolution
most_common_resolution = max(resolution_counts.items(), key=lambda x: x[1])

# Print the most common resolution
print(f"The most common resolution is {most_common_resolution[0]} with {most_common_resolution[1]} images.")

# Generate a distribution report
report = "Distribution Report:\n"
for resolution, count in resolution_counts.items():
    report += f"{resolution}: {count} images\n"

print(report)