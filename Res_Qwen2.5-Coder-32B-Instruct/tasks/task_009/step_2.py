import hashlib

files = ["large_files.txt", "system_prompt_body.txt", "task_descriptions_all.txt", "task_descriptions.txt"]

for file in files:
    with open(file, "rb") as f:
        data = f.read()
        sha256_hash = hashlib.sha256(data).hexdigest()
        print(f"SHA256 hash of {file}: {sha256_hash}")