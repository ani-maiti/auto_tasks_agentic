import hashlib
import os

# Get list of txt files
txt_files = [f for f in os.listdir('.') if f.endswith('.txt') and os.path.isfile(f)]

# Compute SHA256 hash for each file
for file in txt_files:
    sha256_hash = hashlib.sha256()
    with open(file, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    print(f"{sha256_hash.hexdigest()}  {file}")