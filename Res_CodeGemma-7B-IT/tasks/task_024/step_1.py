import os

for root, _, files in os.walk("."):
    for filename in files:
        if not os.path.islink(os.path.join(root, filename)):
            print(os.path.join(root, filename))