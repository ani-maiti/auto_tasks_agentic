import os
import zipfile
import tarfile
from collections import defaultdict

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

print("Inventory built")