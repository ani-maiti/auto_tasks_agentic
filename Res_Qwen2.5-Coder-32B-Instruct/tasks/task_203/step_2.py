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

results = []

def get_largest_file_in_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as z:
        largest_file = max(z.infolist(), key=lambda x: x.file_size)
        return largest_file.filename, largest_file.file_size

def get_largest_file_in_tar(tar_path):
    with tarfile.open(tar_path, 'r') as t:
        largest_file = max(t.getmembers(), key=lambda x: x.size)
        return largest_file.name, largest_file.size

for archive in archives:
    if archive.endswith('.zip'):
        filename, size = get_largest_file_in_zip(archive)
    elif archive.endswith('.tar') or archive.endswith('.tar.gz') or archive.endswith('.tgz'):
        filename, size = get_largest_file_in_tar(archive)
    else:
        continue
    results.append((os.path.basename(archive), filename, size))

with open('largest_files.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Archive', 'Largest File', 'Size'])
    writer.writerows(results)

print("CSV file created with results.")