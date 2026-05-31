import os

files = os.listdir('.')

for file in files:
    print(os.path.abspath(file))