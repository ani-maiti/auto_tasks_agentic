import os

files = [f for f in os.listdir('.') if f.endswith('.sh')]

for file in files:
    print(file)