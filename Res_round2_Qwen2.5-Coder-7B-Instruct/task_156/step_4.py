import os

files = [f for f in os.listdir('.') if f.endswith('.py')]

for file in files:
    print(file)