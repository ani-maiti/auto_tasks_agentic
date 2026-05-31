import os

def find_empty_directories(root_dir):
    empty_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if not filenames and not dirnames:
            empty_dirs.append(dirpath)
    return empty_dirs

root_directory = '.'  # Change this to the directory you want to check
empty_dirs = find_empty_directories(root_directory)

for dir_path in empty_dirs:
    print(dir_path)
```

This script walks through the specified directory and its subdirectories, checking for directories that contain no files or other directories. It then prints out the paths of these empty directories. You can change `root_directory` to the path of the directory you want to inspect.