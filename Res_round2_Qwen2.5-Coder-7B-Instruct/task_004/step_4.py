import hashlib

def find_duplicate_files(directory):
    hashes = {}
    duplicates = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                content = f.read()
                file_hash = hashlib.md5(content).hexdigest()

                if file_hash in hashes:
                    duplicates[file_hash].append(file_path)
                else:
                    hashes[file_hash] = [file_path]

    return duplicates

duplicates = find_duplicate_files('.')
if duplicates:
    for hash_value, file_paths in duplicates.items():
        print(f"Duplicate files with hash {hash_value}:")
        for path in file_paths:
            print(path)
else:
    print("No duplicate files found.")