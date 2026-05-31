# Define the list of file paths again
file_paths = [
    "_log.json",
    "./tasks/task_054/step_2_log.json",
    # Add more file paths as needed
]

# Ensure all file paths exist before attempting to load them
import os

for file_path in file_paths[:]:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        file_paths.remove(file_path)

# Load JSON files
data = load_json_files(file_paths)

# Find numeric fields
numeric_fields = find_numeric_fields(data)

# Compute distributions
distributions = compute_distributions(numeric_fields)

# Generate Markdown summary
markdown_summary = generate_markdown_summary(distributions)

# Save to Markdown file
with open('statistical_summary.md', 'w') as file:
    file.write(markdown_summary)

print("Markdown summary saved to 'statistical_summary.md'")