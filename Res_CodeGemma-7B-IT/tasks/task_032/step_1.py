import hashlib
import os

for filename in os.listdir("."):
    if filename.endswith(".py"):
        with open(filename, "rb") as f:
            data = f.read()
        hash = hashlib.md5(data).hexdigest()
        print(f"{filename}: {hash}")