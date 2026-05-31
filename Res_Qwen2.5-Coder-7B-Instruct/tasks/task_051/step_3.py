import os

def find_long_directories(path):
    long_dirs = []
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            if len(dir_name) > 20:
                long_dirs.append(os.path.join(root, dir_name))
    return long_dirs

long_dirs = find_long_directories('.')
if long_dirs:
    print("Long directories found:")
    for dir_path in long_dirs:
        print(dir_path)
else:
    print("No directories with names longer than 20 characters found.")