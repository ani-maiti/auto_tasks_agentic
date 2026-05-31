import os

for entry in os.listdir("."):
    if os.path.islink(entry):
        print(entry)