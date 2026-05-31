import os

for entry in os.scandir("."):
    if entry.is_dir():
        print(entry.name)