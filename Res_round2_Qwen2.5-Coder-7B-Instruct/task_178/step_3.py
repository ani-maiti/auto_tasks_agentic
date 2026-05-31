import os

# Get the current directory
current_dir = os.getcwd()

# List all files and directories in the current directory
items = [item for item in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, item))]

# Sort items by their total size
sorted_items = sorted(items, key=lambda x: sum(os.path.getsize(os.path.join(current_dir, x, f)) for f in os.listdir(os.path.join(current_dir, x))), reverse=True)

# Print the sorted list
for item in sorted_items:
    print(item)