import os
import zipfile
import tarfile
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

archive_contents = {}

def list_files_in_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as z:
        return z.namelist()

def list_files_in_tar(tar_path):
    try:
        with tarfile.open(tar_path, 'r') as t:
            return t.getnames()
    except tarfile.ReadError:
        return []

for archive in archives:
    if archive.endswith('.zip'):
        archive_contents[archive] = list_files_in_zip(archive)
    elif archive.endswith('.tar') or archive.endswith('.tar.gz') or archive.endswith('.tgz'):
        archive_contents[archive] = list_files_in_tar(archive)

# Find common files across all archives
common_files = set.intersection(*map(set, archive_contents.values()))

# Save the analysis to CSV
with open('archive_comparison.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Archive', 'Files'])
    for archive, files in archive_contents.items():
        writer.writerow([archive, ', '.join(files)])

# Add common files section
with open('archive_comparison.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Common Files'])
    for file in common_files:
        writer.writerow([file])

print("Detailed analysis saved to archive_comparison.csv")