import os

total_chars = 0

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        with open(filename, "r") as f:
            total_chars += len(f.read())

print(f"Total characters: {total_chars}")