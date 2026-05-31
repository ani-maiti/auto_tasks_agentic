import os

for filename in os.listdir("."):
    if " " in filename:
        print(filename)