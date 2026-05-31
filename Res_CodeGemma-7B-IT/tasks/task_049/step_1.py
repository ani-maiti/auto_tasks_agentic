import os

for filename in os.listdir('.'):
    if os.access(filename, os.X_OK):
        print(filename)