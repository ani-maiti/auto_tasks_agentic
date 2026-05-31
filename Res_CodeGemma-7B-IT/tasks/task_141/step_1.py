import os

for root, _, files in os.walk("."):
    for filename in files:
        if filename.endswith(".py"):
            with open(os.path.join(root, filename), "r") as f:
                code = f.read()
                num_classes = code.count("class ")
                print(f"File: {filename}, Classes: {num_classes}")