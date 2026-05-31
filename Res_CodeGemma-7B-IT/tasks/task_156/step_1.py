import os

for filename in os.listdir("."):
    if filename.endswith(r"\d$"):
        print(filename)