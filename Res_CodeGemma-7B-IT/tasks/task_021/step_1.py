import os

for filename in os.listdir("."):
    if os.path.isfile(filename):
        file_size = os.path.getsize(filename)
        if file_size > 10 * 1024 * 1024:
            print(filename)