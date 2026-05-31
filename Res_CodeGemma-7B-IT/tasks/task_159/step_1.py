import os

for filename in os.listdir("."):
    if os.path.getsize(filename) == 0:
        print(filename)