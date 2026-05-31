import os

for filename in os.listdir("."):
    if filename.startswith("."):
        print(filename)