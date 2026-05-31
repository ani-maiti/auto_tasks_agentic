for filename in ["file1.txt", "file2.txt", "file3.txt"]:
    try:
        with open(filename, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        print(f"SHA256 hash of {filename}: {file_hash}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")