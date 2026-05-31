import os

count = 0
for filename in os.listdir("."):
    if filename.endswith(".md"):
        with open(filename, "r") as f:
            for line in f:
                if line.startswith("#"):
                    count += 1
print(count)