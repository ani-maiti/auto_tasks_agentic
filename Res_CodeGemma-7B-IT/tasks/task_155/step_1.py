import os

for filename in os.listdir("."):
    if filename[0].isdigit():
        print(filename)