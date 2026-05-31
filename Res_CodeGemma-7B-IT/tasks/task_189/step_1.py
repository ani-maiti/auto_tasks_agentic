import os

for filename in os.listdir("."):
    try:
        os.stat(filename)
    except FileNotFoundError:
        print(filename)