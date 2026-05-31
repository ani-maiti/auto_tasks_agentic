import os

for filename in os.listdir("."):
    if os.path.isfile(filename) and os.path.getsize(filename) < 100:
        print(filename)