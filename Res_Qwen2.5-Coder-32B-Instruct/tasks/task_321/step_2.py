import os
import zipfile
import tarfile
import csv

archives = open('archives.txt').read().splitlines()
inventory = []

def process_zip(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            inventory.append({
                'archive': file_path,
                'filename': file_info.filename,
                'size': file_info.file_size,
                'modified': file_info.date_time
            })

def process_tar(file_path):
    with tarfile.open(file_path, 'r') as tar_ref:
        for member in tar_ref.getmembers():
            inventory.append({
                'archive': file_path,
                'filename': member.name,
                'size': member.size,
                'modified': member.mtime
            })

for archive in archives:
    if archive.endswith('.zip'):
        process_zip(archive)
    elif archive.endswith('.tar') or archive.endswith('.tar.gz') or archive.endswith('.tgz'):
        process_tar(archive)

with open('inventory.csv', 'w', newline='') as csvfile:
    fieldnames = ['archive', 'filename', 'size', 'modified']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(inventory)

print("Inventory created and saved to inventory.csv")