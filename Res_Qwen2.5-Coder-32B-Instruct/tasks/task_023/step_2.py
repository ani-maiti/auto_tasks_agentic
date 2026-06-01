import os

files = os.listdir('.')
extensions = {os.path.splitext(f)[1] for f in files if os.path.isfile(f)}
print("Unique file extensions:", extensions)
print("Number of unique file extensions:", len(extensions))