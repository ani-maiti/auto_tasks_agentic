import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file), "r") as f:
                for line in f:
                    if "FIXME" in line:
                        print(os.path.join(root, file))
                        break