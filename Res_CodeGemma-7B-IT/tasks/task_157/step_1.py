import os

for filename in os.listdir("."):
    if filename.isupper():
        print(filename)