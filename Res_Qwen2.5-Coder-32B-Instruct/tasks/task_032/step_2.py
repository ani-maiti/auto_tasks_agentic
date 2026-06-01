import hashlib

def compute_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

files = ["generate_code_model_run1.py", "generate_code_model_run.py", "test.py"]
for file in files:
    print(f"MD5 hash of {file}: {compute_md5(file)}")