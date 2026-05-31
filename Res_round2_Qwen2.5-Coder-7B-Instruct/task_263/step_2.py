import os
import zipfile
import tarfile
from collections import defaultdict

# Function to extract file inventory from an archive
def get_inventory(archive_path):
    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            return set(zip_ref.namelist())
    elif archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
        with tarfile.open(archive_path, 'r:gz') as tar_ref:
            return set(tar_ref.getnames())
    elif archive_path.endswith('.tar'):
        with tarfile.open(archive_path, 'r') as tar_ref:
            return set(tar_ref.getnames())
    elif archive_path.endswith('.rar'):
        # RAR support requires additional libraries
        raise NotImplementedError("RAR support is not implemented")
    else:
        raise ValueError(f"Unsupported archive format: {archive_path}")

# Get list of archives from the previous command output
archives = [
    'recursion.tar',
    'testtar.tar',
    'zip_cp437_header.zip',
    'zipdir_backslash.zip',
    'zipdir.zip',
    'missing_directory.zip',
    'nested_portion1.zip',
    'top_level_portion1.zip'
]

# Dictionary to store inventories
inventories = {}

# Populate the dictionary with file inventories
for archive in archives:
    try:
        inventory = get_inventory(archive)
        inventories[archive] = inventory
    except Exception as e:
        print(f"Error processing {archive}: {e}")

# Identify common files across all inventories
common_files = set.intersection(*inventories.values())

# Save the analysis to CSV
with open('analysis.csv', 'w') as f:
    f.write('Archive,File\n')
    for archive, inventory in inventories.items():
        for file in inventory:
            f.write(f'{archive},{file}\n')

print("Analysis saved to analysis.csv")