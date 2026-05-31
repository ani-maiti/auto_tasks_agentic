import os
import csv

# Get a list of all archives
archives = [f for f in os.listdir('.') if f.endswith('.zip')]

# Create a dictionary to store file metadata
file_metadata = {}

# Iterate over each archive
for archive in archives:
    # Extract the archive
    os.system(f'unzip {archive}')

    # Get a list of files in the archive
    files = [f for f in os.listdir(archive[:-4])]

    # Iterate over each file
    for file in files:
        # Get file metadata
        file_size = os.path.getsize(os.path.join(archive[:-4], file))
        file_type = os.path.splitext(file)[1][1:]

        # Add file metadata to the dictionary
        if file not in file_metadata:
            file_metadata[file] = {'size': file_size, 'type': file_type, 'archives': []}
        file_metadata[file]['archives'].append(archive)

# Create a list of files that appear in multiple archives
duplicated_files = [f for f in file_metadata if len(file_metadata[f]['archives']) > 1]

# Save the results to a CSV file
with open('file_metadata.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['File', 'Size', 'Type', 'Archives'])
    for file, metadata in file_metadata.items():
        writer.writerow([file, metadata['size'], metadata['type'], ', '.join(metadata['archives'])])

# Generate a report
print('File Metadata Report:')
for file, metadata in file_metadata.items():
    print(f'{file}: {metadata["size"]} bytes, {metadata["type"]}')

# Print the most duplicated file
most_duplicated_file = max(file_metadata, key=lambda f: len(file_metadata[f]['archives']))
print(f'Most Duplicated File: {most_duplicated_file}')