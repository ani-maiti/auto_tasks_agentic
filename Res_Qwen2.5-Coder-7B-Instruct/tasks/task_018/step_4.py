import os

directories = [name for name in os.listdir('.') if os.path.isdir(name)]
print("Number of directories:", len(directories))