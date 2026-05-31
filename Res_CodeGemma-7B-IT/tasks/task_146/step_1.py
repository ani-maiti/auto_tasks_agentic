import glob

files = glob.glob('**/*.py')

for file in files:
    with open(file, 'r') as f:
        contents = f.read()
        if 'import requests' in contents:
            print(file)