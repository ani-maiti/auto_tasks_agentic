import os
import zipfile
import tarfile
from collections import defaultdict, Counter
import csv

archives = [
    './cpython/Lib/test/test_importlib/namespace_pkgs/nested_portion1.zip',
    './cpython/Lib/test/test_importlib/namespace_pkgs/top_level_portion1.zip',
    './cpython/Lib/test/test_importlib/namespace_pkgs/missing_directory.zip',
    './cpython/Lib/test/archivetestdata/testtar.tar',
    './cpython/Lib/test/archivetestdata/zipdir.zip',
    './cpython/Lib/test/archivetestdata/recursion.tar',
    './cpython/Lib/test/archivetestdata/zipdir_backslash.zip',
    './cpython/Lib/test/archivetestdata/zip_cp437_header.zip'
]

inventory = defaultdict(list)

for archive in archives:
    if archive.endswith('.zip'):
        with zipfile.ZipFile(archive, 'r') as z:
            for file_info in z.infolist():
                inventory[file_info.filename].append(archive)
    elif archive.endswith('.tar'):
        try:
            with tarfile.open(archive, 'r') as t:
                for member in t.getmembers():
                    inventory[member.name].append(archive)
        except tarfile.ReadError:
            print(f"Failed to read {archive} as tar")

# Save inventory to CSV
with open('archive_inventory.csv', 'w', newline='') as csvfile:
    fieldnames = ['filename', 'archives']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for filename, archives in inventory.items():
        writer.writerow({'filename': filename, 'archives': ', '.join(archives)})

# Generate report
duplicates = {filename: archives for filename, archives in inventory.items() if len(archives) > 1}

with open('duplicate_report.txt', 'w') as reportfile:
    reportfile.write("Duplicate Files Report\n")
    reportfile.write("======================\n")
    for filename, archives in duplicates.items():
        reportfile.write(f"{filename}: Found in {len(archives)} archives - {', '.join(archives)}\n")

# Print the most frequently occurring filename
filename_counts = Counter(filename for filename in inventory.keys())
most_frequent_filename = filename_counts.most_common(1)[0]
print(f"Most frequently occurring filename: {most_frequent_filename[0]} (occurred {most_frequent_filename[1]} times)")