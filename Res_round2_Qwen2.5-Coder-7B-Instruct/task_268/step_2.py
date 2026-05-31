import json
from collections import defaultdict
import numpy as np

def load_json_files(file_paths):
    data = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data.append(json.load(file))
    return data

def find_numeric_fields(data):
    numeric_fields = defaultdict(list)
    for item in data:
        for key, value in item.items():
            if isinstance(value, (int, float)):
                numeric_fields[key].append(value)
    return numeric_fields

def compute_distributions(numeric_fields):
    distributions = {}
    for field, values in numeric_fields.items():
        distributions[field] = {
            'mean': np.mean(values),
            'median': np.median(values),
            'std_dev': np.std(values),
            'min': np.min(values),
            'max': np.max(values)
        }
    return distributions

def generate_markdown_summary(distributions):
    markdown = "# Statistical Summary\n\n"
    for field, stats in distributions.items():
        markdown += f"## {field}\n\n"
        markdown += f"- **Mean**: {stats['mean']:.2f}\n"
        markdown += f"- **Median**: {stats['median']:.2f}\n"
        markdown += f"- **Standard Deviation**: {stats['std_dev']:.2f}\n"
        markdown += f"- **Min**: {stats['min']:.2f}\n"
        markdown += f"- **Max**: {stats['max']:.2f}\n\n"
    return markdown

# Load JSON files
file_paths = [
    "_log.json",
    "./tasks/task_054/step_2_log.json",
    # Add more file paths as needed
]

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