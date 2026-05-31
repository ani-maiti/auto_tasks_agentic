import os

for filename in os.listdir("."):
    if filename.endswith(".json"):
        print(filename)