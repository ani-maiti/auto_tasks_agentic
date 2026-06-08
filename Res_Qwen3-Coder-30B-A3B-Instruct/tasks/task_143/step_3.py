import os
import subprocess

# Find all Python files
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

# Get line counts for each file
file_line_counts = []
for file in python_files:
    try:
        result = subprocess.run(['wc', '-l', file], capture_output=True, text=True)
        line_count = int(result.stdout.split()[0])
        file_line_counts.append((line_count, file))
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Sort by line count (descending) and get top 10
file_line_counts.sort(reverse=True)
top_10 = file_line_counts[:10]

# Print results
for line_count, file_path in top_10:
    print(f"{line_count} lines - {file_path}")