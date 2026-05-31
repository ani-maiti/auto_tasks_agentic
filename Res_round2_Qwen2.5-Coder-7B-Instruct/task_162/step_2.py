import os

files = [
    "./cpython/.git/objects/pack/pack-f39038638fd1255074908b2444777bbfcc38f781.pack",
    "./words.txt"
]

for file in files:
    size = os.path.getsize(file)
    if size > 50 * 1024 * 1024:
        print(f"{file} is larger than 50MB")