import zipfile
import tarfile
import gzip
import bz2
import lzma
from collections import Counter
import json

# Function to check if a file is a compressed archive
def is_compressed(file):
    return file.endswith('.zip') or file.endswith('.tar.gz') or file.endswith('.tgz') or \
           file.endswith('.tar.bz2') or file.endswith('.tb2') or file.endswith('.tar.xz') or \
           file.endswith('.gz') or file.endswith('.bz2') or file.endswith('.xz')

# Filter out non-compressed files
compressed_files = [f for f in files if is_compressed(f)]

# Initialize counters for different compression types
zip_counter = Counter()
tar_gz_counter = Counter()
tar_bz2_counter = Counter()
tar_xz_counter = Counter()

# Inspect each compressed file
for file in compressed_files:
    try:
        if file.endswith('.zip'):
            with zipfile.ZipFile(file, 'r') as zip_ref:
                for info in zip_ref.infolist():
                    _, ext = os.path.splitext(info.filename)
                    zip_counter[ext] += 1
        elif file.endswith('.tar.gz') or file.endswith('.tgz'):
            with tarfile.open(file, 'r:gz') as tar_ref:
                for member in tar_ref.getmembers():
                    _, ext = os.path.splitext(member.name)
                    tar_gz_counter[ext] += 1
        elif file.endswith('.tar.bz2') or file.endswith('.tb2'):
            with tarfile.open(file, 'r:bz2') as tar_ref:
                for member in tar_ref.getmembers():
                    _, ext = os.path.splitext(member.name)
                    tar_bz2_counter[ext] += 1
        elif file.endswith('.tar.xz'):
            with tarfile.open(file, 'r:xz') as tar_ref:
                for member in tar_ref.getmembers():
                    _, ext = os.path.splitext(member.name)
                    tar_xz_counter[ext] += 1
        elif file.endswith('.gz'):
            with gzip.open(file, 'rb') as gz_ref:
                pass
        elif file.endswith('.bz2'):
            with bz2.open(file, 'rb') as bz2_ref:
                pass
        elif file.endswith('.xz'):
            with lzma.open(file, 'rb') as xz_ref:
                pass
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Combine all counters into one
all_counters = {
    '.zip': zip_counter,
    '.tar.gz': tar_gz_counter,
    '.tar.bz2': tar_bz2_counter,
    '.tar.xz': tar_xz_counter,
    '.gz': Counter(),
    '.bz2': Counter(),
    '.xz': Counter()
}

# Save the report to JSON
with open('extension_frequency_report.json', 'w') as f:
    json.dump(all_counters, f, indent=4)

print("Report saved to extension_frequency_report.json")