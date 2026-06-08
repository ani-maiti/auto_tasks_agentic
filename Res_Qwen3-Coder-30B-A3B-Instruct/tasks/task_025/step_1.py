import os
import json

def get_file_sizes(directory):
    file_summary = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                file_summary.append({
                    "path": file_path,
                    "size": size
                })
            except OSError:
                # Handle files that can't be accessed
                continue
    
    return file_summary

# Get current directory
current_directory = "."

# Generate JSON summary
summary = get_file_sizes(current_directory)

# Print as JSON
print(json.dumps(summary, indent=2))