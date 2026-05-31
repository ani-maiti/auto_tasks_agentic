import os
import zipfile
import tarfile
import rarfile
from collections import defaultdict

archive_files = []
for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith(('.zip', '.tar.gz', '.rar')):
            archive_files.append(os.path.join(root, file))

print(f"Found {len(archive_files)} archive files.")