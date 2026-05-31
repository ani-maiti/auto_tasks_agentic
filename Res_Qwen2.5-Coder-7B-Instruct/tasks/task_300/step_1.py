import os

# Step 1: Discover all XML files in the current directory and its subdirectories
xml_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.xml'):
            xml_files.append(os.path.join(root, file))

print(f"Found {len(xml_files)} XML files.")