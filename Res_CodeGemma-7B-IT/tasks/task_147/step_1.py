import os

for root, _, files in os.walk("."):
    for filename in files:
        if filename.endswith(".py"):
            with open(os.path.join(root, filename), "r") as f:
                for line in f:
                    if "TODO" in line:
                        print(os.path.join(root, filename))
                        break