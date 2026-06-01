print("Duplicate files found based on SHA256 hashes:")
import sys
from collections import defaultdict

hash_dict = defaultdict(list)

for line in sys.stdin:
    hash_value, file_path = line.strip().split('  ')
    hash_dict[hash_value].append(file_path)

for hash_value, file_paths in hash_dict.items():
    if len(file_paths) > 1:
        print(f"Hash: {hash_value}")
        for file_path in file_paths:
            print(f"  {file_path}")