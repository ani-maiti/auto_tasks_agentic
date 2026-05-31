import hashlib

paragraph_hashes = {}

for file_path in text_files:
    with open(file_path, 'r') as file:
        content = file.read()
        paragraphs = content.split('\n\n')
        for paragraph in paragraphs:
            hash_object = hashlib.md5(paragraph.encode())
            hash_value = hash_object.hexdigest()
            if hash_value in paragraph_hashes:
                paragraph_hashes[hash_value].append((file_path, paragraph))
            else:
                paragraph_hashes[hash_value] = [(file_path, paragraph)]

duplicates = {hash_value: info for hash_value, info in paragraph_hashes.items() if len(info) > 1}

print(f"Found {len(duplicates)} duplicate paragraphs across files.")