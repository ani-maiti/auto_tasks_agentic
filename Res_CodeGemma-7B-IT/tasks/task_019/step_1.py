import os

for filename in os.listdir("."):
    if os.path.islink(filename):
        print(f"Found broken symbolic link: {filename}")