import hashlib
import os

def get_file_hashes(folder):
    hashes = {}
    for filename in os.listdir(folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            with open(os.path.join(folder, filename), 'rb') as f:
                filehash = hashlib.md5(f.read()).hexdigest()
            hashes[filename] = filehash
    return hashes

def find_duplicates(hashes):
    duplicates = []
    for filename1, hash1 in hashes.items():
        for filename2, hash2 in hashes.items():
            if filename1 != filename2 and hash1 == hash2:
                duplicates.append((filename1, filename2))
    return duplicates

def save_duplicates_to_csv(duplicates, filename):
    with open(filename, 'w') as f:
        f.write('filename1,filename2\n')
        for filename1, filename2 in duplicates:
            f.write(f'{filename1},{filename2}\n')

# Example usage:
folder = '/path/to/images'
hashes = get_file_hashes(folder)
duplicates = find_duplicates(hashes)
save_duplicates_to_csv(duplicates, 'duplicates.csv')

# Print the largest duplicate group
largest_group = max(duplicates, key=len)
print(f'Largest duplicate group: {largest_group}')