import os

for dirpath, dirnames, filenames in os.walk("."):
    if len(filenames) > 100:
        print(dirpath)