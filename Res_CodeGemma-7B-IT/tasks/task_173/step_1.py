import os

# Get the current directory
current_dir = os.getcwd()

# Search for files containing the phrase "machine learning"
for filename in os.listdir(current_dir):
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            content = f.read()
            if "machine learning" in content:
                print(filename)