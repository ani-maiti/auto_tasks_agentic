import os

for filename in os.listdir("."):
    if filename.count(".") > 1:
        print(filename)