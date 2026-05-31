import os

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        print(filename)