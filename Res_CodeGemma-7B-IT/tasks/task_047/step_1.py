import os

for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".json"):
            print(os.path.join(root, filename))