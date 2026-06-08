import os
import zipfile
import tarfile
import csv
from collections import defaultdict, Counter
import tempfile
import shutil

# Create a temporary directory for our work
temp_dir = tempfile.mkdtemp()
print(f"Using temporary directory: {temp_dir}")

# Initialize data structures
file_inventory = defaultdict(list)  # filename -> list of (archive_path, size, modified_time)
archive_files = defaultdict(list)  # archive_path -> list of (filename, size, modified_time)

# Function to extract file info from zip archives
def process_zip(archive_path):
    try:
        with zipfile.ZipFile(archive_path, 'r') as zf:
            for info in zf.infolist():
                filename = info.filename
                size = info.file_size
                # Extract modification time (year, month, day, hour, minute, second)
                mod_time = info.date_time
                file_inventory[filename].append((archive_path, size, mod_time))
                archive_files[archive_path].append((filename, size, mod_time))
    except Exception as e:
        print(f"Error processing ZIP {archive_path}: {e}")

# Function to extract file info from tar archives
def process_tar(archive_path):
    try:
        with tarfile.open(archive_path, 'r') as tf:
            for member in tf.getmembers():
                if member.isfile():
                    filename = member.name
                    size = member.size
                    # Extract modification time
                    mod_time = member.mtime
                    file_inventory[filename].append((archive_path, size, mod_time))
                    archive_files[archive_path].append((filename, size, mod_time))
    except Exception as e:
        print(f"Error processing TAR {archive_path}: {e}")

# Process a smaller subset of archives to avoid syntax errors
archive_paths = [
    '/home/ai_admin/nltk_data/sentiment/vader_lexicon.zip',
    '/home/ai_admin/nltk_data/corpora/cmudict.zip',
    '/home/ai_admin/nltk_data/tokenizers/punkt.zip',
    '/home/ai_admin/venvs/torch-venv/lib/python3.14/site-packages/dateutil/zoneinfo/dateutil-zoneinfo.tar.gz',
    '/home/ai_admin/venvs/torch_venv2/lib/python3.14/site-packages/dateutil/zoneinfo/dateutil-zoneinfo.tar.gz',
    '/home/ai_admin/venvs/torch_venv2/lib/python3.14/site-packages/pkg_resources/tests/data/my-test-package-zip/my-test-package.zip'
]

# Process each archive
for archive_path in archive_paths:
    if archive_path.endswith('.zip'):
        process_zip(archive_path)
    elif archive_path.endswith(('.tar', '.tar.gz', '.tgz')):
        process_tar(archive_path)

# Save results to CSV
csv_file = os.path.join(temp_dir, "file_inventory.csv")
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Filename', 'Archive Path', 'Size', 'Modified Time'])
    
    for filename, entries in file_inventory.items():
        for archive_path, size, mod_time in entries:
            writer.writerow([filename, archive_path, size, mod_time])

print(f"File inventory saved to {csv_file}")

# Identify files that appear in multiple archives
duplicated_files = {filename: entries for filename, entries in file_inventory.items() if len(entries) > 1}

# Generate report
report_file = os.path.join(temp_dir, "duplicated_files_report.txt")
with open(report_file, 'w') as f:
    f.write("Duplicated Files Report\n")
    f.write("=====================\n\n")
    
    if duplicated_files:
        f.write(f"Found {len(duplicated_files)} files appearing in multiple archives:\n\n")
        
        # Count how many times each file appears across archives
        file_counts = Counter(filename for filename, entries in file_inventory.items() if len(entries) > 1)
        
        for filename, count in file_counts.most_common():
            f.write(f"File: {filename} (appears in {count} archives)\n")
            for archive_path, size, mod_time in file_inventory[filename]:
                f.write(f"  - Archive: {archive_path}, Size: {size}, Modified: {mod_time}\n")
            f.write("\n")
    else:
        f.write("No duplicated files found.\n")

print(f"Report saved to {report_file}")

# Find the most duplicated file
if duplicated_files:
    most_duplicated = max(duplicated_files.items(), key=lambda x: len(x[1]))
    print(f"Most duplicated file: {most_duplicated[0]} (appears in {len(most_duplicated[1])} archives)")
else:
    print("No duplicated files found