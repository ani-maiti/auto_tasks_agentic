import os
import csv

# Get all archives in the current directory
archives = [f for f in os.listdir('.') if f.endswith('.tar.gz')]

# Create a list to store the analysis results
analysis = []

# Iterate through each archive
for archive in archives:
    # Extract the archive contents
    # ... (code to extract archive contents)

    # Get a list of files in the archive
    archive_files = os.listdir('archive_contents')

    # Compare file inventories across archives
    for other_archive in archives:
        if other_archive != archive:
            # Extract the other archive contents
            # ... (code to extract other archive contents)

            # Get a list of files in the other archive
            other_archive_files = os.listdir('other_archive_contents')

            # Find common files
            common_files = set(archive_files).intersection(other_archive_files)

            # Add the analysis result to the list
            analysis.append({
                'archive': archive,
                'other_archive': other_archive,
                'common_files': list(common_files)
            })

# Save the analysis to a CSV file
with open('analysis.csv', 'w', newline='') as csvfile:
    fieldnames = ['archive', 'other_archive', 'common_files']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(analysis)