import os
import hashlib
from collections import defaultdict

def get_file_hash(filepath):
    """Calculate SHA256 hash of a file"""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception:
        return None

def find_duplicates(directory):
    """Find duplicate files in directory based on SHA256 hashes"""
    hashes = defaultdict(list)
    
    # Walk through directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = get_file_hash(filepath)
            if file_hash:
                hashes[file_hash].append(filepath)
    
    # Filter out hashes that appear only once
    duplicates = {k: v for k, v in hashes.items() if len(v) > 1}
    return duplicates

# Find duplicates in current directory
duplicates = find_duplicates(".")

# Print results
print(f"Found {len(duplicates)} sets of duplicate files")
if duplicates:
    for i, (hash_val, file_list) in enumerate(duplicates.items(), 1):
        print(f"\nSet {i}:")
        print(f"Hash: {hash_val}")
        for file_path in file_list:
            print(f"  {file_path}")
else:
    print("No duplicate files found.")