import os

for filename in os.listdir("."):
    if not filename.isascii():
        print(filename)