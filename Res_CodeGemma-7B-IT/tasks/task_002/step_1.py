import os

total_lines = 0

for root, _, files in os.walk("."):
    for filename in files:
        if filename.endswith(".py"):
            with open(os.path.join(root, filename), "r") as f:
                total_lines += len(f.readlines())

print(total_lines)