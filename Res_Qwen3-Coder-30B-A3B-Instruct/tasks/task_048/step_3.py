import os

def get_all_absolute_paths():
    all_paths = []
    for root, dirs, files in os.walk('/'):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                # Check if path is readable
                os.access(filepath, os.R_OK)
                all_paths.append(os.path.abspath(filepath))
            except:
                # Skip files we can't access
                continue
    return all_paths

# Get a sample of paths to verify functionality
paths = get_all_absolute_paths()
print(f"Found {len(paths)} paths")
print("First 10 paths:")
for i, path in enumerate(paths[:10]):
    print(path)