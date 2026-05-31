import os

for filename in os.listdir("."):
    if os.path.islink(filename):
        print(f"Symlink: {filename} -> {os.readlink(filename)}")