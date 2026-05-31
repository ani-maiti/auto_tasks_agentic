import os

for filename in os.listdir("."):
    if filename.endswith(".md"):
        with open(filename, "r") as f:
            for line in f:
                if line.startswith("#"):
                    print(line)